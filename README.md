# Advanced Calculator GUI

## Description

An advanced calculator application with a modern graphical user interface (GUI) built using Python and Tkinter. This project allows users to perform both basic and scientific calculations through an interactive desktop application. It includes a calculation history, keyboard shortcuts, clipboard support, and a clean dark-themed interface.

## Features

### Basic Calculator
- Addition
- Subtraction
- Multiplication
- Division
- Decimal (.) support
- Parentheses `(` and `)`
- Clear (C) button
- Backspace (⌫) button
- Error handling for invalid expressions
- Previous calculation display

### Scientific Calculator
- Square Root (√)
- Square (x²)
- Cube (x³)
- Pi (π)
- Euler's Number (e)
- Sine (sin)
- Cosine (cos)
- Tangent (tan)
- Logarithm (log)
- Natural Logarithm (ln)
- Factorial (!)

### Additional Features
- Modern dark-themed interface
- Calculation history
- Copy result to clipboard
- Status bar for user feedback
- Keyboard shortcuts
  - Enter = Calculate
  - Backspace = Delete last character
  - Escape = Clear display
- Object-oriented program structure
- Simple and user-friendly layout

## Technologies Used

- Python 3
- Tkinter
- Math Module

## Project Structure

```
Calculator-GUI/
│
├── main-gui.py
├── README.md
└── LICENSE
```

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open the project in VS Code, PyCharm, or your preferred Python IDE.
4. Run:

```bash
python main.py
```

## Screenshots
<img width="400" height="500" alt="image" src="https://github.com/user-attachments/assets/5424d3e2-a8d7-402b-a685-86f3cac7e796" />


## What I Learned

Through this project, I learned how to:

- Build desktop applications using Tkinter
- Design a graphical user interface with frames, labels, buttons, and entry widgets
- Use object-oriented programming (OOP) to organize larger projects
- Handle button events and keyboard shortcuts
- Perform mathematical calculations using Python's `math` module
- Store and display calculation history
- Copy text to the system clipboard
- Update the interface dynamically during program execution
- Handle invalid input using exception handling (`try` and `except`)
- Create a modern dark-themed application
- Improve user experience through better interface design

## Future Improvements

- Replace `eval()` with a safer mathematical expression parser
- Add light mode and customizable themes
- Implement memory functions (MC, MR, M+, M−, MS)
- Save calculation history to a file
- Add keyboard-only navigation
- Make the interface responsive and resizable
- Add graph plotting for mathematical functions
- Add Programmer Mode (Binary, Octal, Decimal, Hexadecimal)
- Add Unit Converter
- Add Currency Converter
- Improve button styling with custom icons and animations
- Package the application as a standalone executable (.exe)

## License

This project is licensed under the MIT License.
