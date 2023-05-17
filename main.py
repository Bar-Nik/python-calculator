import tkinter as tk
from tkinter import messagebox


class Calculator():

    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry(f"240x270+100+200")
        self.win.resizable(False, False)
        self.win['bg'] = '#bfa8a8'
        self.win.title('Калькулятор')

        self.win.bind('<Key>', self.press_key)  # обрабатывает событие - любое нажатие на клавиатуре

        self.calc = tk.Entry(justify=tk.RIGHT, font=('Arial', 15), width=15)
        self.calc.insert(0, '0')
        self.calc['state'] = tk.DISABLED
        self.calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5)

        self.make_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
        self.make_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
        self.make_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
        self.make_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
        self.make_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
        self.make_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
        self.make_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
        self.make_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
        self.make_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
        self.make_digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

        self.make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
        self.make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
        self.make_operation_button('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
        self.make_operation_button('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)

        self.make_calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
        self.make_clear_button('C').grid(row=4, column=1, stick='wens', padx=5, pady=5)

        self.win.grid_columnconfigure(0, minsize=60)
        self.win.grid_columnconfigure(1, minsize=60)
        self.win.grid_columnconfigure(2, minsize=60)
        self.win.grid_columnconfigure(3, minsize=60)

        self.win.grid_rowconfigure(1, minsize=60)
        self.win.grid_rowconfigure(2, minsize=60)
        self.win.grid_rowconfigure(3, minsize=60)
        self.win.grid_rowconfigure(4, minsize=60)

        self.win.mainloop()

    def add_digit(self, digit):  # добавляем число
        value = self.calc.get()
        if value[0] == '0' and len(value) == 1:
            value = value[1:]
        self.calc['state'] = tk.NORMAL
        self.calc.delete(0, tk.END)
        self.calc.insert(0, value + digit)
        self.calc['state'] = tk.DISABLED

    def make_digit_button(self, digit):  # действия при нажатии на цифры
        return tk.Button(text=digit, bd=5, font=('Arial', 12,), command=lambda: self.add_digit(digit))

    def make_operation_button(self, operation):  # действия при нажатии на операции +-*/
        return tk.Button(text=operation, bd=5, font=('Arial', 12,), fg='blue',
                         command=lambda: self.add_operation(operation))

    def make_calc_button(self, operation):  # действия при нажатии на операцию =
        return tk.Button(text=operation, bd=5, font=('Arial', 12,), fg='blue',
                         command=self.calculate)

    def add_operation(self, operation):  # добавляем операции
        value = self.calc.get()
        if value[-1] in '-+*/':
            value = value[:-1]
        elif '+' in value or '-' in value or '*' in value or '/' in value:
            self.calculate()
            value = self.calc.get()
        self.calc['state'] = tk.NORMAL
        self.calc.delete(0, tk.END)
        self.calc.insert(0, value + operation)
        self.calc['state'] = tk.DISABLED

    def calculate(self):  # вычисление
        value = self.calc.get()
        if value[-1] in '-+*/':
            operation = value[-1]
            value = value[:-1] + operation + value[:-1]

        self.calc['state'] = tk.NORMAL
        self.calc.delete(0, tk.END)
        try:
            self.calc.insert(0, eval(value))
        except (NameError, SyntaxError):
            messagebox.showinfo('Внимание', 'Вводим цифры!')
            self.calc.insert(0, 0)
        except ZeroDivisionError:
            messagebox.showinfo('Внимание', 'На ноль делить нельзя!')
            self.calc.insert(0, 0)
        self.calc['state'] = tk.DISABLED

    def make_clear_button(self, operation):  # действие при нажатии на очищение
        return tk.Button(text=operation, bd=5, font=('Arial', 12,), fg='blue',
                         command=self.clear)

    def clear(self):  # очищение
        self.calc['state'] = tk.NORMAL
        self.calc.delete(0, tk.END)
        self.calc.insert(0, 0)
        self.calc['state'] = tk.DISABLED

    def press_key(self, event):
        print(repr(event.char))
        if event.char.isdigit():
            self.add_digit(event.char)
        elif event.char in '+-*/':
            self.add_operation(event.char)
        elif event.char == '=' and event.char == '\r':
            self.calculate()


Calculator()
