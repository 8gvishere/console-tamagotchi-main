# Tamagotchi Pet – User Guide

## Elevator Pitch

Tamagotchi Pet is a small desktop game where you take care of a virtual pet.
You can choose a cat, dog, or dragon, give it a name, and keep it alive by
feeding it, playing with it, and letting it sleep. The pet’s hunger, happiness,
and energy change over time. If you look after it well, it will grow from a baby
into an adult; if you ignore it, it may eventually die.

This guide explains how to start the game and how to use each feature step by step.

---

## Quick Start

### Requirements

- Python 3.10 or later
- Project files in one folder, including at least:
  - `main.py`
  - `pet.py`

### How to run the game

1. Open a terminal / command prompt in the project folder.
2. Run:

   ```bash
   python main.py
   ```
   If this does not work, try:
   ```bash
   python3 main.py
   ```
3. A window titled “Tamagotchi” will appear.

# Features Overview

This version includes the following features:

1. [Create & name your Tamagotchi](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/13)
2. [Feed your Tamagotchi (Hunger System)](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/14)
3. [Play with your Tamagotchi (Happiness System)](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/15)
4. [Sleep & energy cycle](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/16)
5. [Show pet status (UI panel)](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/17)
6. [Evolution & growth](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/18)

---

# Feature 1: Create & Name Your Tamagotchi

## What it does

Creates a new pet with a chosen name and species (Cat, Dog, or Dragon) and initialises its starting stats: Hunger, Happiness, and Energy.

## How to use

1. Run the game. A small dialog window appears.
2. In the **Name** field, type any name you like.
   - If you leave it empty, a default name (e.g. *Tama*) is used.
3. Select a **Species** by clicking Cat, Dog, or Dragon.
4. Click **OK** or press **Enter**.

## Expected result

- The main window opens.
- Your pet appears on screen with an ASCII picture.
- The name and species are shown in the info area.
- Hunger, Happiness, and Energy are set to their default starting values.

---

# Feature 2: Feed Your Tamagotchi (Hunger System)

## What it does

Feeding reduces how hungry your pet is and slightly improves its happiness.  
The hunger stat also naturally increases over time as the pet gets hungry.

## How to use

1. Make sure your pet is alive and awake.
2. When the **Hunger** bar becomes low, click the **Feed** button or press the **F** key.
3. Repeat when the pet is hungry again.

## Expected result

- The **Hunger** bar increases (more green = less hungry).
- The pet plays a short “eating” animation.
- A message appears at the bottom, e.g. *“You feed your pet. Crunch crunch.”*
- If hunger is already very low, the game shows a message that feeding has no effect.
- If you never feed the pet, hunger can reach a deadly level and the pet may die.

---

# Feature 3: Play with Your Tamagotchi (Happiness System)

## What it does

Playing makes your pet happier but consumes some energy.  
Happiness also slowly decreases over time if you do nothing.

## How to use

1. Ensure your pet has enough **Energy** (the Energy bar is not empty).
2. Click **Play** or press **P**.
3. Wait a short moment before playing again — there is a small cooldown.

## Expected result

- The **Happiness** bar increases.
- The **Energy** bar decreases slightly.
- The pet’s ASCII expression changes to look more excited or playful.
- A message appears, e.g. *“You play with your pet. It looks happier!”*
- If you spam the action, a cooldown message tells you that playing has no effect for now.

---

# Feature 4: Sleep & Energy Cycle

## What it does

Sleep restores the pet’s energy while temporarily disabling other actions.  
Energy slowly goes down during normal activity; when it is very low, the pet may fall asleep automatically.

## How to use

1. When the **Energy** bar is low, click **Sleep** or press **S**.
2. The pet lies down and starts sleeping.
3. Wait while the pet recovers energy.
4. Click **Wake** or press **W** to wake it up.

## Expected result

- During sleep:
  - **Energy** increases quickly.
  - **Hunger** slowly increases (the pet gets hungry while sleeping).
  - **Feed** and **Play** buttons are disabled.
- The info label shows that the pet is sleeping.
- When you wake the pet (or it wakes automatically after enough rest), normal actions become available again.

---

# Feature 5: Show Pet Status (UI Panel)

## What it does

The UI panel shows the pet’s current name, species, high-level state and its three main stats: Hunger, Happiness, and Energy.

## How to use

Simply watch the right side of the main window while playing:

- **Name** — the name you chose.
- **Species** — Cat, Dog, or Dragon.
- **State** — overall condition such as `ALIVE`, `HUNGRY`, `TIRED`, `BORED`, or `DEAD`.
- **Bars** — three horizontal bars for Hunger, Happiness, and Energy.

## Expected result

- Values update automatically every tick and immediately after each action.
- When a value becomes dangerously low, the state label changes (e.g. `HUNGRY`).
- If a stat reaches a deadly threshold, the state changes to `DEAD` and actions are disabled.

---

# Feature 6: Evolution & Growth

## What it does

If you keep feeding your pet and it eats enough total food, it grows from a baby into an adult form.

## How to use

1. Take good care of your pet:
   - Feed it regularly so hunger stays under control.
   - Avoid letting it die.
2. Over time, as the pet eats, an internal counter tracks how much food it has eaten.
3. Once it reaches the evolution threshold, the pet automatically evolves.

## Expected result

- The pet’s stage changes from baby to adult.
- The ASCII art becomes larger and more detailed.
- A message line confirms that your pet has evolved.

---

# Troubleshooting

## The window does not open

- Check that you are running the command in the correct folder.
- Try `python3 main.py` if `python main.py` does not work.
- Make sure Python 3 is installed on your system.

## Buttons are greyed out

- If the pet is sleeping, only **Wake** and **Quit** are available.
- If the pet is dead, all actions except **Quit** are disabled.

## The pet dies quickly

- Feed it more often when the **Hunger** bar is low.
- Let it sleep when **Energy** is low.
- Use **Play** to keep **Happiness** from dropping to zero.

---

# Glossary

- **Hunger** — how hungry the pet is. More green = less hungry (better).
- **Happiness** — how happy the pet feels. More green = happier.
- **Energy** — how rested the pet is. More green = more energy.
- **State** — overall condition, e.g. `ALIVE`, `HUNGRY`, `TIRED`, `BORED`, `DEAD`.
- **Stage** — growth stage, currently **Baby** or **Adult**.
- **Cooldown** — short delay after playing where repeating the action has no effect.
