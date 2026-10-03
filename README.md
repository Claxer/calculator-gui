# Advanced Calculator GUI

## Description

An advanced calculator application with a modern graphical user interface (GUI) built using **Python and Tkinter**. This project allows users to perform both basic and scientific calculations through an interactive desktop application.

The calculator includes basic arithmetic, scientific functions, trigonometric calculations, memory functions, angle mode selection, calculation history, clipboard support, random number generation, permutation and combination calculations, and keyboard shortcuts.

The application uses a dark-themed interface and is designed to be simple and user-friendly while demonstrating different Python programming concepts.

## Features

### Basic Calculator

* Addition
* Subtraction
* Multiplication
* Division
* Decimal (`.`) support
* Parentheses `(` and `)`
* Clear (`C`) button
* Backspace (`⌫`) button
* Percentage (`%`)
* Sign change (`±`)
* Reciprocal (`1/x`)
* Power calculations
* Error handling for invalid expressions
* Previous calculation display
* Last answer (`Ans`) support

### Scientific Calculator

* Square Root (`√`)
* Square (`x²`)
* Cube (`x³`)
* Power (`xʸ`)
* Pi (`π`)
* Euler's Number (`e`)
* Sine (`sin`)
* Cosine (`cos`)
* Tangent (`tan`)
* Inverse Sine (`asin`)
* Inverse Cosine (`acos`)
* Inverse Tangent (`atan`)
* Hyperbolic Sine (`sinh`)
* Hyperbolic Cosine (`cosh`)
* Hyperbolic Tangent (`tanh`)
* Common Logarithm (`log`)
* Natural Logarithm (`ln`)
* `10ˣ`
* `eˣ`
* `2ˣ`
* Factorial (`!`)
* Absolute Value (`abs`)
* Floor (`floor`)
* Ceiling (`ceil`)

### Angle Mode

The calculator supports two angle modes for trigonometric calculations:

* **DEG** - Degrees
* **RAD** - Radians

The user can switch between the two modes using the **Angle** button.

Example:

```text
Angle: DEG
```

or:

```text
Angle: RAD
```

This allows trigonometric functions such as `sin`, `cos`, and `tan` to work with either degrees or radians.

### Memory Functions

The calculator includes a memory system for temporarily storing numerical values.

* **MC** - Memory Clear
* **MR** - Memory Recall
* **M+** - Add current value to memory
* **M-** - Subtract current value from memory

Example:

```text
Enter: 100
Press M+
Clear the display
Press MR

Result: 100
```

The memory value remains available while the application is running.

### Previous Answer

The calculator keeps track of the most recent answer.

The **Ans** button can be used to insert the previous result into the calculator.

Example:

```text
5 + 5
= 10

Press Ans

10
```

This allows the previous calculation result to be reused in another calculation.

### Permutation

The calculator can calculate permutations using `nPr`.

The user enters values in the format:

```text
5,2
```

The calculator then calculates:

```text
5P2 = 20
```

This feature uses Python's factorial calculations.

### Combination

The calculator also supports combinations using `nCr`.

The user can enter:

```text
5,2
```

The result is:

```text
5C2 = 10
```

This feature uses Python's built-in combination calculation.

### Random Number Generator

The calculator can generate a random number between `1` and a maximum value.

For example:

```text
Enter:

100

Press Random
```

The calculator will generate a random number between:

```text
1 - 100
```

This feature uses Python's `random` module.

### Calculation History

The calculator stores calculations performed during the current session.

Example:

```text
5 + 5 = 10
10 * 2 = 20
√25 = 5.0
```

The history is displayed in a listbox at the bottom of the application.

Users can:

* View previous calculations
* Select a history item
* Load a previous result
* Delete a selected history item
* Clear the entire history

### History Management

The calculator provides several tools for managing calculation history.

#### Clear History

Removes all saved calculations from the history list.

#### Delete Selected History

Allows the user to select one calculation and remove it.

#### Load History

Allows the user to select a previous calculation and load its result back into the calculator display.

