import tkinter as tk

class IOSCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("eivyddd")
        self.root.geometry("420x620")
        self.root.resizable(False, False)
        self.root.configure(bg="black")

        self.total = 0
        self.current = ""
        self.operator = ""
        self.reset_next = False

        self.display = tk.Label(
            root,
            text="0",
            anchor='e',
            justify="right",
            font=("Helvetica", 26),
            bg="black",
            fg="white",
            padx=24,
            wraplength=380,
            height=3
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.create_buttons()

        for i in range(6):
            self.root.rowconfigure(i, weight=1)
        for i in range(4):
            self.root.columnconfigure(i, weight=1)

        for child in self.root.winfo_children():
            if isinstance(child, tk.Button):
                child.configure(pady=10)

    def create_buttons(self):
        buttons = [
            ["AC", "+/-", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        for r, row in enumerate(buttons, start=1):
            for c, key in enumerate(row):
                if key == "0":
                    btn = tk.Button(
                        self.root, text=key, font=("Helvetica", 24),
                        bg="#333333", fg="white", bd=0,
                        command=lambda x=key: self.button_press(x)
                    )
                    btn.grid(row=r, column=0, columnspan=2, sticky="nsew", padx=1, pady=1)
                elif key == "." and len(row) == 3:
                    btn = tk.Button(
                        self.root, text=key, font=("Helvetica", 24),
                        bg="#333333", fg="white", bd=0,
                        command=lambda x=key: self.button_press(x)
                    )
                    btn.grid(row=r, column=2, sticky="nsew", padx=1, pady=1)
                elif key == "=" and len(row) == 3:
                    btn = tk.Button(
                        self.root, text=key, font=("Helvetica", 24),
                        bg="#FF9500", fg="white", bd=0,
                        command=lambda x=key: self.button_press(x)
                    )
                    btn.grid(row=r, column=3, sticky="nsew", padx=1, pady=1)
                else:
                    btn = tk.Button(
                        self.root, text=key, font=("Helvetica", 24),
                        bg=self.get_color(key), fg="white", bd=0,
                        command=lambda x=key: self.button_press(x)
                    )
                    btn.grid(row=r, column=c, sticky="nsew", padx=1, pady=1)

    def get_color(self, key):
        if key in ["+", "-", "×", "÷", "="]:
            return "#FF9500"
        elif key in ["AC", "+/-", "%"]:
            return "#A5A5A5"
        else:
            return "#333333"

    def button_press(self, key):
        if key == "AC":
            self.total = 0
            self.current = ""
            self.operator = ""
            self.display.config(text="0")
            self.reset_next = False

        elif key in "+-×÷":
            if self.current:
                self.total = float(self.current)
                self.operator = key
                self.reset_next = True

        elif key == "=":
            self.lyrics = [
                "ikaw lang at ikaw",
                "ang sinisigaw",
                "ng puso kong 'di mapakali",
                "ikaw lang at ikaw",
                "ang sinisigaw",
                "pag-ibig ko sana mapansin",
                "ongkee",
                "miss kona kayo tvl cm pati siya"
                
            ]
            self.timings = [2500, 2500, 4000, 2500, 2400, 3500]  
            self.current_line = 0
            self.show_lyrics_with_timing()

        elif key == "+/-":
            if self.current:
                if self.current.startswith("-"):
                    self.current = self.current[1:]
                else:
                    self.current = "-" + self.current
                self.display.config(text=self.current)

        elif key == "%":
            if self.current:
                self.current = str(float(self.current) / 100)
                self.display.config(text=self.format_number(self.current))

        else:  
            if self.reset_next:
                self.current = ""
                self.reset_next = False

            if key == "." and "." in self.current:
                return

            self.current += key
            self.display.config(text=self.current)

    def show_lyrics_with_timing(self):
        if self.current_line < len(self.lyrics):
            line = self.lyrics[self.current_line]
            self.display.config(text=line)
            delay = self.timings[self.current_line]
            self.current_line += 1
            self.root.after(delay, self.show_lyrics_with_timing)
        else:
            self.reset_next = True
            self.current = ""
            self.operator = ""
            self.total = 0

    def format_number(self, num_str):
        num = float(num_str)
        return str(int(num)) if num == int(num) else str(round(num, 8))


if __name__ == "__main__":
    root = tk.Tk()
    app = IOSCalculator(root)
    #root.iconbitmap("skibidi.ico")
    root.mainloop()
