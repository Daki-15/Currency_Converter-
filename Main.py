# Import necessary modules
from tkinter import *
from forex_python.converter import CurrencyRates
from tkinter import ttk
from design import configure_the_window, from_to_labels

# Create a tkinter window object
window = Tk()
# Create StringVar objects to store the selected currencies
from_variable = StringVar()
to_variable = StringVar()
# Create a StringVar object to store the converted amount and a function to convert the currency
txt = StringVar()
# font, font size and type of text used for text
font_size_type = "Arial 20 bold"
currency_list = ["USD", "EUR", "GBP", "CHF", "CAD", "ZAR", "HKD"]

# Configure the window with a background color, size, and title
configure_the_window(window)

# Labels for "From" and "To" currencies
from_to_labels(window, font_size_type)

# Create an image object and label for the program icon
img = PhotoImage(file="./Images/icon.png")
Label(window,image=img, bg="#242424").place(x=0, y=0)
window.iconphoto(False, img)

# Create comboboxes for selecting the "From" and "To" currencies and set their positions
from_menu = ttk.Combobox(window, values = currency_list, width=10, textvariable=from_variable)
from_menu.place(x=10, y=180)
from_menu.current(0)

to_menu = ttk.Combobox(window, values=currency_list, width=10, textvariable=to_variable)
to_menu.place(x=248, y=180)
to_menu.current(0)

# Create an entry widget for entering the amount to convert
amount_entry = Entry(window, font=(font_size_type), width=15, justify=CENTER)
amount_entry.place(x=70, y=240)


def convert():
    # Get the selected currencies and create a CurrencyRates object
    from_currency = from_variable.get()
    to_currency = to_variable.get()
    curent = CurrencyRates()

    # Check if an amount was entered, convert it, and display the result
    if amount_entry.get():
        ans = curent.convert(from_currency, to_currency, float(amount_entry.get()))
        amount = float("{:.3f}".format(ans))
        txt.set(amount)
        result_label = Label(window, textvariable=txt, font=(font_size_type), bg="#242424", fg="#EEEEEE")
        result_label.place(x=125, y=400)
    # If no amount was entered, display an error message
    else:
        txt.set("Please enter an amount")

# Create a function to reset the amount and converted amount
def reset():
    amount_entry.delete(0, END)
    txt.set("")

# Create buttons for converting and resetting and set their positions
convert_button = Button(window, command=convert, text="Convert", font=(font_size_type), fg="#EEEEEE", bg="#0C5243", width=7)
convert_button.place(x=60, y=300)

reset_button = Button(window, command=reset, text="Reset", font=(font_size_type), fg="#EEEEEE", bg="#47177B", width=7)
reset_button.place(x=200, y=300)

# Start
#The mainloop() function runs the application window
window.mainloop()