import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор")

        self.display = tk.Entry(master, width=25, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Создаем кнопки для цифр и операций
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("C", 4, 2)
        self.create_button("+", 4, 3)

        self.create_button("=", 5, 0, columnspan=4)

        # Очищаем дисплей
        self.clear_display()

    def create_button(self, text, row, col, rowspan=1, columnspan=1):
        button = tk.Button(self.master, text=text, padx=10, pady=5, font=('Arial', 16), command=lambda:self.handle_click(text))
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, padx=5, pady=5)

    def handle_click(self, text):
        if text == "C":
            self.clear_display()
        elif text == "=":
            self.calculate()
        else:
            self.display.insert(tk.END, text)

    def clear_display(self):
        self.display.delete(0, tk.END)

    def calculate(self):
        expression = self.display.get()
        try:
            result = eval(expression)
            self.clear_display()
            self.display.insert(tk.END, str(result))
        except:
            self.clear_display()
            self.display.insert(tk.END, "Ошибка")

if __name__ == '__main__':
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