This makes it easier to reuse previous answers.

### Clipboard Support

The calculator includes a **Copy** button that copies the current display value to the system clipboard.

Example:

```text
Result: 125.5

Press Copy
```

The result can then be pasted into another application.

### Calculation Counter

The application keeps track of how many successful calculations have been performed during the current session.

The status bar displays the calculation count after a successful calculation.

Example:

```text
Calculated Successfully | Calculations: 5
```

### Keyboard Shortcuts

The calculator supports keyboard shortcuts for common actions.

| Key       | Function              |
| --------- | --------------------- |
| Enter     | Calculate             |
| Backspace | Delete last character |
| Escape    | Clear display         |

This allows users to interact with the calculator using the keyboard in addition to the GUI buttons.

### Status Bar

A status bar is displayed at the bottom of the application.

It provides feedback such as:

```text
Calculator Ready
```

```text
Calculated Successfully
```

```text
History cleared
```

```text
Copied to clipboard
```

```text
Invalid Expression
```

This helps users understand what the calculator is currently doing.

### Error Handling

The calculator uses Python's `try` and `except` statements to handle invalid calculations and prevent the application from crashing.

For example, invalid mathematical operations display an error message instead of terminating the program.

Example:

```text
Error
Invalid operation
```

This provides a better user experience when incorrect values are entered.

---

## User Interface

The application uses a dark-themed graphical interface.

The interface contains:

```text
Advanced Calculator
│
├── Previous Answer
├── Display
├── Angle Mode
├── History Controls
├── Memory Buttons
├── Scientific Buttons
├── Basic Calculator Buttons
├── Extra Functions
├── Calculation History
├── History Controls
└── Status Bar
```

The layout is organized using Tkinter frames to keep the different calculator sections separated.

---

## Technologies Used

* **Python 3**
* **Tkinter**
* **Math Module**
* **Random Module**

Tkinter is used to create the graphical user interface.

The `math` module provides scientific and mathematical functions.

The `random` module is used for random number generation.

---

## Python Concepts Used

This project demonstrates several Python programming concepts.

### Object-Oriented Programming

The calculator is organized using a class:

```python
class CalculatorApp:
```

The class contains the calculator's interface, variables, and functions.

This makes the program easier to organize and maintain.

### Functions

Different functions are used for different calculator operations.

Examples include:

```python
def calculate():
```

```python
def special():
```

```python
def memory_add():
```

```python
def memory_recall():
```

```python
def clear_history():
```

```python
def delete_history():
```

```python
def load_history():
```

```python
def toggle_angle_mode():
```

Using separate functions makes the program easier to understand and modify.

### Variables

Variables are used to store information such as:

```python
self.memory = 0
self.last_answer = 0
self.calculation_count = 0
self.angle_mode = "DEG"
```

These variables allow the calculator to keep track of its current state.

### Lists

A list is used to store calculation history:

```python
self.history = []
```

New calculations are added to the list when the user performs a calculation.

### Conditional Statements

The program uses `if`, `elif`, and `else` statements to determine which operation should be performed.

Example:

```python
if operation == "√":
    result = math.sqrt(x)

elif operation == "x²":
    result = x ** 2

elif operation == "x³":
    result = x ** 3
```

### Exception Handling

The calculator uses:

```python
try:
```

and:

```python
except:
```

to handle invalid mathematical operations and incorrect input.

This prevents common errors from crashing the application.

### Loops

Loops are used when creating groups of calculator buttons.

For example:

```python
for text in scientific_buttons:
```

This avoids having to manually create every button separately.

### Event Handling

Tkinter button commands are connected to Python functions.

For example:

```python
command=lambda x=text: self.special(x)
```

When the user clicks a scientific button, the corresponding operation is executed.

### Keyboard Events

The program uses Tkinter's `bind()` function to connect keyboard keys to calculator functions.

```python
root.bind("<Return>", lambda e: self.calculate())
```

This allows the Enter key to perform calculations.

