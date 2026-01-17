# Developer Guide – Console Tamagotchi

## Code structure (overview)

The project follows a simple split between the **pet model** and the **UI**.
`pet.py` implements the `Pet` class with the finite state machine (ALIVE,
HUNGRY, TIRED, BORED, DEAD), stat updates, ASCII animation frames, and
serialization helpers. `main.py` contains the `TamagotchiApp` Tkinter GUI that
owns a single `Pet` instance, renders its state, and wires up the buttons and
keyboard shortcuts. The simulation is driven by Tkinter timers:
`game_tick()` calls `Pet.tick()` once per second, while `animation_tick()`
advances the ASCII animation frames.

Modules such as `actions.py`, `config.py`, `evolution.py`, `state_machine.py`,
`storage.py`, and `ui.py` come from the initial course template and are kept as
placeholders for future refactoring. In the current MVP, all core game logic is
implemented in `pet.py`, and the Tkinter GUI and event wiring live in `main.py`
for simplicity.

## Key APIs and comments

### `Pet.tick()`

`Pet.tick()` is the central per-frame update for the simulation. It delegates to
either `_apply_sleep_tick()` or `_apply_awake_tick()` depending on whether the
pet is currently sleeping, then applies cooldowns, auto sleep/wake rules, and
recomputes the derived `PetState`.

Internal design comment (why we route everything through one place):  
[see code](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/edit/main/src/console_tamagotchi/pet.py#L727)

### `Pet.feed()`

`Pet.feed()` is the public API for reducing hunger and slightly improving
happiness. Callers should treat the method as a side-effecting action that may
be ignored when the pet is dead, sleeping, or already full. It returns `True`
when the feed action was applied and `False` otherwise, so the UI can decide
whether to show a “no effect” message.

Docstring with usage details and return value:  
[see API doc](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/edit/main/src/console_tamagotchi/pet.py#L751)

---

## Running and extending the code

- The program entry point is `main()` in `main.py`, which creates and runs
  `TamagotchiApp`.
- To change balance or thresholds, edit `PetConfig` in `pet.py` – all states and
  death thresholds are derived from this configuration.
- New actions should go through the `Pet` class (e.g. `train()`, `heal()`) and
  be called from the GUI layer, keeping UI and game logic separate.
