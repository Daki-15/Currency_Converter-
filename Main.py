from tkinter import *
from forex_python.converter import CurrencyRates
from tkinter import ttk


window = Tk()
window.config(bg="#242424") # background color
window.geometry("400x500") # window size
window.title("Currency Converter") # window title
img = PhotoImage(file="./Images/icon.png") # create image object 
photo_label = Label(window,image=img, bg="#242424") # create label for image object
photo_label.place(x=0, y=0) # position on left corner of window
window.iconphoto(False, img) # add image object on window

# label
from_label = Label(window, text="From", font=("Arial 15 bold"), bg="#242424", fg="#EEEEEE")
to_label = Label(window, text="To", font=("Arial 15 bold"), bg="#242424", fg="#EEEEEE")
from_label.place(x=10, y=150)
to_label.place(x=248, y=150)


from_variable = StringVar()
to_variable = StringVar()


# Combobox creation
from_menu = ttk.Combobox(window, values=from_variable ,width = 10, textvariable = StringVar(window))
from_menu['values'] = ("IND", "USD", "CAD", "CNY", "EUR", "GBP", "RSD")
from_menu.place(x=10, y=180)
from_menu.current()

to_menu = ttk.Combobox(window, values = to_variable, width = 10, textvariable = StringVar(window))
to_menu['values'] = ("IND", "USD", "CAD", "CNY", "EUR", "GBP", "RSD")
to_menu.place(x=248, y=180)
to_menu.current()


amount_entry = Entry(window, font=("Arial 20 bold"), width=15, justify=CENTER)
amount_entry.place(x=70, y=240)

convert_button = Button(window, text="Convert", font=("Arial 20 bold"), fg="#EEEEEE", bg="#B0E0E6")
convert_button.place(x=100, y=300)


window.mainloop()