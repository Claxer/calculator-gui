import tkinter as tk
from tkinter import messagebox
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("500x700")
        self.root.configure(bg="#1e1e1e")
        self.memory = 0
        self.history = []

        self.prev = tk.Label(root,text="Previous: None",bg="#1e1e1e",fg="white",anchor="e")
        self.prev.pack(fill="x",padx=10,pady=(10,0))

        self.display = tk.Entry(root,font=("Segoe UI",24),justify="right",bg="#111",fg="lime",insertbackground="white")
        self.display.pack(fill="x",padx=10,pady=10)

        sci = tk.Frame(root,bg="#1e1e1e"); sci.pack()
        for t in ["√","x²","x³","π","e","sin","cos","tan","log","ln","!","Copy"]:
            tk.Button(sci,text=t,width=6,height=2,command=lambda x=t:self.special(x)).pack(side="left",padx=2,pady=2)

        frame=tk.Frame(root,bg="#1e1e1e"); frame.pack()
        buttons=[
            ["("," )","C","⌫"],
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","-"],
            ["0",".","=","+"]
        ]
        for r,row in enumerate(buttons):
            for c,t in enumerate(row):
                tk.Button(frame,text=t.strip(),font=("Segoe UI",18),width=5,height=2,
                          command=lambda x=t.strip():self.press(x)).grid(row=r,column=c,padx=4,pady=4)

        tk.Label(root,text="History",bg="#1e1e1e",fg="white").pack()
        self.listbox=tk.Listbox(root,height=10)
        self.listbox.pack(fill="both",expand=True,padx=10)

        self.status=tk.Label(root,text="Ready",anchor="w",bg="#333",fg="white")
        self.status.pack(fill="x")

        root.bind("<Return>",lambda e:self.calculate())
        root.bind("<Escape>",lambda e:self.clear())
        root.bind("<BackSpace>",lambda e:self.backspace())

    def press(self,v):
        if v=="=":
            self.calculate()
        elif v=="C":
            self.clear()
        elif v=="⌫":
            self.backspace()
        else:
            self.display.insert(tk.END,v)

    def clear(self):
        self.display.delete(0,tk.END)
        self.status.config(text="Cleared")

    def backspace(self):
        txt=self.display.get()
        self.display.delete(0,tk.END)
        self.display.insert(0,txt[:-1])

    def calculate(self):
        expr=self.display.get()
        try:
            ans=eval(expr,{"__builtins__":None},{})
            self.prev.config(text=f"Previous: {ans}")
            self.history.append(f"{expr} = {ans}")
            self.listbox.insert(tk.END,f"{expr} = {ans}")
            self.display.delete(0,tk.END)
            self.display.insert(0,str(ans))
            self.status.config(text="Calculated Successfully")
        except Exception:
            self.display.delete(0,tk.END)
            self.display.insert(0,"Error")
            self.status.config(text="Invalid Expression")

    def special(self,op):
        try:
            x=float(self.display.get())
            if op=="√": r=math.sqrt(x)
            elif op=="x²": r=x**2
            elif op=="x³": r=x**3
            elif op=="π": r=math.pi
            elif op=="e": r=math.e
            elif op=="sin": r=math.sin(math.radians(x))
            elif op=="cos": r=math.cos(math.radians(x))
            elif op=="tan": r=math.tan(math.radians(x))
            elif op=="log": r=math.log10(x)
            elif op=="ln": r=math.log(x)
            elif op=="!": r=math.factorial(int(x))
            elif op=="Copy":
                self.root.clipboard_clear()
                self.root.clipboard_append(self.display.get())
                self.status.config(text="Copied to clipboard")
                return
            self.display.delete(0,tk.END)
            self.display.insert(0,str(r))
        except Exception:
            messagebox.showerror("Error","Invalid operation")

root=tk.Tk()
CalculatorApp(root)
root.mainloop()
