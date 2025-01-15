## General Tho Interpreter Todos
- [x] Initialize the register `R` to 0.0 at the start of the program.
- [x] Prompt the user to input the name of the Tho script file to interpret.
    - [x] File should be stored in the same directory as `/checks/`.
- [x] Open the specified script file and read its contents line by line.
- [x] Register the built-in keywords within every Tho script being:
    - [x] `ADD`
    - [x] `SUB`
    - [x] `MUL`
    - [x] `DIV`
    - [x] `ASK`
    - [x] `TELL`
- [x] For each line in the script file:
    - [x] If the line is a comment, ignore it.
    - [x] If the line is a Tho command, execute it.
- [x] Ensure the named constants are created by the `ASK` command.
- [ ] Handle file I/O errors gracefully (e.g. throw an exception if file not found).
- [ ] Add comments for all major sections of the code to explain what they do (OPTIONAL).


## Tho Commands
- [x] Implement the `ASK` command.
    - [x] Prompt the user for a floating-point number.
    - [x] Store the value as a named constant within a dictionary.
- [x] Implement the `ADD` command.
    - [x]  Add the provided value of constant to the registrar `R`.
- [x] Implement the `SUB` command.
    - [x] Subtract the provided value or constant from the registrar `R`.
- [x] Implement the `MUL` command.
    - [x] Multiply the registrar `R` with the provided value or constant.
- [x] Implement the `DIV` command.
    - [x] Divide the registrar `R` by the provided value or constant.
- [x] Implement the `TELL` command.
    - [x] Print the value of the registrar `R` to the console.