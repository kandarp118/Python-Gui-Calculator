import tkinter as tk
from tkinter import messagebox

class GUICalculator:
    def __init__(self, master):
        self.master = master
        master.title("Python GUI Calculator")

        self.current_expression = ""
        self.input_text = tk.StringVar()

        input_frame = tk.Frame(master, bd=0, relief=tk.RIDGE, bg='light gray')
        input_frame.pack(expand=tk.YES, fill='both')

        self.input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'),
                                    textvariable=self.input_text, justify=tk.RIGHT, 
                                    bd=0, bg="#eee", cursor="arrow")
        self.input_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15)
        
        btns_frame = tk.Frame(master, bg='#ccc')
        btns_frame.pack(expand=tk.YES, fill='both')

        buttons = [
            ('C', 1, 0, 'red'), ('/', 1, 3, 'orange'),
            ('7', 2, 0, 'white'), ('8', 2, 1, 'white'), ('9', 2, 2, 'white'), ('*', 2, 3, 'orange'),
            ('4', 3, 0, 'white'), ('5', 3, 1, 'white'), ('6', 3, 2, 'white'), ('-', 3, 3, 'orange'),
            ('1', 4, 0, 'white'), ('2', 4, 1, 'white'), ('3', 4, 2, 'white'), ('+', 4, 3, 'orange'),
            ('0', 5, 0, 'white'), ('.', 5, 1, 'white'), ('=', 5, 2, 'green')
        ]
        
        row_val = 0
        for (text, row, col, color) in buttons:
            if col == 0:
                row_val += 1
            
            button = tk.Button(btns_frame, text=text, fg='black',
                               width=10, height=3, bd=0, bg=color,
                               font=('arial', 12, 'bold'),
                               command=lambda t=text: self.button_click(t))
            
            if text == '=':
                 button.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=1, pady=1)
            else:
                 button.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

        for i in range(5):
            btns_frame.grid_columnconfigure(i, weight=1)
            btns_frame.grid_rowconfigure(i, weight=1)

    def button_click(self, char):
        if char == 'C':
            self.current_expression = ""
            self.input_text.set("")
        elif char == '=':
            try:
                result = str(eval(self.current_expression))
                self.input_text.set(result)
                self.current_expression = result
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero!")
                self.current_expression = ""
                self.input_text.set("")
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
                self.current_expression = ""
                self.input_text.set("")
        else:
            self.current_expression += str(char)
            self.input_text.set(self.current_expression)

if __name__ == '__main__':
    root = tk.Tk()
    app = GUICalculator(root)
    root.mainloop()