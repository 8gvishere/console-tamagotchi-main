# console-tamagotchi

## Why This Project (Motivation & Value)

Console Tamagotchi is not just a small command-line game — it’s an **educational simulation** designed to teach beginners how to think like software engineers.  
It demonstrates **modular software design**, **finite state machines**, and **data persistence** in a lightweight, beginner-friendly environment.  
Beyond the course itself, it can serve as a **template project for programming workshops, tutorials, or AI/game logic experiments**.

The project aims to show how logic, storage, and user interaction layers can work together in a clean and maintainable structure.

### Who is it for?
- **Students and self-learners** who want to practice object-oriented programming, persistence, and command-line interfaces through an engaging project.  
- **Instructors and mentors** who can use it as a teaching example to demonstrate clean modular design and simple game architecture.

### What value does it bring?
- **Practical learning:** Implements OOP concepts, a finite state machine (`ALIVE`, `HUNGRY`, `TIRED`, `BORED`, `DEAD`), and JSON-based data persistence.  
- **Engineering discipline:** Encourages modular structure, testable components, and a clean CLI design following issue-driven development.  
- **Lightweight & accessible:** Runs anywhere with Python 3.10+, requires no external libraries or setup.  
- **Extendable:** Easily allows new rules, interactions, or narrative elements to be added without breaking the core design.

### Why would someone use this?
Console Tamagotchi offers an engaging and hands-on way to **practice Python programming**,  
**object-oriented design**, and **state management** through an interactive learning experience.  
It’s ideal for students, teachers, and developers who want to explore how small systems mimic real-world software behavior.


## Elevator Pitch
A simple command-line virtual pet with three core attributes: **hunger**, **happiness**, and **energy**.  
Players interact via `feed`, `play`, `rest`, `status`, `help`, and `quit` to keep the pet alive and happy.

## Project Diagram

We designed the following **Teamwork Rules diagram** to visualize how our team collaborates during the Console Tamagotchi project.  
It summarizes our communication channels, meeting routines, decision-making process, and conflict resolution strategies.

