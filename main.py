from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests

def get_html(url):
    # делаем запрос по адресу
    html_content = requests.get(url)
    # получаем содержание
    return html_content.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    t = soup.find('div', class_= "chart__subtitle js-chart-value")
    t.span.decompose()  # убираем вложенный div
    return t.text


def main():
    txt.delete(0, "end")
    url = 'https://www.rbc.ru/crypto/currency/xmrusd'
    res = get_html(url)
    print(get_data(res))
    ddd = get_data(res)

    '''txt.insert(0, get_data(res))'''



def zn():
    x = txt.get()
    if not x.isdigit():
        messagebox.showinfo('Ошибка', 'Текст')
    txt1.delete(0, END)

    if var.get() == 0:
        res = float(x) * 50
    elif var.get() == 1:
        res = float(x) * 90
    main()

    txt1.insert(0, str(round(res, 2)))


window = Tk()
window.geometry('500x350')
window.title("Конвертер")
lbl = Label(window, text="<-<-*Конвертатор*->->", font=("Monaco", 28))
lbl.grid(column=0, row=0)
lbl.place(relx=.5, rely=.07, anchor='c')

text = Label(window, text="Кол-во валюты", font=("Monaco", 13))
text.grid(column=0, row=0)
text.place(relx=.15, rely=.5, anchor='c')

text1 = Label(window, text="Кол-во валюты", font=("Monaco", 13))
text1.grid(column=0, row=0)
text1.place(relx=.85, rely=.5, anchor='c')

txt = Entry(window, width=20, bd=2, relief=GROOVE)
txt.grid(column=1, row=0)
txt.place(relx=.15, rely=.4, anchor='c')

txt1 = Entry(window, width=20, bd=2, relief=GROOVE)
txt1.grid(column=1, row=0)
txt1.place(relx=.85, rely=.4, anchor='c')

btn = Button(window, text="Перевести", command=zn, width=12, font=("Monaco", 11), relief=GROOVE)
btn.grid(column=1, row=0)
btn.place(relx=.5, rely=.4, anchor='c')

var = IntVar()
rad1 = Radiobutton(window, text='dollar', variable=var, value=0, font=("Monaco", 11))
rad2 = Radiobutton(window, text='Евро', variable=var, value=1, font=("Monaco", 11))
rad1.place(relx=.5, rely=.7, anchor='c')
rad2.place(relx=.5, rely=.6, anchor='c')

window.mainloop()