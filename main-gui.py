import tkinter as tk
from tkinter import messagebox
import math
import random


class CalculatorApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("700x850")
        self.root.configure(bg="#1e1e1e")

        # ==========================================
        # CALCULATOR DATA
        # ==========================================

        self.memory = 0
        self.history = []
        self.last_answer = 0
        self.calculation_count = 0

        # DEG or RAD
        self.angle_mode = "DEG"

        # ==========================================
        # TOP INFORMATION
        # ==========================================

        self.prev = tk.Label(
            root,
            text="Previous: None",
            bg="#1e1e1e",
            fg="white",
            anchor="e",
            font=("Segoe UI", 11)
        )

        self.prev.pack(
            fill="x",
            padx=10,
            pady=(10, 0)
        )

        # ==========================================
        # DISPLAY
        # ==========================================

        self.display = tk.Entry(
            root,
            font=("Segoe UI", 24),
            justify="right",
            bg="#111",
            fg="lime",
            insertbackground="white"
        )

        self.display.pack(
            fill="x",
            padx=10,
            pady=10
        )

        # ==========================================
        # MODE BUTTON
        # ==========================================

        mode_frame = tk.Frame(
            root,
            bg="#1e1e1e"
        )

        mode_frame.pack()

        self.mode_button = tk.Button(
            mode_frame,
            text="Angle: DEG",
            width=12,
            height=2,
            command=self.toggle_angle_mode
        )

        self.mode_button.pack(
            side="left",
            padx=3,
            pady=3
        )

        tk.Button(
            mode_frame,
            text="Clear History",
            width=12,
            height=2,
            command=self.clear_history
        ).pack(
            side="left",
            padx=3,
            pady=3
        )

        # ==========================================
        # MEMORY BUTTONS
        # ==========================================

        memory_frame = tk.Frame(
            root,
            bg="#1e1e1e"
        )

        memory_frame.pack()

        memory_buttons = [
            ("MC", self.memory_clear),
            ("MR", self.memory_recall),
            ("M+", self.memory_add),
            ("M-", self.memory_subtract)
        ]

        for text, command in memory_buttons:

            tk.Button(
                memory_frame,
                text=text,
                width=7,
                height=2,
                command=command
            ).pack(
                side="left",
                padx=3,
                pady=3
            )

        # ==========================================
        # SCIENTIFIC BUTTONS
        # ==========================================

        sci_frame = tk.Frame(
            root,
            bg="#1e1e1e"
        )

        sci_frame.pack()

        scientific_buttons = [
            "√",
            "x²",
            "x³",
            "xʸ",
            "1/x",
            "π",
            "e",
            "Ans",
            "±",
            "%",
            "sin",
            "cos",
            "tan",
            "asin",
            "acos",
            "atan",
            "sinh",
            "cosh",
            "tanh",
            "log",
            "ln",
            "10ˣ",
            "eˣ",
            "2ˣ",
            "!",
            "abs",
            "floor",
            "ceil",
            "Copy",
            "Rand"
        ]

        for text in scientific_buttons:

            tk.Button(
                sci_frame,
                text=text,
                width=7,
                height=2,
                command=lambda x=text: self.special(x)
            ).pack(
                side="left",
                padx=2,
                pady=2
            )

        # ==========================================
        # BASIC CALCULATOR BUTTONS
        # ==========================================

        frame = tk.Frame(
            root,
            bg="#1e1e1e"
        )

        frame.pack()

        buttons = [
            ["(", ")", "C", "⌫"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        for r, row in enumerate(buttons):

            for c, text in enumerate(row):

                tk.Button(
                    frame,
                    text=text.strip(),
                    font=("Segoe UI", 18),
                    width=5,
                    height=2,
                    command=lambda x=text.strip(): self.press(x)
                ).grid(
                    row=r,
                    column=c,
                    padx=4,
                    pady=4
                )

        # ==========================================
        # EXTRA FUNCTIONS
        # ==========================================

        extra_frame = tk.Frame(
            root,
            bg="#1e1e1e"
        )

        extra_frame.pack()

        extra_buttons = [
            ("nPr", self.permutation),
            ("nCr", self.combination),
            ("Random", self.random_number),
            ("Load History", self.load_history)
        ]

        for text, command in extra_buttons:

            tk.Button(
                extra_frame,
                text=text,
                width=12,
                height=2,
                command=command
            ).pack(
                side="left",
                padx=3,
                pady=3
            )

        # ==========================================
        # HISTORY
        # ==========================================

        tk.Label(
            root,
            text="History",
            bg="#1e1e1e",
            fg="white",
            font=("Segoe UI", 12)
        ).pack()

        self.listbox = tk.Listbox(
            root,
            height=10
        )

        self.listbox.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        # ==========================================
        # DELETE HISTORY ITEM
        # ==========================================

        tk.Button(
            root,
            text="Delete Selected History",
            command=self.delete_history
        ).pack(
            pady=3
        )

        # ==========================================
        # STATUS BAR
        # ==========================================

        self.status = tk.Label(
            root,
            text="Ready",
            anchor="w",
            bg="#333",
            fg="white"
        )

        self.status.pack(
            fill="x"
        )

        # ==========================================
        # KEYBOARD SHORTCUTS
        # ==========================================

        root.bind(
            "<Return>",
            lambda e: self.calculate()
        )

        root.bind(
            "<Escape>",
            lambda e: self.clear()
        )

        root.bind(
            "<BackSpace>",
            lambda e: self.backspace()
        )

        # ==========================================
        # STARTUP MESSAGE
        # ==========================================

        self.status.config(
            text="Calculator Ready"
        )

    # ==========================================
    # BASIC BUTTON INPUT
    # ==========================================

    def press(self, value):

        if value == "=":

            self.calculate()

        elif value == "C":

            self.clear()

        elif value == "⌫":

            self.backspace()

        else:

            self.display.insert(
                tk.END,
                value
            )

    # ==========================================
    # CLEAR
    # ==========================================

    def clear(self):

        self.display.delete(
            0,
            tk.END
        )

        self.status.config(
            text="Cleared"
        )

    # ==========================================
    # BACKSPACE
    # ==========================================

    def backspace(self):

        text = self.display.get()

        self.display.delete(
            0,
            tk.END
        )

        self.display.insert(
            0,
            text[:-1]
        )

        self.status.config(
            text="Deleted last character"
        )

    # ==========================================
    # CALCULATE
    # ==========================================

    def calculate(self):

        expression = self.display.get()

        if expression == "":
            return

        try:

            answer = eval(
                expression,
                {
                    "__builtins__": None
                },
                {}
            )

            self.last_answer = answer

            self.calculation_count += 1

            self.prev.config(
                text=f"Previous: {answer}"
            )

            history_item = (
                f"{expression} = {answer}"
            )

            self.history.append(
                history_item
            )

            self.listbox.insert(
                tk.END,
                history_item
            )

            self.display.delete(
                0,
                tk.END
            )

            self.display.insert(
                0,
                str(answer)
            )

            self.status.config(
                text=f"Calculated Successfully | "
                     f"Calculations: {self.calculation_count}"
            )

        except Exception:

            self.display.delete(
                0,
                tk.END
            )

            self.display.insert(
                0,
                "Error"
            )

            self.status.config(
                text="Invalid Expression"
            )

    # ==========================================
    # ANGLE MODE
    # ==========================================

    def toggle_angle_mode(self):

        if self.angle_mode == "DEG":

            self.angle_mode = "RAD"

        else:

            self.angle_mode = "DEG"

        self.mode_button.config(
            text=f"Angle: {self.angle_mode}"
        )

        self.status.config(
            text=f"Angle mode changed to {self.angle_mode}"
        )

    # ==========================================
    # SCIENTIFIC FUNCTIONS
    # ==========================================

    def special(self, operation):

        try:

            # ------------------------------------------
            # COPY
            # ------------------------------------------

            if operation == "Copy":

                self.root.clipboard_clear()

                self.root.clipboard_append(
                    self.display.get()
                )

                self.status.config(
                    text="Copied to clipboard"
                )

                return

            # ------------------------------------------
            # PI
            # ------------------------------------------

            if operation == "π":

                result = math.pi

            # ------------------------------------------
            # E
            # ------------------------------------------

            elif operation == "e":

                result = math.e

            # ------------------------------------------
            # ANSWER
            # ------------------------------------------

            elif operation == "Ans":

                result = self.last_answer

            # ------------------------------------------
            # RANDOM
            # ------------------------------------------

            elif operation == "Rand":

                result = random.random()

            else:

                x = float(
                    self.display.get()
                )

                # --------------------------------------
                # SQUARE ROOT
                # --------------------------------------

                if operation == "√":

                    result = math.sqrt(x)

                # --------------------------------------
                # SQUARE
                # --------------------------------------

                elif operation == "x²":

                    result = x ** 2

                # --------------------------------------
                # CUBE
                # --------------------------------------

                elif operation == "x³":

                    result = x ** 3

                # --------------------------------------
                # POWER
                # --------------------------------------

                elif operation == "xʸ":

                    result = x ** 2

                    self.status.config(
                        text="xʸ currently uses x²"
                    )

                # --------------------------------------
                # RECIPROCAL
                # --------------------------------------

                elif operation == "1/x":

                    result = 1 / x

                # --------------------------------------
                # SIGN
                # --------------------------------------

                elif operation == "±":

                    result = -x

                # --------------------------------------
                # PERCENTAGE
                # --------------------------------------

                elif operation == "%":

                    result = x / 100

                # --------------------------------------
                # FACTORIAL
                # --------------------------------------

                elif operation == "!":

                    result = math.factorial(
                        int(x)
                    )

                # --------------------------------------
                # ABSOLUTE
                # --------------------------------------

                elif operation == "abs":

                    result = abs(x)

                # --------------------------------------
                # FLOOR
                # --------------------------------------

                elif operation == "floor":

                    result = math.floor(x)

                # --------------------------------------
                # CEILING
                # --------------------------------------

                elif operation == "ceil":

                    result = math.ceil(x)

                # --------------------------------------
                # LOG
                # --------------------------------------

                elif operation == "log":

                    result = math.log10(x)

                # --------------------------------------
                # NATURAL LOG
                # --------------------------------------

                elif operation == "ln":

                    result = math.log(x)

                # --------------------------------------
                # 10 POWER
                # --------------------------------------

                elif operation == "10ˣ":

                    result = 10 ** x

                # --------------------------------------
                # E POWER
                # --------------------------------------

                elif operation == "eˣ":

                    result = math.exp(x)

                # --------------------------------------
                # 2 POWER
                # --------------------------------------

                elif operation == "2ˣ":

                    result = 2 ** x

                # --------------------------------------
                # TRIGONOMETRY
                # --------------------------------------

                elif operation == "sin":

                    if self.angle_mode == "DEG":

                        result = math.sin(
                            math.radians(x)
                        )

                    else:

                        result = math.sin(x)

                elif operation == "cos":

                    if self.angle_mode == "DEG":

                        result = math.cos(
                            math.radians(x)
                        )

                    else:

                        result = math.cos(x)

                elif operation == "tan":

                    if self.angle_mode == "DEG":

                        result = math.tan(
                            math.radians(x)
                        )

                    else:

                        result = math.tan(x)

                # --------------------------------------
                # INVERSE TRIGONOMETRY
                # --------------------------------------

                elif operation == "asin":

                    result = math.asin(x)

                    if self.angle_mode == "DEG":

                        result = math.degrees(
                            result
                        )

                elif operation == "acos":

                    result = math.acos(x)

                    if self.angle_mode == "DEG":

                        result = math.degrees(
                            result
                        )

                elif operation == "atan":

                    result = math.atan(x)

                    if self.angle_mode == "DEG":

                        result = math.degrees(
                            result
                        )

                # --------------------------------------
                # HYPERBOLIC
                # --------------------------------------

                elif operation == "sinh":

                    result = math.sinh(x)

                elif operation == "cosh":

                    result = math.cosh(x)

                elif operation == "tanh":

                    result = math.tanh(x)

                else:

                    return

            # ==========================================
            # DISPLAY RESULT
            # ==========================================

            self.display.delete(
                0,
                tk.END
            )

            self.display.insert(
                0,
                str(result)
            )

            self.last_answer = result

            self.status.config(
                text=f"{operation} calculated"
            )

        except Exception:

            messagebox.showerror(
                "Error",
                "Invalid operation"
            )

            self.status.config(
                text="Scientific operation failed"
            )

    # ==========================================
    # MEMORY CLEAR
    # ==========================================

    def memory_clear(self):

        self.memory = 0

        self.status.config(
            text="Memory cleared"
        )

    # ==========================================
    # MEMORY RECALL
    # ==========================================

    def memory_recall(self):

        self.display.delete(
            0,
            tk.END
        )

        self.display.insert(
            0,
            str(self.memory)
        )

        self.status.config(
            text="Memory recalled"
        )

    # ==========================================
    # MEMORY ADD
    # ==========================================

    def memory_add(self):

        try:

            value = float(
                self.display.get()
            )

            self.memory += value

            self.status.config(
                text=f"Added {value} to memory"
            )

        except ValueError:

            self.status.config(
                text="Invalid memory value"
            )

    # ==========================================
    # MEMORY SUBTRACT
    # ==========================================

    def memory_subtract(self):

        try:

            value = float(
                self.display.get()
            )

            self.memory -= value

            self.status.config(
                text=f"Subtracted {value} from memory"
            )

        except ValueError:

            self.status.config(
                text="Invalid memory value"
            )

    # ==========================================
    # PERMUTATION
    # ==========================================

    def permutation(self):

        try:

            values = self.display.get().split(",")

            n = int(values[0])
            r = int(values[1])

            result = (
                math.factorial(n) /
                math.factorial(n - r)
            )

            self.display.delete(
                0,
                tk.END
            )

            self.display.insert(
                0,
                str(int(result))
            )

            self.status.config(
                text="Permutation calculated"
            )

        except Exception:

            messagebox.showerror(
                "Permutation",
                "Enter values like: 5,2"
            )

    # ==========================================
    # COMBINATION
    # ==========================================

    def combination(self):

        try:

            values = self.display.get().split(",")

            n = int(values[0])
            r = int(values[1])

            result = math.comb(
                n,
                r
            )

            self.display.delete(
                0,
                tk.END
            )

            self.display.insert(
                0,
                str(result)
            )

            self.status.config(
                text="Combination calculated"
            )

        except Exception:

            messagebox.showerror(
                "Combination",
                "Enter values like: 5,2"
            )

    # ==========================================
    # RANDOM NUMBER
    # ==========================================

    def random_number(self):

        try:

            maximum = int(
                self.display.get()
            )

            result = random.randint(
                1,
                maximum
            )

            self.display.delete(
                0,
                tk.END
            )

            self.display.insert(
                0,
                str(result)
            )

            self.status.config(
                text=f"Random number from 1 to {maximum}"
            )

        except Exception:

            messagebox.showerror(
                "Random Number",
                "Enter a maximum number first."
            )

    # ==========================================
    # CLEAR HISTORY
    # ==========================================

    def clear_history(self):

        self.history.clear()

        self.listbox.delete(
            0,
            tk.END
        )

        self.status.config(
            text="History cleared"
        )

    # ==========================================
    # DELETE HISTORY ITEM
    # ==========================================

    def delete_history(self):

        selected = self.listbox.curselection()

        if not selected:

            self.status.config(
                text="Select a history item first"
            )

            return

        index = selected[0]

        self.listbox.delete(
            index
        )

        del self.history[index]

        self.status.config(
            text="History item deleted"
        )

    # ==========================================
    # LOAD HISTORY RESULT
    # ==========================================

    def load_history(self):

        selected = self.listbox.curselection()

        if not selected:

            self.status.config(
                text="Select a history item first"
            )

            return

        index = selected[0]

        item = self.history[index]

        try:

            result = item.split("=")[-1].strip()

            self.display.delete(
                0,
                tk.END
            )

            self.display.insert(
                0,
                result
            )

            self.status.config(
                text="History result loaded"
            )

        except Exception:

            self.status.config(
                text="Could not load history"
            )


# ==========================================
# START PROGRAM
# ==========================================

root = tk.Tk()

app = CalculatorApp(root)

root.mainloop()
