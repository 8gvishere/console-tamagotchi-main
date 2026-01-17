"""
Core pet logic, finite state machine, and ASCII animation for Tamagotchi.

Author: Buyan-Erdene Batsaikhan
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Any, List


class PetState(str, Enum):
    ALIVE = "alive"
    HUNGRY = "hungry"
    TIRED = "tired"
    BORED = "bored"
    DEAD = "dead"


@dataclass
class PetConfig:
    max_stat: int = 100
    min_stat: int = 0

    # Per-tick changes (when awake)
    hunger_per_tick: int = 2
    energy_per_tick: int = -1
    happiness_per_tick: int = -1

    # Per-tick changes (when sleeping)
    sleep_energy_gain_per_tick: int = 5
    sleep_hunger_increase_per_tick: int = 1
    sleep_happiness_change_per_tick: int = 0

    # Action effects
    feed_amount: int = 25
    play_happiness_gain: int = 20
    play_energy_cost: int = 10

    # Cooldown
    play_cooldown_ticks: int = 2

    # State thresholds
    hungry_threshold: int = 70
    tired_threshold: int = 30
    bored_threshold: int = 30

    # Death conditions
    death_hunger: int = 100
    death_energy: int = 0
    death_happiness: int = 0

    # Sleep control
    auto_sleep_energy_threshold: int = 15
    auto_wake_energy_threshold: int = 80

    # Visual action duration (ticks)
    action_visual_ticks: int = 3

    # ---------- Evolution settings ----------
    food_to_adult: int = 100



# Big ASCII sprites, per species and visual "mode"
# Cheap but good enough.
# species -> stage -> visual-mode -> frames
ASCII_SPRITES: Dict[str, Dict[str, Dict[str, List[str]]]] = {
    "cat": {
        "baby": {
            "idle": [
r"""
  /\_/\  
 ( >^< ) 
 /  ^  \ 
 \_/ \_/ 
""",
        ],
            "eat":  [
r"""
  /\_/\  
 ( =ω= ) 
 /  ^  \ 
 \_/ \_/ 
""",
        ],
            "sleep":[
r"""
  /\_/\  
 ( -^- )  zz
 /  ^  \ 
 \_/ \_/ 
""",
r"""
  /\_/\  
 ( -^- )  zzz
 /  ^  \ 
 \_/ \_/ 
""",
        ],
            "play": [
r"""
  /\_/\ ♪
 ( >o< ) 
 /  ^  \ 
 \_/ \_/ 
""",
r"""
♪ /\_/\  
 ( >o< ) 
 /  ^  \ 
 \_/ \_/ 
""",      
        ],
            "hungry":[
r"""
  /\_/\  
 ( ·_· ) 
 /  ^  \ 
 \_/ \_/ 
""",
r"""
  /\_/\  
 ( ;_; ) 
 /  ^  \ 
 \_/ \_/ 
""",        
        ],
            "tired":[
r"""
  /\_/\  
 ( -_- ) 
 /  ^  \ 
 \_/ \_/ 
""",
r"""
  /\_/\  
 ( -.- ) z
 /  ^  \ 
 \_/ \_/ 
""",
        ],
            "bored":[
r"""
  /\_/\  
 ( -^- ) 
 /  ^  \ 
 \_/ \_/ 
""",
        ],
            "dead": [
r"""
  /\_/\  
 ( x^x ) 
 /  ^  \ 
 \_/ \_/ 
""",
        ],
        },
        "adult": {
            "idle": [
r"""
  /\___/\  
 (  >^<  ) 
 /  | |  \ 
/   | |   \
\___/ \___/
""",
        ],
            "eat":  [
r"""
   /\___/\  
  (   >^<  ) 
 /  | |  \ 
/   | |   \
\___/ \___/
""",
r"""
   /\___/\  
  (   =ω=  ) 
 /  | |  \ 
/   | |   \
\___/ \___/
""",        
        ],
            "sleep":[
r"""
  /\___/\  
 (  -^-  )  zz
 /  | |  \ 
