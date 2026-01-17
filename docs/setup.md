# Installation Steps

Follow the instructions below to set up your development environment.

## 1. **Install Visual Studio Code (VSCode)**
- **Windows:**  
  Download VSCode from the [official website](https://code.visualstudio.com/Download) and follow the installation instructions.

- **Recommended Extensions:**  
  - **Python** extension for Python development.
  - **Git** extension for version control integration.

## 2. **Install Python (for Windows)**
- Download Python from the [official Python website](https://www.python.org/downloads/).
- Ensure that **Python** and **pip** are added to your system PATH during installation.

## 3. **Get the project code**

- Open a terminal (PowerShell / Command Prompt).
- Clone the repository:

  ```bash
  git clone <your GitLab repo URL>
  cd console-tamagotchi
  ```
- (Optional) Create and activate a virtual environment:
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
  ```
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Open the folder in VS Code and run the game with:
  ```bash
  python src/console_tamagotchi/main.py
  ```