---

## Project Structure

```text
Calculator-GUI/
│
├── main-gui.py
├── README.md
└── LICENSE
```

### `main-gui.py`

Contains the complete calculator application, including:

* GUI design
* Calculator operations
* Scientific functions
* Memory functions
* History management
* Keyboard shortcuts
* Error handling
* Random number generation
* Statistics

### `README.md`

Contains the project documentation, features, instructions, and learning information.

### `LICENSE`

Contains the license information for the project.

---

## How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

You can check your Python version using:

```bash
python --version
```

### 2. Clone or Download the Repository

Clone the repository using Git:

```bash
git clone https://github.com/your-username/Calculator-GUI.git
```

Or download the repository as a ZIP file.

### 3. Open the Project

Open the project using:

* PyCharm
* Visual Studio Code
* Another Python IDE

### 4. Run the Program

If the main file is named `main-gui.py`, run:

```bash
python main-gui.py
```

If the file is renamed to `main.py`, run:

```bash
python main.py
```

---

## Example Calculations

### Basic Arithmetic

```text
10 + 5
```

Result:

```text
15
```

### Square Root

```text
√25
```

Result:

```text
5.0
```

### Square

```text
5²
```

Result:

```text
25
```

### Factorial

```text
5!
```

Result:

```text
120
```

### Trigonometry

Using DEG mode:

```text
sin(30)
```

Result:

```text
0.5
```

### Logarithm

```text
log(100)
```

Result:

```text
2.0
```

### Combination

```text
5,2
```

Using `nCr`:

```text
10
```

### Permutation

```text
5,2
```

Using `nPr`:

```text
20
```

---

## Screenshots

<img width="400" height="500" alt="Advanced Calculator GUI" src="https://github.com/user-attachments/assets/5424d3e2-a8d7-402b-a685-86f3cac7e796" />

---

## What I Learned

Through this project, I learned how to:

* Build desktop applications using Tkinter
* Design a graphical user interface using frames, labels, buttons, entry widgets, and listboxes
* Use object-oriented programming (OOP)
* Organize a larger Python program into different functions
* Handle button events
* Handle keyboard shortcuts
* Perform mathematical calculations using Python's `math` module
* Generate random numbers using the `random` module
* Create scientific calculator functions
* Implement trigonometric calculations
* Work with degrees and radians
* Create a calculator memory system
* Store and display calculation history
* Delete individual history items
* Clear calculation history
* Load previous results
* Copy text to the system clipboard
* Track the number of calculations performed
* Use Python lists and variables to store application data
* Use `try` and `except` for error handling
* Create a modern dark-themed GUI
* Improve user experience through status messages and organized controls
* Connect GUI buttons to Python functions
* Use keyboard event binding in Tkinter

---

## Future Improvements

Although the calculator already contains many advanced features, possible future improvements include:

* Replace `eval()` with a safer mathematical expression parser
* Add light mode
* Add customizable themes
* Save calculation history to a file
* Save memory values between sessions
* Add keyboard-only navigation
* Make the interface fully responsive and resizable
* Add graph plotting for mathematical functions
* Add Programmer Mode

  * Binary
  * Octal
  * Decimal
  * Hexadecimal
* Add Unit Converter
* Add Currency Converter
* Add more advanced mathematical functions
* Add equation solving
* Add matrix calculations
* Add statistics calculations
* Add a calculation history export feature
* Add custom button icons and animations
* Add a scientific expression preview
* Package the application as a standalone `.exe`

---

## Known Limitations

The current version has a few limitations:

* Calculation history is only stored while the program is running.
* Memory values are not saved after closing the application.
* The calculator uses `eval()` for basic mathematical expressions.
* The `xʸ` feature currently uses the existing power implementation and can be improved with a dedicated second-value input.
* The random number generator works with a maximum value entered by the user.
* Permutation and combination inputs use a comma-separated format such as `5,2`.

These limitations can be addressed in future versions.

---

## License

This project is licensed under the MIT License.
