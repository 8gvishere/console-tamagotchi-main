# main entry for Console Tamagotchi
"""
GUI Tamagotchi using tkinter.

Author: Buyan-Erdene Batsaikhan
"""

import tkinter as tk
from tkinter import ttk

from pet import Pet, PetState  # pet.py is in the same folder

TICK_INTERVAL_MS = 1000       # logic tick: 1s
ANIM_INTERVAL_MS = 333        # ~3 FPS animation
BAR_WIDTH = 220
BAR_HEIGHT = 16


class TamagotchiApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Tamagotchi")
        self.resizable(False, False)

        # Create once so dialogs can use it
        self.style = ttk.Style(self)
        self.style.theme_use("clam")

        name, species = self.ask_name_and_species()
        self.pet = Pet(name=name, species=species)

        self.tick_count = 0
        self.anim_frame = 0
        self.feedback_text = tk.StringVar(value="Your new pet has hatched!")

        self._build_ui()
        self._update_ui()

        self.update_idletasks()
        self.minsize(self.winfo_reqwidth(), self.winfo_reqheight())

        # Keyboard bindings
        self.bind_all("<Key>", self.on_key)

        # Start loops
        self.after(TICK_INTERVAL_MS, self.game_tick)
        self.after(ANIM_INTERVAL_MS, self.animation_tick)

    # ------------- Pet selection dialog -------------

    def ask_name_and_species(self) -> tuple[str, str]:
        container = ttk.Frame(self, padding=20)
        container.grid(row=0, column=0, sticky="nsew")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        name_var = tk.StringVar(value="Tama")
        species_var = tk.StringVar(value="cat")
        done = tk.BooleanVar(value=False)

        ttk.Label(container, text="Pet name:").grid(
            row=0, column=0, padx=10, pady=(10, 4), sticky="w"
        )
        entry = ttk.Entry(container, textvariable=name_var, width=20)
        entry.grid(row=1, column=0, padx=10, pady=(0, 8), sticky="w")

        ttk.Label(container, text="Choose your pet:").grid(
            row=2, column=0, padx=10, pady=(4, 2), sticky="w"
        )

        species_frame = ttk.Frame(container)
        species_frame.grid(row=3, column=0, padx=10, pady=(0, 8), sticky="w")

        ttk.Radiobutton(
            species_frame, text="Cat", value="cat", variable=species_var
        ).grid(row=0, column=0, sticky="w")
        ttk.Radiobutton(
            species_frame, text="Dog", value="dog", variable=species_var
        ).grid(row=0, column=1, sticky="w", padx=(8, 0))
        ttk.Radiobutton(
            species_frame, text="Dragon", value="dragon", variable=species_var
        ).grid(row=0, column=2, sticky="w", padx=(8, 0))

        result_name = "Tama"
        result_species = "cat"

        def confirm(event=None) -> None:
            nonlocal result_name, result_species
            n = name_var.get().strip() or "Tama"
            result_name = n
            result_species = species_var.get()
            done.set(True)

        ttk.Button(container, text="OK", command=confirm).grid(
            row=4, column=0, padx=10, pady=(0, 10), sticky="e"
        )

        entry.bind("<Return>", confirm)

        self.update_idletasks()
        width = self.winfo_width() or 320
        height = self.winfo_height() or 160
        x = self.winfo_screenwidth() // 2 - width // 2
        y = self.winfo_screenheight() // 2 - height // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

        entry.focus_set()

        self.wait_variable(done)

        container.destroy()

        return result_name, result_species


    # ------------- UI construction -------------

    def _build_ui(self) -> None:
        top_frame = ttk.Frame(self, padding=10)
        top_frame.grid(row=0, column=0, sticky="nsew")

        self.art_label = tk.Label(
            top_frame,
            font=("Consolas", 11),
            justify="left"
        )
        self.art_label.grid(row=0, column=0, rowspan=3, padx=(0, 15))

        info_frame = ttk.Frame(top_frame)
        info_frame.grid(row=0, column=1, sticky="nw")

        self.name_label = ttk.Label(info_frame, text=f"Name: {self.pet.name}", font=("Segoe UI", 12, "bold"))
        self.name_label.grid(row=0, column=0, sticky="w")

        self.state_label = ttk.Label(info_frame, text="", font=("Segoe UI", 10))
        self.state_label.grid(row=1, column=0, sticky="w", pady=(4, 0))

        self.species_label = ttk.Label(info_frame, text=f"Species: {self.pet.species.capitalize()}", font=("Segoe UI", 10))
        self.species_label.grid(row=2, column=0, sticky="w", pady=(2, 0))

        bars_frame = ttk.Frame(self, padding=(10, 0, 10, 10))
        bars_frame.grid(row=1, column=0, sticky="nsew")

        ttk.Label(bars_frame, text="Hunger").grid(row=0, column=0, sticky="w")
        self.hunger_canvas = tk.Canvas(bars_frame, width=BAR_WIDTH, height=BAR_HEIGHT, highlightthickness=0)
        self.hunger_canvas.grid(row=0, column=1, padx=(8, 0), pady=2)

        ttk.Label(bars_frame, text="Happiness").grid(row=1, column=0, sticky="w")
        self.happiness_canvas = tk.Canvas(bars_frame, width=BAR_WIDTH, height=BAR_HEIGHT, highlightthickness=0)
        self.happiness_canvas.grid(row=1, column=1, padx=(8, 0), pady=2)

        ttk.Label(bars_frame, text="Energy").grid(row=2, column=0, sticky="w")
        self.energy_canvas = tk.Canvas(bars_frame, width=BAR_WIDTH, height=BAR_HEIGHT, highlightthickness=0)
        self.energy_canvas.grid(row=2, column=1, padx=(8, 0), pady=2)

        feedback_label = ttk.Label(self, textvariable=self.feedback_text, foreground="#555555", padding=(10, 4))
        feedback_label.grid(row=2, column=0, sticky="w")

        buttons_frame = ttk.Frame(self, padding=(10, 5, 10, 10))
        buttons_frame.grid(row=3, column=0, sticky="ew")

        self.feed_button = ttk.Button(buttons_frame, text="Feed [F]", command=self.on_feed)
        self.feed_button.grid(row=0, column=0, padx=3)

        self.play_button = ttk.Button(buttons_frame, text="Play [P]", command=self.on_play)
        self.play_button.grid(row=0, column=1, padx=3)

        self.sleep_button = ttk.Button(buttons_frame, text="Sleep [S]", command=self.on_sleep)
        self.sleep_button.grid(row=0, column=2, padx=3)

        self.wake_button = ttk.Button(buttons_frame, text="Wake [W]", command=self.on_wake)
        self.wake_button.grid(row=0, column=3, padx=3)

        self.quit_button = ttk.Button(buttons_frame, text="Quit [Q]", command=self.on_quit)
        self.quit_button.grid(row=0, column=4, padx=3)

    # ------------- Drawing helpers -------------

    def draw_bar(self, canvas: tk.Canvas, value: int, max_value: int = 100, invert: bool = False) -> None:
        canvas.delete("all")
        value = max(0, min(max_value, value))
        if invert:
            value = max_value - value

        ratio = value / max_value if max_value > 0 else 0
        fill_width = int(BAR_WIDTH * ratio)

        canvas.create_rectangle(0, 0, BAR_WIDTH, BAR_HEIGHT, outline="#666666", width=1)
        if fill_width > 0:
            canvas.create_rectangle(0, 0, fill_width, BAR_HEIGHT, outline="", fill="#4caf50")

    def _update_art(self) -> None:
        art = self.pet.get_ascii_frame(self.anim_frame)
        self.art_label.config(text=art)

    def _update_ui(self) -> None:
        self._update_art()

        state_text = self.pet.state.value.upper()
        if self.pet.is_sleeping and self.pet.state != PetState.DEAD:
            state_text += " (SLEEPING)"
        self.state_label.config(text=f"State: {state_text}")

        self.draw_bar(self.hunger_canvas, self.pet.hunger, invert=True)
        self.draw_bar(self.happiness_canvas, self.pet.happiness, invert=False)
        self.draw_bar(self.energy_canvas, self.pet.energy, invert=False)

        if self.pet.state == PetState.DEAD:
            self.feed_button.state(["disabled"])
            self.play_button.state(["disabled"])
            self.sleep_button.state(["disabled"])
            self.wake_button.state(["disabled"])
            self.feedback_text.set("Your pet has died. Press [Q] to quit.")
        else:
            if self.pet.is_sleeping:
                self.feed_button.state(["disabled"])
                self.play_button.state(["disabled"])
                self.sleep_button.state(["disabled"])
                self.wake_button.state(["!disabled"])
            else:
                self.feed_button.state(["!disabled"])
                self.play_button.state(["!disabled"])
                self.sleep_button.state(["!disabled"])
                self.wake_button.state(["disabled"])

    # ------------- Button callbacks -------------

    def on_feed(self) -> None:
        if self.pet.state == PetState.DEAD:
            return
        if self.pet.feed():
            self.feedback_text.set("You feed your pet. Crunch crunch.")
        else:
            self.feedback_text.set("Feeding had no effect.")
        self._update_ui()

    def on_play(self) -> None:
        if self.pet.state == PetState.DEAD:
            return
        if self.pet.play():
            self.feedback_text.set("You play with your pet. It looks happier!")
        else:
            self.feedback_text.set("Your pet is too tired or on cooldown.")
        self._update_ui()

    def on_sleep(self) -> None:
        if self.pet.state == PetState.DEAD:
            return
        if self.pet.sleep():
            self.feedback_text.set("Your pet curls up and falls asleep.")
        else:
            self.feedback_text.set("Your pet cannot sleep right now.")
        self._update_ui()

    def on_wake(self) -> None:
        if self.pet.state == PetState.DEAD:
            return
        if self.pet.wake():
            self.feedback_text.set("You gently wake your pet.")
        else:
            self.feedback_text.set("Your pet refuses to wake.")
        self._update_ui()

    def on_quit(self) -> None:
        self.destroy()

    # ------------- Keyboard -------------

    def on_key(self, event: tk.Event) -> None:
        key = event.keysym.lower()

        if key == "q":
            self.on_quit()
        elif self.pet.state == PetState.DEAD:
            return
        elif key == "f":
            self.on_feed()
        elif key == "p":
            self.on_play()
        elif key == "s":
            self.on_sleep()
        elif key == "w":
            self.on_wake()

    # ------------- Loops -------------

    def game_tick(self) -> None:
        if not self.winfo_exists():
            return

        if self.pet.state != PetState.DEAD:
            self.pet.tick()
            self.tick_count += 1
            self._update_ui()

        self.after(TICK_INTERVAL_MS, self.game_tick)

    def animation_tick(self) -> None:
        if not self.winfo_exists():
            return
        self.anim_frame += 1
        self._update_art()
        self.after(ANIM_INTERVAL_MS, self.animation_tick)


def main() -> None:
    app = TamagotchiApp()
    app.mainloop()


if __name__ == "__main__":
    main()
