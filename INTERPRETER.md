# THO Interpreter Challenge

## Introduction

This challenge asks to implement a simple Python program that acts as
an interpreter for the Tho Programming Language. Tho is a minimalistic
scripting language designed to perform basic arithmetic operations on
floating-point numbers; the catch, there is a single register `R` that
holds the current value of the most recently executed operation.

## About the Tho Language

We already know about Tho a little bit from the introduction, so let's 
dive into the details and introduce the commands and syntax of the language:

### Commands

1. **ASK**
    - **Effect:** Prompts the user to input a floating-point value and stores it as the constant `T`.
    - Example:
      ```
      ASK A
      ```
        - Prompts the user for input and assigns the value to `A`.

2. **TELL**
    - **Effect:** Displays the current value of the register `R`.
    - Example:
      ```
      TELL
      ```
        - Outputs the value of `R`.

3. **ADD `e`**
    - **Effect:** Adds the value of `e` (a floating-point literal or a constant created by `ASK`) to the register `R`.
    - Example:
      ```
      ADD 5.0
      ```
        - Adds `5.0` to the value of `R`.

4. **SUB `e`**
    - **Effect:** Subtracts the value of `e` from the register `R`.
    - Example:
      ```
      SUB 2.0
      ```
        - Subtracts `2.0` from the value of `R`.

5. **MUL `e`**
    - **Effect:** Multiplies the value of `R` by `e`.
    - Example:
      ```
      MUL 3.0
      ```
        - Multiplies `R` by `3.0`.

6. **DIV `e`**
    - **Effect:** Divides the value of `R` by `e` (floating-point division).
    - Example:
      ```
      DIV 4.0
      ```
        - Divides `R` by `4.0`.

## Your Challenge

Write a Python program that:

1. **Prompts the user for the name of a Tho script file** (a `.txt` file containing Tho commands).
2. **Opens and reads the script file line by line**.
3. **Parses and executes each command** according to the rules of the Tho language.
4. **Handles user input** for `ASK` commands and displays output for `TELL` commands.

---

## TODOS

### General Tho Interpreter Todos
- [ ] Initialize the register `R` to 0.0 at the start of the program.
- [ ] Prompt the user to input the name of the Tho script file to interpret.
    - [ ] File should be stored in the same directory as `/checks/`.
- [ ] Open the specified script file and read its contents line by line.
- [ ] Register the built-in keywords within every Tho script being:
    - [ ] `ADD`
    - [ ] `SUB`
    - [ ] `MUL`
    - [ ] `DIV`
    - [ ] `ASK`
    - [ ] `TELL`
- [ ] For each line in the script file:
    - [ ] If the line is a comment, ignore it.
    - [ ] If the line is a Tho command, execute it.
- [ ] Ensure the named constants are created by the `ASK` command.
- [ ] Handle file I/O errors gracefully (e.g. throw an exception if file not found).
- [ ] Add comments for all major sections of the code to explain what they do (OPTIONAL).


### Tho Commands
- [ ] Implement the `ASK` command.
    - [ ] Prompt the user for a floating-point number.
    - [ ] Store the value as a named constant within a dictionary.
- [ ] Implement the `ADD` command.
    - [ ]  Add the provided value of constant to the registrar `R`.
- [ ] Implement the `SUB` command.
    - [ ] Subtract the provided value or constant from the registrar `R`.
- [ ] Implement the `MUL` command.
    - [ ] Multiply the registrar `R` with the provided value or constant.
- [ ] Implement the `DIV` command.
    - [ ] Divide the registrar `R` by the provided value or constant.
- [ ] Implement the `TELL` command.
    - [ ] Print the value of the registrar `R` to the console.

--- 

## Notes

You will be provided a file (or you can create your own) that contains an example 
Tho script for testing your implementation. Make sure to run the script and
check the output to ensure your implementation is working based on the 
requirements. Happy coding! 😊
