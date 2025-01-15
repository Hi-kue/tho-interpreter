# THO INTERPRETER CHALLENGE

## Overview
The **Tho Interpreter Challenge** is an exciting task to develop a Python program that acts as an interpreter for the **Tho Programming Language**. This minimalistic scripting language focuses on performing arithmetic operations on floating-point numbers using a single register `R`.

---

## Key Features
- Simple command-based syntax to perform basic arithmetic operations.
- Interactive commands for user input and output.
- Supports operations such as addition, subtraction, multiplication, and division.
- Minimalistic design to encourage learning and experimentation.

---

## How It Works
The Tho interpreter processes commands line by line from a script file. Each command manipulates the value in the single register `R` or interacts with the user. Key commands include:

### Commands
- **ASK**: Prompts the user for input and stores it as a named constant.
- **TELL**: Outputs the current value of the register `R`.
- **ADD**: Adds a value or constant to `R`.
- **SUB**: Subtracts a value or constant from `R`.
- **MUL**: Multiplies `R` by a value or constant.
- **DIV**: Divides `R` by a value or constant.

---

## Getting Started

### Prerequisites
- Python 3.7 or higher.
- Basic knowledge of Python programming, with understanding of the CLI.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Hi-kue/tho-interpreter.git
   ```
2. Navigate to the project directory:
   ```bash
   cd tho-interpreter
   ```
3. Ensure you have Python installed by running:
   ```bash
   python --version | py --version | py3 --version | python3 --version
   ```

### Usage
1. Create a Tho script file (e.g., `script.txt`) with the desired commands in the `/checks/` directory.
2. Make sure you install all dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the interpreter by executing the `main.py` script:
   ```bash
   python main.py
   ```
4. Follow the prompts to select the Tho script file to interpret.
5. The interpreter will parse and execute the commands in the script file.
6. The output will be displayed in the console.

---

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.
