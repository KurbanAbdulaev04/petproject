from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title('Калькулятор')


#логика калькулятора
def calc(key):
    global memory
    if key == '=':
        #исключаем написание букв
        strl = '-+1234567890.*/'
        if calc_entry.get()[0] not in strl:
            calc_entry.insert(END, 'Первый символ не число!')
            messagebox.showerror('Ошибка!', "Вы ввели не число!")
        #счет
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, '=' + str(result))
        except:
            calc_entry.insert(END, 'Ошибка!')
            messagebox.showerror('Ошибка!', 'Проверь правильность данных')
    #очистить поле
    elif key == 'C':
        calc_entry.delete(0, END)
    #смена
    elif key == '+/-':
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == '-':
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, '-')
        except IndexError:
            pass
    elif key == '**':
        calc_entry.insert(END, '**')
    else:
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)


# создаём кнопки
button_list = [
    '7', '8', '9', '+', '-',
    '4', '5', '6', '*', '/',
    '1', '2', '3', '+/-', '**',
    '00', '0', '.', 'C', '='
]
r = 2
c = 0

for i in button_list:
    rel = ''
    cmd = lambda x=i: calc(x)
    ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1

calc_entry = Entry(root, width=33)
calc_entry.grid(row=0, column=0, columnspan=5)

root.mainloop()