[View the Excalidraw Diagram](https://excalidraw.com/#json=G9JCwgg2Nd4KHXFo3g4E1,lXfI2NpdiNnBLYfKCQp4kw)
[See full Teamwork Rules](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/blob/main/TEAM_RULES.md)


## Goals
- Implement a game loop with time progression.
- Update and display pet attributes.
- Implement core commands: `feed`, `play`, `rest`, `status`, `help`, `quit`.
- Keep the code clean, readable, and include basic unit tests.

## Non-goals
- No graphical interface (CLI only) in v1.  
- No online database; all data is stored locally in memory or JSON files.

## How to Run
- Requirements: **Python 3.10+**

<details>
  <summary><h2>Project Structure</h2></summary>

```text
console-tamagotchi/
│
├─ src/                                  # all source code lives here (stable imports)
│  └─ console_tamagotchi/                # project package
│     ├─ __init__.py                     # marks this as a Python package
│     ├─ main.py                         # app entrypoint & CLI routing (Yin)
│     ├─ ui.py                           # terminal UI: render status, prompts (Yin)
│     ├─ pet.py                          # core Pet model & tick() loop (Batsaikhan)
│     ├─ actions.py                      # actions: feed/play/sleep (Batsaikhan)
│     ├─ state_machine.py                # optional: Awake/Sleep/GameOver (Batsaikhan)
│     ├─ evolution.py                    # evolution/growth logic (Batsaikhan)
│     ├─ storage.py                      # save/load to JSON (Faraz)
│     ├─ config.py                       # tuning constants & thresholds (shared)
│     └─ types.py                        # optional: dataclasses / type hints (shared)
│
├─ tests/                                 # unit tests (Faraz)
│  ├─ test_pet.py
│  ├─ test_actions.py
│  ├─ test_storage.py
│  └─ __init__.py
│
├─ assets/                                # ASCII art, screenshots, demo GIFs (optional)
│  └─ ascii_samples.txt
│
├─ saves/                                 # runtime save files (ignored by Git)
│  └─ sample_save.json                    # example only
│
├─ .vscode/                               # VS Code project settings (optional but handy)
│  ├─ settings.json                       # interpreter, pytest, formatting
│  └─ launch.json                         # F5 to run module / tests
│
├─ README.md                              # main documentation (how to run, structure, roles)
├─ requirements.txt                       # dependencies (can be minimal; stdlib mostly)
└─ .gitignore                             # ignore caches, venv, saves, etc.

```
### Why this structure?

We organized the project into separate folders for source code, tests, and documentation.
This makes the project easy to navigate and lets each member focus on their own parts.

### Future Structure Plan
> The structure will stay simple for the CLI version.  
> Future updates may only add more test files or internal modules (e.g., for animations or saving features).

</details> 


<details>
  <summary><h2> Team Responsibilities</h2></summary>

| Member | Role | Responsibilities | Deliverables |
|---------|------|------------------|---------------|
| **Batsaikhan Buyan-Erdene** | Logic & State Machine Lead | Design and implement the `Pet` class, finite state machine (`ALIVE`, `HUNGRY`, `TIRED`, `BORED`, `DEAD`), and balance logic. | `pet.py`, unit tests → [Issue #2: Logic & FSM](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/2) |
| **Yin Zirui** | CLI & User Experience Lead | Develop and manage the main command-line interface, handle user input/output, ASCII UI design, and feedback messages. | `main.py`, UI guideline → [Issue #1: CLI & UX](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/1) |
| **Syed Hassan Faraz** | Extensions & QA Lead | Extend the project with save/load and narrative features, perform testing, and maintain project documentation. | `storage.py`, `narrative.py`, `tests/`, `README.md` → [Issue #3: Extensions & QA](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/3) |

>  *For details on our communication and teamwork methods, see* [TEAM_RULES.md](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/blob/main/TEAM_RULES.md)


| Member | Role | Responsibilities | Use-Case |
|---|---|---|---|
| **Batsaikhan Buyan-Erdene** | Core Logic & Simulation Lead | Implements the pet’s core logic, including actions (play / sleep), state machine, and timing loop. Handles emotion and energy updates, and ensures balanced gameplay. Works closely with the UI Lead to connect logic APIs. | [**Use-Case 3** – Play with Your Tamagotchi (Happiness System)](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/15)<br>[**Use-Case 4** – Sleep & Energy Cycle](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/16) |
| **Yin Zirui** | Feature & Interface Lead | Designs and implements the command-line interface (CLI) and user interactions. Handles naming/creation, feeding, showing pet status, and evolution logic. Responsible for UI rendering, routing commands, and ensuring accessibility and usability. | [**Use-Case 1** – Create & Name Your Tamagotchi](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/13)<br>[**Use-Case 2** – Feed Your Tamagotchi (Hunger System)](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/14)<br>[**Use-Case 5** – Show Pet Status (UI Panel)](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/17)<br>[**Use-Case 6** – Evolution & Growth](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/18) |
| **Syed Hassan Faraz** | QA, Persistence & Documentation Lead | Implements save/load (JSON) system, manages testing (unit + integration), and maintains documentation (README + Wiki). Ensures data persistence and verifies the correctness of all six features through testing. | Supports [**Use-Case 1–6**] (testing, save/load, docs) |

</details>

<details>
  <summary><h2>Technical Stack</h2></summary> 

- **Language:** Python 3.10+
- **Environment:** Command-line interface (CLI)
- **Dependencies:** None (standard library only)
- **Data Format:** JSON for save/load
- **Testing Framework:** `unittest`

The project is designed to run cross-platform (Windows, macOS, Linux) and requires no external packages.

</details>

<details>
  <summary><h2> Planned Features & Requirements Summary</h2></summary>   

The first version (v1.0) will focus on core gameplay:
feeding, resting, playing, and tracking the pet’s status.

| No. | Feature | Description | Issue Link |
|-----|----------|--------------|-------------|
| 1 | **Feed the Pet** | Allows the player to feed the pet and restore its hunger level. Includes edge case handling when the pet is already full. | [Feed the Pet](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/4) |
| 2 | **Play with the Pet** | Lets the player play games to increase happiness while consuming energy. Prevents overplaying. | [Play with the Pet](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/5) |
| 3 | **Rest Command** | Allows the pet to rest, restoring energy and reducing hunger over time. | [Rest Command](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/6) |
| 4 | **Check Status** | Displays the pet’s current stats (hunger, happiness, energy) in a clean CLI format. | [Check Status](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/7) |
| 5 | **Save & Load Progress** | Saves and loads the pet’s data via JSON files, ensuring game persistence between sessions. | [Save & Load Progress](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/8) |
| 6 | **Help & Quit Commands** | Displays a list of commands and enables players to safely exit the game with confirmation and farewell message. | [Help & Quit Commands](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/9) |

### Notes
- Each feature corresponds to a requirement issue documented in detail (with goal, usage example, and done criteria).  
- All features align with the **MVP goals** defined in the project instructions.  
- Version 1.0 focuses on CLI-only functionality with local JSON-based storage.  

</details>

<details>
  <summary><h2> Role–Feature Mapping</h2></summary>  

| Member / Role | Main Module | Related Issues | Responsibility |
|----------------|--------------|----------------|----------------|
| **Yin Zirui (CLI & UX Lead)** | `main.py` | #4 Feed · #5 Play · #7 Status · #9 Help/Quit | Implements CLI commands, user input/output, and feedback messages. |
| **Buyqka (Logic & State Machine Lead)** | `pet.py` | #4 Feed · #5 Play · #6 Rest · #7 Status | Implements internal pet logic (state machine, value changes, and rules). |
| **Hassan (Extensions & QA Lead)** | `storage.py`, `narrative.py`, `tests/` | #8 Save & Load | Implements save/load features, testing, and project documentation. |

>  Shared Features (#4, #5, #7) are **jointly developed** by Yin (CLI layer) and Buyqka (logic layer).

### Dependencies & Collaboration Notes
- **Feed, Play, and Status (#4, #5, #7)** depend on interactions between `main.py` (command interface) and `pet.py` (state logic).  
  Yin and Buyqka collaborated to integrate input handling and logic updates.  
- **Save & Load (#8)** relies on both the pet’s state structure (`pet.py`) and CLI messages (`main.py`) to ensure smooth file persistence and user feedback.  
- All team members reviewed and tested features to ensure consistent gameplay experience.

</details>

<details>
  <summary><h2> Use-Case Notes</h2></summary>   

These notes summarize insights from our simulated domain expert interviews for the core gameplay features of **Console Tamagotchi**.  
The goal is to identify key actors, user goals, contexts, missing scenarios, and potential ambiguities for the upcoming use-case modeling phase.

---

Actors

- **Player** — Interacts with the pet through CLI commands (feed, play, rest, check, save/load, help, quit).  
- **Pet (System)** — Reacts to player actions and automatically updates hunger, happiness, and energy levels.  
- **File System** — Stores and retrieves saved pet data (JSON-based persistence).

---

Goals

- Keep the pet alive, happy, and healthy by managing hunger, happiness, and energy.  
- Observe the pet’s condition to decide which action (feed, play, rest) to take.  
- Save and load game progress to continue caring for the pet across sessions.  
- Receive clear feedback and guidance while using text-based commands.

---

Contexts & Pain Points

- **Hunger Loop:** If the pet is not fed, hunger increases until it may “die.” Feeding too often should be prevented.  
- **Play Loop:** Playing boosts happiness but costs energy; overplaying should have limits.  
- **Rest Loop:** Resting restores energy but can increase hunger slightly.  
- **Feedback:** Players need confirmation after every command to know their action worked.  
- **Information:** Without the “check” command, players may not know what the pet needs.  
- **Persistence:** If saving fails, player progress could be lost between sessions.  
- **Usability:** Players might enter wrong commands; the system must handle these gracefully.

---

Missing Scenarios

- What happens when the player enters an invalid command?  
- Should there be any automatic time-based events (e.g., pet gets hungry over time)?  
- What happens if the player ignores the pet for a long time (death, reset, warning)?  
- Can the player accidentally delete or overwrite saved data?  
- Should multiple actions be allowed quickly in sequence, or should there be time delays?

---

Ambiguities & Inconsistencies

- Does resting always increase happiness, or only when energy is low?  
- Should playing reduce both hunger and energy, or only energy?  
- How frequently should time progression and automatic updates occur?  
- When feeding, does happiness increase slightly, or only hunger decrease?  
- Should quitting trigger autosave automatically or require confirmation each time?  
- Is the “check status” command passive or does it affect gameplay time progression?

---

Summary

The primary gameplay loop (**Feed → Play → Rest → Check → Repeat**) defines the **core user interaction**.  
Supporting features like **Save/Load**, **Help**, and **Quit** enhance persistence and usability.  
These notes clarify user goals, system behaviors, and open questions to be refined into detailed use cases in the next milestone.

</details>


<details>
  <summary><h2>Cost Estimation</h2></summary>

### MoSCoW Prioritization  

| Category | Features |
|-----------|-----------|
| **Must Have** | Feed Your Tamagotchi (Hunger System), Play with Your Tamagotchi (Happiness System) |
| **Should Have** | Create & Name Your Tamagotchi, Sleep & Energy Cycle |
| **Could Have** | Show Pet Status (UI Panel), Evolution & Growth |

*Must-haves are essential for the MVP (Minimum Viable Product).*

---

### Cost, Value & Bang Estimation  

> **Note on Story vs. Value Points**  
> In our project, **Story Points** represent the estimated development effort (from our team’s GitLab issues),  
> while **Value Points** reflect the tutor’s evaluation of each feature’s impact or importance.  
> “**Bang for the Buck**” measures the ratio **Value ÷ Story Points**, showing how much value each feature provides per unit of effort.

---

> **How we estimated Story Points:**  
> We used the **Fibonacci scale** (1, 2, 3, 5, 8, 13) to represent increasing effort and technical complexity.  
> Story Points measure **relative difficulty**, not development time.  
> Each value was discussed collaboratively by our team during sprint planning.

> **Feature breakdown:**  
> - **Show Pet Status (3 pts)** – Simple UI logic; low effort, only updates real-time values.  
> - **Create & Name (5 pts)** – Moderate complexity; requires input validation and initialization logic.  
> - **Sleep & Energy Cycle (5 pts)** – Time-based loops and event triggers; simple but needs consistent updates.  
> - **Play with Tamagotchi (8 pts)** – Medium-to-high effort; adds animations, user interaction, and state feedback.  
> - **Evolution & Growth (8 pts)** – Complex conditional logic; multi-stage transitions and progress saving.  
> - **Feed (13 pts)** – High complexity; affects multiple systems (hunger, happiness, UI feedback).

---

| Feature (Use Case) | Value (Points) | Cost (Story Points) | Bang for the Buck = Value ÷ Cost | Priority |
|----------------------|----------------|---------------------|--------------------|-----------|
| [Show Pet Status (UI Panel)](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/17) | 20 | 3 | **6.67** | 🥇 1 |
| [Create & Name Your Tamagotchi](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/13) | 20 | 5 | **4.00** | 🥈 2 |
| [Evolution & Growth](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/18) | 30 | 8 | **3.75** | 🥉 3 |
| [Play with Your Tamagotchi (Happiness System)](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/15) | 25 | 8 | **3.13** | 4 |
| [Sleep & Energy Cycle](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/16) | 10 | 5 | **2.00** | 5 |
| [Feed Your Tamagotchi (Hunger System)](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/issues/14) | 15 | 13 | **1.15** | 6 |


> **Bang for the Buck Formula:**
> ```
> Bang for the Buck = Value Points / Story Points
> ```
> The higher the ratio, the more efficient the feature is to implement.  
> This helps the team prioritize features that offer the greatest user impact for the least development effort.

---

### Feature Prioritization  

We prioritized the six core features based on a combination of **MoSCoW categories**,  
**Bang for the Buck ratios**, and **practical development feasibility**.

| **Priority** | **Feature** | **Rationale** |
|---------------|-------------|----------------|
| 🥇 1 | **Show Pet Status (UI Panel)** | Delivers strong visibility and real-time feedback to players; highly efficient to implement with large user impact. |
| 🥈 2 | **Create & Name Your Tamagotchi** | Forms the foundation of the player’s ownership and personalization experience; simple but valuable. |
| 🥉 3 | **Evolution & Growth** | Expands replayability and progression; adds long-term engagement goals once the core loop is complete. |
| 4 | **Play with Your Tamagotchi (Happiness System)** | Adds fun and emotional depth to gameplay; strengthens player-pet connection. |
| 5 | **Sleep & Energy Cycle** | Introduces pacing and realism; balances activity with rest to simulate daily rhythm. |
| 6 | **Feed Your Tamagotchi (Hunger System)** | Fundamental survival mechanic but offers lower value-to-effort ratio due to complexity and dependencies. |

> These priorities were determined collaboratively during our team discussion,  
> considering **gameplay impact**, **user experience value**, and **overall feature complexity**.

---

### Summary  

Overall, our estimation results show a clear trade-off between **development effort** and **gameplay value**.  
This cost estimation helped our team balance **effort**, **impact**, and **feasibility**,  
allowing us to identify which features deliver the most meaningful impact for the **Minimum Viable Product (MVP)**.

By combining **MoSCoW prioritization** with **Bang-for-the-Buck analysis**,  
we focused our development plan on features that are both **valuable** and **achievable** within limited time.

This approach also improved our **team coordination** and **communication efficiency** during sprint planning,  
ensuring that all members understood the relationship between implementation complexity and gameplay impact.

Our MVP centers on the **core gameplay loop** — *creating, feeding, playing, and interacting with the Tamagotchi* —  
while leaving room for future improvements such as **evolution** and **visual UI enhancement**  
once the foundational systems are stable.
</details>

<details>
  <summary><h2>Project Management</h2></summary>

### Issue Workflow
Our team manages all tasks through the GitLab **Issue Board**.

We use four columns to track progress:
**To Do → In Progress → Review → Done**

Each issue corresponds to a use case or feature (1–6).  
Team members move issues between columns as progress changes.

View our live board here: [Issue Board](https://git-okt.sed.inf.szte.hu/project-work/one/2025/123/console-tamagotchi/-/boards/3333)

### Issue Movement Responsibility

Each team member is responsible for updating the status of their own assigned issues.

- **Developers (Yin & Batsaikhan)** move issues from **To Do → In Progress** when they start working on a feature.
- After finishing implementation, they move it to **Review** and tag **Faraz** for testing or documentation check.
- Once testing and verification are done, **Faraz** moves the issue to **Done**.
- If any bug or rework is required, the issue is moved back to **In Progress**.

This ensures that the board always reflects the current state of the project.

## Project Workflow

Our team follows a clear workflow to ensure quality and consistency.  
The following checklist defines when a task or feature is considered complete.

### Definition of Done (DoD)

The following checklist defines when a task or feature is considered Done in our team workflow:

>Code has been implemented according to the issue description.

>Code has been reviewed by at least one other team member.

>All related tests have passed successfully.

>No major bugs remain after testing.

>Documentation (README or Wiki) has been updated if needed.

>The changes have been merged into the main branch.

>The corresponding issue has been moved to the “Done” column on the Issue Board.

### Issue Label Conventions

To keep our Issue Board organized and easy to understand, our team uses the following labels:

**Work Status Labels (for workflow tracking):**
- **to do** — task not started yet  
- **in progress** — task currently being worked on  
- **review** — task completed, waiting for review or testing  
- **done** — task reviewed and finalized  

**Task Type Labels (for categorization):**
- **feature** — for implementing new functionality or user stories  
- **requirement** — for describing key requirements or system components  
- **bug** — for tracking and fixing program errors  
- **refactor** — for improving or restructuring existing code  

These labels help the team clearly track task progress and maintain consistency across the Issue Board.

### Git & Issue Integration

We use GitLab’s automatic issue-closing keywords to link commits with issues.  
When developers include a message like `Fixes #14` in their commit, GitLab automatically links the commit to that issue and closes it once merged.

Example:
git commit -m "Implement feeding logic (Fixes #14)"

This ensures every code change is directly connected to the task it solves and helps keep our Issue Board updated automatically.

</details>

I wish future developers feel confident and comfortable understanding and improving our code.

## Getting Started

To set up the environment and install dependencies, see:

- [Environment setup](docs/environment.md)
- [Project setup](docs/setup.md)

## Documentation

- **User Guide** – how to run the app and use all features  
  → [docs/user/index.md](docs/user/index.md)

- **Developer Guide** – code structure and API notes  
  → [docs/dev/index.md](docs/dev/index.md)

## Demo

We provide two short demo videos for the tutor:

1. **Demo 1 – Create & Name Your Tamagotchi (Use-Case 1)**  
   Starts the program from the terminal, creates and names a new pet, and shows the main game screen.  
   YouTube: [https://youtu.be/s4TvIbWxW-U](https://youtu.be/s4TvIbWxW-U)

2. **Demo 2 – Core Gameplay & Additional Feature (Use-Cases 2–6 + priced feature)**  
   Continues with the same pet and demonstrates feeding, playing, sleeping/energy, the status panel, evolution,
   and our additional priced feature.  
   YouTube: [https://youtu.be/_6C0U5qKkXI](https://youtu.be/_6C0U5qKkXI)
