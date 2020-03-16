from tkinter import *
from tkinter import ttk
import urllib.request
import json
from tkinter import messagebox

root = Tk()
root.title('Currency converter')
root.geometry('300x250+1000+300')
root.resizable(False, False)

START_AMOUNT = 1000

def exchange():
	e_usd.delete(0, END)
	e_eur.delete(0, END)
	e_uah.delete(0, END)
	try:
		e_usd.insert(0, round(float(e_rur.get()) / float(currency_stat['USD']['Value']), 2))
		e_eur.insert(0, round(float(e_rur.get()) / float(currency_stat['EUR']['Value']), 2))
		e_uah.insert(0, round(float(e_rur.get()) / float(currency_stat['UAH']['Value']), 2))
	except:
		messagebox.showwarning('Error', 'Check entered value')

try:
	html = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js')
	data = html.read()
	JSON_object = json.loads(data)
	currency_stat = JSON_object['Valute']
except:
	messagebox.showerror('Error', 'External service is not available')
	root.destroy()

header_frame = Frame(root)
header_frame.pack(fill=X)
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)

# Header
h_currency = Label(header_frame, text='Currency', bg='#ccc', fg='#696969', font='Arial 12 bold')
h_currency.grid(row=0, column=0, sticky=EW)
h_value = Label(header_frame, text='Value', bg='#ccc', fg='#696969', font='Arial 12 bold')
h_value.grid(row=0, column=1, sticky=EW)

usd_currency = Label(header_frame, text='USD', font='Arial 10 bold')
usd_currency.grid(row=1, column=0, sticky=EW)
usd_value = Label(header_frame, text=currency_stat['USD']['Value'], font='Arial 10 bold')
usd_value.grid(row=1, column=1, sticky=EW)

eur_currency = Label(header_frame, text='EUR', font='Arial 10 bold')
eur_currency.grid(row=2, column=0, sticky=EW)
eur_value = Label(header_frame, text=currency_stat['EUR']['Value'], font='Arial 10 bold')
eur_value.grid(row=2, column=1, sticky=EW)

uah_currency = Label(header_frame, text='UAH', font='Arial 10 bold')
uah_currency.grid(row=3, column=0, sticky=EW)
uah_value = Label(header_frame, text=currency_stat['UAH']['Value'], font='Arial 10 bold')
uah_value.grid(row=3, column=1, sticky=EW)

# Calc frame
calc_frame = Frame(root, bg='#fff')
calc_frame.pack(expand=1, fill=BOTH)
calc_frame.grid_columnconfigure(1, weight=1)

l_rur = Label(calc_frame, text='RUR:', bg='#fff', fg='#696969', font='Arial 10 bold')
l_rur.grid(row=0, column=0, padx=10)
e_rur = ttk.Entry(calc_frame, justify=CENTER, font='Arial 10')
e_rur.grid(row=0, column=1, columnspan=2, pady=10, padx=10, sticky=EW)
e_rur.insert(0, START_AMOUNT)

btn_calc = ttk.Button(calc_frame, text='Exchange', command=exchange)
btn_calc.grid(row=1, column=1, columnspan=2, sticky=EW, padx=10)

# Result frame
res_frame = Frame(root)
res_frame.pack(expand=1, fill=BOTH, pady=5)
res_frame.grid_columnconfigure(1, weight=1)

# USD
l_usd = Label(res_frame, text='USD:', font='Arial 10 bold')
l_usd.grid(row=2, column=0)
e_usd = ttk.Entry(res_frame, justify=CENTER, font='Arial 10')
e_usd.grid(row=2, column=1, columnspan=2, padx=10, sticky=EW)
e_usd.insert(0, round(START_AMOUNT / float(currency_stat['USD']['Value']), 2))

# EUR
l_eur = Label(res_frame, text='EUR:', font='Arial 10 bold')
l_eur.grid(row=3, column=0)
e_eur = ttk.Entry(res_frame, justify=CENTER, font='Arial 10')
e_eur.grid(row=3, column=1, columnspan=2, padx=10, sticky=EW)
e_eur.insert(0, round(START_AMOUNT / float(currency_stat['EUR']['Value']), 2))

# UAH
l_uah = Label(res_frame, text='UAH:', font='Arial 10 bold')
l_uah.grid(row=4, column=0)
e_uah = ttk.Entry(res_frame, justify=CENTER, font='Arial 10')
e_uah.grid(row=4, column=1, columnspan=2, padx=10, sticky=EW)
e_uah.insert(0, round(START_AMOUNT / float(currency_stat['UAH']['Value']), 2))

root.mainloop()