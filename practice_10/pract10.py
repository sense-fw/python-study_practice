import tkinter as tk
from tkinter import ttk, messagebox, filedialog

root = tk.Tk()
root.title('Шарова Дарья Сергеевна')

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both', padx=10, pady=10)

# ------------------ Вкладка 1: Калькулятор ------------------
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Калькулятор')

num1_var = tk.StringVar()
num2_var = tk.StringVar()
op_var = tk.StringVar(value='+')

tk.Label(tab1, text='Число 1:').grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(tab1, textvariable=num1_var)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(tab1, text='Число 2:').grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(tab1, textvariable=num2_var)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

tk.Label(tab1, text='Операция:').grid(row=2, column=0, padx=5, pady=5)
combobox_op = ttk.Combobox(tab1, textvariable=op_var, values=['+', '-', '*', '/'])
combobox_op.grid(row=2, column=1, padx=5, pady=5)

def calculate():
    try:
        a = float(num1_var.get())
        b = float(num2_var.get())
        op = op_var.get()
        if op == '+':
            res = a + b
        elif op == '-':
            res = a - b
        elif op == '*':
            res = a * b
        elif op == '/':
            res = a / b
        else:
            res = 'Ошибка'
        messagebox.showinfo('Результат', f'Результат: {res}')
    except Exception as e:
        messagebox.showerror('Ошибка', f'Неверные данные: {e}')

def clear_calculator():
    num1_var.set('')
    num2_var.set('')
    op_var.set('+')

tk.Button(tab1, text='Вычислить', command=calculate).grid(row=3, column=0, pady=10)
tk.Button(tab1, text='Очистить', command=clear_calculator).grid(row=3, column=1, pady=10)

# ------------------ Вкладка 2: Чекбоксы ------------------
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Чекбоксы')

cb1_var = tk.BooleanVar()
cb2_var = tk.BooleanVar()
cb3_var = tk.BooleanVar()

cb1 = tk.Checkbutton(tab2, text='Первый', variable=cb1_var)
cb1.pack(pady=5)
cb2 = tk.Checkbutton(tab2, text='Второй', variable=cb2_var)
cb2.pack(pady=5)
cb3 = tk.Checkbutton(tab2, text='Третий', variable=cb3_var)
cb3.pack(pady=5)

def show_selection():
    selected = []
    if cb1_var.get(): selected.append('первый')
    if cb2_var.get(): selected.append('второй')
    if cb3_var.get(): selected.append('третий')
    if selected:
        messagebox.showinfo('Выбор', f'Вы выбрали: {", ".join(selected)}')
    else:
        messagebox.showinfo('Выбор', 'Вы ничего не выбрали')

def clear_checkboxes():
    cb1_var.set(False)
    cb2_var.set(False)
    cb3_var.set(False)

tk.Button(tab2, text='Показать выбор', command=show_selection).pack(pady=5)
tk.Button(tab2, text='Очистить', command=clear_checkboxes).pack(pady=5)

# ------------------ Вкладка 3: Работа с текстом ------------------
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text='Текст')

text_box = tk.Text(tab3, wrap='word')
text_box.pack(expand=True, fill='both', padx=5, pady=5)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, content)

def clear_text():
    text_box.delete(1.0, tk.END)

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Открыть текстовый файл', command=open_file)
menu_bar.add_cascade(label='Файл', menu=file_menu)
root.config(menu=menu_bar)

tk.Button(tab3, text='Очистить текст', command=clear_text).pack(pady=5)

root.mainloop()