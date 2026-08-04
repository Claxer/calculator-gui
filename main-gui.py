import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")
window.resizable(False, False)

display = tk.Entry(
    window,
    font=("Verdana", 24),
    justify="right",
    bd=10
)
display.pack(fill="x", padx=10, pady=20)

def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)


def clear():
    display.delete(0, tk.END)


def calculate():
    try:
        answer = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, answer)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

button_frame = tk.Frame(window)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in range(len(buttons)):
    for col in range(len(buttons[row])):
        text = buttons[row][col]

        if text == "=":
            command = calculate
        elif text == "C":
            command = clear
        else:
            command = lambda value=text: button_click(value)

        button = tk.Button(
            button_frame,
            text=text,
            font=("Verdana", 18),
            width=5,
            height=2,
            command=command
        )

        button.grid(row=row, column=col, padx=5, pady=5)

window.mainloop()