/   | |   \
\___/ \___/
""",
r"""
  /\___/\  
 (  -^-  )  zzz
 /  | |  \ 
/   | |   \
\___/ \___/
""",
        ],  
            "play": [
r"""
  /\___/\ ♪ 
 (  >o<  ) 
 /  | |  \ 
/   | |   \
\___/ \___/
""",
r"""
♪ /\___/\  
 (  >o<  ) 
 /  | |  \ 
/   | |   \
\___/ \___/
""",
        ],
            "hungry":[
r"""
  /\___/\  
 (  ·_·  )  
 /  | |  \ 
/   | |   \
\___/ \___/
""",
r"""
  /\___/\  
 (  ;_;  )  
 /  | |  \ 
/   | |   \
\___/ \___/
""",
        ],
            "tired":[
r"""
 /\___/\  
( -_-  ) 
 /  | |  \ 
/   | |   \
\___/ \___/
""",
r"""
 /\___/\  
( -.-  )   zz
 /  | |  \ 
/   | |   \
\___/ \___/
""",
        ],
            "bored":[
r"""
  /\___/\  
 (  -^-  ) 
 /  | |  \ 
/   | |   \
\___/ \___/
""",
        ],
            "dead": [
r"""
  /\___/\  
 (  x^x  ) 
 /  | |  \ 
/   | |   \
\___/ \___/
""",
        ], 
        },
    },
    "dog": {
        "baby": {
            "idle": [
r"""
  _____  
 /)UᴥU(\ 
 /  V  \ 
 \_/ \_/ 
""",
        ],
            "eat":  [
r"""
  _____  
 /)=ω=(\ 
 /  V  \ 
 \_/ \_/ 
""",
        ],
            "sleep":[
r"""
  _____  
 /)-ᴥ-(\  zz
 /  V  \ 
 \_/ \_/ 
""",
r"""
  _____  
 /)-ᴥ-(\  zzz
 /  V  \ 
 \_/ \_/ 
""",
        ],
            "play": [
r"""
  _____  
 /)^ᴥ^(\ 
 /  V  \ ⚽
 \_/ \_/ 
""",
r"""
  _____  ⚽
 /)^ᴥ^(\ 
 /  V  \ 
 \_/ \_/
""",      
        ],
            "hungry":[
r"""
  _____  
 /)·ᴥ·(\ 
 /  V  \ 
 \_/ \_/ 
""",
r"""
  _____  
 /);ᴥ;(\  
 /  V  \ 
 \_/ \_/ 
""",
        ],
            "tired":[ 
r"""
  _____  
 /)-ᴥ-(\ 
 /  V  \ 
 \_/ \_/ 
""",
r"""
  _____  
 /)-ᴥ-(\  zz
 /  V  \ 
 \_/ \_/ 
""",
        ],
            "bored":[
r"""
  _____  
 /)-ᴥ-(\ 
 /  V  \ 
 \_/ \_/ 
""",
        ],
            "dead": [
r"""
  _____  
 /)xᴥx(\ 
 /  V  \ 
 \_/ \_/ 
""",
        ],
        },
        "adult": {
            "idle": [
r"""
  /)   (\  
 /  UᴥU  \ 
(   | |   )
/   | |   \
\___/ \___/
""",
        ],
            "eat":  [
r"""
   /)   (\  
  /   UᴥU  \ 
(   | |   )
/   | |   \
\___/ \___/
""",
r"""
   /)   (\  
  /   =ω=  \ 
(   | |   )
/   | |   \
\___/ \___/
""",        ],
            "sleep":[
r"""
  /)   (\  
 /  -ᴥ-  \  zz
(   | |   )
/   | |   \
\___/ \___/
""",
r"""
  /)   (\  
 /  -ᴥ-  \  zzz
(   | |   )
/   | |   \
\___/ \___/
""",
        ],
            "play": [
r"""
  /)   (\ 
 /  ^ᴥ^  \ 
(   | |   ) ⚽
/   | |   \
\___/ \___/
""",
r"""
♪ /)   (\   ⚽
 /  ^ᴥ^  \ 
(   | |   )
/   | |   \
\___/ \___/
""",      ],
            "hungry":[
r"""
  /)   (\  
 /  ·ᴥ·  \  
(   | |   )
/   | |   \
\___/ \___/
""",
r"""
  /)   (\  
 /  ;ᴥ;  \  
(   | |   )
/   | |   \
\___/ \___/
""",
        ],
            "tired":[
r"""
 /)   (\  
/ -ᴥ-  \ 
(   | |   )
/   | |   \
\___/ \___/
""",
r"""
 /)   (\  
/ -ᴥ-  \   zz
(   | |   )
/   | |   \
\___/ \___/
""",
        ],
            "bored":[
r"""
  /)   (\  
 /  -ᴥ-  \ 
(   | |   )
/   | |   \
\___/ \___/
""",
        ],
            "dead": [
r"""
  /)   (\  
 /  xᴥx  \ 
(   | |   )
/   | |   \
\___/ \___/
""",
        ],        
        },
    },
    "dragon": {
        "baby": {
            "idle": [
r"""
   /\   
 [ +_+ ]
 /  |  \
 \_/ \_/
""",
        ],
            "eat":  [
r"""
   /\   
 [ =ω= ]
 /  |  \
 \_/ \_/
""",
        ],
            "sleep":[
r"""
   /\   
 [ -_- ]  zz
 /  |  \
 \_/ \_/
""",
r"""
   /\   
 [ -_- ]  zzz
 /  |  \
 \_/ \_/
""",
        ],
            "play": [
r"""
   /\   
 [ +.+ ] 
 /  |🔥\
 \_/ \_/
""",
r"""
   /\   
 [ +.+ ] 
 /🔥|🔥\
 \_/ \_/
""",      
        ],
            "hungry":[
r"""
   /\   
 [ ·_· ] 
 /  |  \
 \_/ \_/
""",
r"""
   /\   
 [ ;_; ] 
 /  |  \
 \_/ \_/
""",      
        ],
            "tired":[
r"""
   /\   
 [ -_- ]  
 /  |  \
 \_/ \_/
""",
r"""
   /\   
 [ -.- ]  zz
 /  |  \
 \_/ \_/
""",
        ],
            "bored":[
r"""
   /\   
 [ -_- ]
 /  |  \
 \_/ \_/
""",
        ],
            "dead": [
r"""
   /\   
 [ x_x ]
 /  |  \
 \_/ \_/
""",
        ],        
        },
        "adult": {
            "idle": [
r"""
      /\  
   <[ +_+ ]>
   /  | |  \
  /   | |   \
  \___/ \___==^
""",
        ],
            "eat":  [
r"""
       /\  
    <[  +_+ ]>
   /  | |  \
  /   | |   \
  \___/ \___==^
""",
r"""
       /\  
    <[  =ω= ]>
   /  | |  \
  /   | |   \
  \___/ \___==^
""",        
        ],
            "sleep":[
r"""
      /\  
   <[ -_- ]>  z
   /  | |  \
  /   | |   \
  \___/ \___==^
""",
r"""
      /\  
   <[ -_- ]>  zzz
   /  | |  \
  /   | |   \
  \___/ \___==^
""",
        ],
            "play": [
r"""
      /\   
   <[ +.+ ]>
   /  | |  \
  /   | | 🔥\
  \___/ \___==^
""",
r"""
      /\   
   <[ +.+ ]>
   /  | |  \
  / 🔥| |🔥 \
  \___/ \___==^
""",      
        ],
            "hungry":[
r"""
      /\   
   <[ ·_· ]>
   /  | |  \
  /   | |   \
  \___/ \___==^
""",
r"""
      /\   
   <[ ;_; ]>
   /  | |  \
  /   | |   \
  \___/ \___==^
""",      
        ],
            "tired":[
r"""
     /\  
  <[ -_- ]>  
   /  | |  \
  /   | |   \
  \___/ \___==^
""",
r"""
     /\  
  <[ -.- ]>   zz
   /  | |  \
  /   | |   \
  \___/ \___==^
""",
        ],
            "bored":[
r"""
      /\  
   <[ -_- ]>
   /  | |  \
  /   | |   \
  \___/ \___==^
""",
        ],
            "dead": [
r"""
      /\  
   <[ x_x ]>
   /  | |  \
  /   | |   \
  \___/ \___==^
""",
        ],
        },
    },
}


class Pet:
    """
    Tamagotchi pet with FSM and visual state.
    """

    def __init__(
        self,
        name: str,
        species: str = "cat",
        stage: str = "baby", 
        hunger: int = 20,
        happiness: int = 70,
        energy: int = 70,
        config: PetConfig | None = None,
    ) -> None:
        self.name = name
        self.species = species if species in ASCII_SPRITES else "cat"
        self._stage = stage if stage in ("baby", "adult") else "baby"

        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.total_food_eaten: int = 0

        self._config = config or PetConfig()

        self._state: PetState = PetState.ALIVE
        self._is_sleeping: bool = False
        self._play_cooldown: int = 0

        # For temporary visual actions: "eat", "play"
        self._visual_action: str | None = None
        self._visual_action_ticks_remaining: int = 0

        self._update_state()

    @property
    def state(self) -> PetState:
        return self._state

    @property
    def is_sleeping(self) -> bool:
        return self._is_sleeping

    # ------------- Core loop -------------

    def tick(self) -> None:
        if self._state == PetState.DEAD:
            self._visual_action = None
            self._visual_action_ticks_remaining = 0
            return

        # Central per-tick update: route through a single place so all
        # stat changes, cooldowns, and auto sleep/wake logic stay in sync.
        if self._is_sleeping:
            self._apply_sleep_tick()
        else:
            self._apply_awake_tick()

        if self._play_cooldown > 0:
            self._play_cooldown -= 1

        # Decay temporary visual action
        if self._visual_action_ticks_remaining > 0:
            self._visual_action_ticks_remaining -= 1
            if self._visual_action_ticks_remaining == 0:
                self._visual_action = None

        self._maybe_auto_sleep_or_wake()

        self._clamp_stats()
        self._update_state()

    # ------------- Actions -------------

    def feed(self) -> bool:
        """Feed the pet to reduce hunger and slightly increase happiness.

        Returns:
            bool: True if the action had an effect, False if feeding is
            ignored (for example when the pet is dead, sleeping, or
            already full).
        """
        if self._state == PetState.DEAD or self._is_sleeping:
                return False
        if self.hunger <= 0:
                return False

        before = self.hunger

        self.hunger -= self._config.feed_amount
        self._clamp_stats()

        eaten = max(0, before - self.hunger)
        self.total_food_eaten += eaten

        self._check_evolution()

        self._update_state()
        self._set_visual_action("eat")
        return True

    def play(self) -> bool:
        if self._state == PetState.DEAD or self._is_sleeping:
            return False
        if self.energy <= self._config.play_energy_cost:
            return False
        if self._play_cooldown > 0:
            return False

        self.happiness += self._config.play_happiness_gain
        self.energy -= self._config.play_energy_cost
        self._play_cooldown = self._config.play_cooldown_ticks

        self._clamp_stats()
        self._update_state()

        self._set_visual_action("play")
        return True

    def sleep(self) -> bool:
        if self._state == PetState.DEAD or self._is_sleeping:
            return False
        self._is_sleeping = True
        self._visual_action = None
        self._visual_action_ticks_remaining = 0
        return True

    def wake(self) -> bool:
        if self._state == PetState.DEAD or not self._is_sleeping:
            return False
        self._is_sleeping = False
        self._update_state()
        return True

    # ------------- Internal helpers -------------

    def _set_visual_action(self, action: str) -> None:
        self._visual_action = action
        self._visual_action_ticks_remaining = self._config.action_visual_ticks

    def _apply_awake_tick(self) -> None:
        cfg = self._config
        self.hunger += cfg.hunger_per_tick
        self.energy += cfg.energy_per_tick
        self.happiness += cfg.happiness_per_tick

    def _apply_sleep_tick(self) -> None:
        cfg = self._config
        self.energy += cfg.sleep_energy_gain_per_tick
        self.hunger += cfg.sleep_hunger_increase_per_tick
        self.happiness += cfg.sleep_happiness_change_per_tick

    def _maybe_auto_sleep_or_wake(self) -> None:
        if self._state == PetState.DEAD:
            self._is_sleeping = False
            return

        cfg = self._config
        if not self._is_sleeping and self.energy <= cfg.auto_sleep_energy_threshold:
            self._is_sleeping = True
            self._visual_action = None
            self._visual_action_ticks_remaining = 0

        if self._is_sleeping and self.energy >= cfg.auto_wake_energy_threshold:
            self._is_sleeping = False

    def _clamp_stats(self) -> None:
        min_s = self._config.min_stat
        max_s = self._config.max_stat

        self.hunger = max(min_s, min(max_s, self.hunger))
        self.happiness = max(min_s, min(max_s, self.happiness))
        self.energy = max(min_s, min(max_s, self.energy))

    def _update_state(self) -> None:
        cfg = self._config

        if (
            self.hunger >= cfg.death_hunger
            or self.energy <= cfg.death_energy
            or self.happiness <= cfg.death_happiness
        ):
            self._state = PetState.DEAD
            self._is_sleeping = False
            return

        if self.hunger >= cfg.hungry_threshold:
            self._state = PetState.HUNGRY
        elif self.energy <= cfg.tired_threshold:
            self._state = PetState.TIRED
        elif self.happiness <= cfg.bored_threshold:
            self._state = PetState.BORED
        else:
            self._state = PetState.ALIVE

    # ------------- Visual state + ASCII -------------

    def _check_evolution(self) -> None:
        if self._stage == "baby" and self.total_food_eaten >= self._config.food_to_adult:
            self._stage = "adult"


    def _visual_mode(self) -> str:
        """
        Decide which visual "mode" to show.
        """

        if self._state == PetState.DEAD:
            return "dead"
        if self._is_sleeping:
            return "sleep"
        if self._visual_action in ("eat", "play"):
            return self._visual_action

        # Fall back to need-based visuals
        if self._state == PetState.HUNGRY:
            return "hungry"
        if self._state == PetState.TIRED:
            return "tired"
        if self._state == PetState.BORED:
            return "bored"

        return "idle"

    def get_ascii_frame(self, frame_index: int = 0) -> str:
        """
        Return an ASCII frame for current species & visual mode.

        frame_index is used to cycle animation (UI calls with its own counter).
        """
        species_sprites = ASCII_SPRITES.get(self.species, ASCII_SPRITES["cat"])
        stage_key = getattr(self, "_stage", "baby")
        stage_sprites = (
            species_sprites.get(stage_key)
            or species_sprites.get("baby")
            or next(iter(species_sprites.values()))
        )
        mode = self._visual_mode()
        frames = stage_sprites.get(mode) or stage_sprites["idle"]
        idx = frame_index % len(frames)
        return frames[idx]

    # ------------- Persistence -------------

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "species": self.species,
            "stage": self._stage, 
            "hunger": self.hunger,
            "happiness": self.happiness,
            "energy": self.energy,
            "state": self._state.value,
            "is_sleeping": self._is_sleeping,
            "total_food_eaten": self.total_food_eaten,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any], config: PetConfig | None = None) -> "Pet":
        pet = cls(
            name=data["name"],
            species=data.get("species", "cat"),
            stage=data.get("stage", "baby"), 
            hunger=int(data.get("hunger", 20)),
            happiness=int(data.get("happiness", 70)),
            energy=int(data.get("energy", 70)),
            config=config,
        )
        pet._is_sleeping = bool(data.get("is_sleeping", False))
        pet.total_food_eaten = int(data.get("total_food_eaten", 0))
        pet._update_state()
        return pet
