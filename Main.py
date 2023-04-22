# Import necessary modules
from tkinter import *
from forex_python.converter import CurrencyRates
from tkinter import ttk

# Create a tkinter window object
window = Tk()

# Configure the window with a background color, size, and title
window.config(bg="#242424")
window.geometry("400x450")
window.title("Currency Converter")

# Create an image object and label for the program icon
img = PhotoImage(file="./Images/icon.png")
photo_label = Label(window,image=img, bg="#242424")
photo_label.place(x=0, y=0)
window.iconphoto(False, img)

# Create labels for "From" and "To" currencies and set their positions
from_label = Label(window, text="From", font=("Arial 15 bold"), bg="#242424", fg="#EEEEEE")
to_label = Label(window, text="To", font=("Arial 15 bold"), bg="#242424", fg="#EEEEEE")
from_label.place(x=10, y=150)
to_label.place(x=248, y=150)

# Create StringVar objects to store the selected currencies
from_variable = StringVar()
to_variable = StringVar()

# Create comboboxes for selecting the "From" and "To" currencies and set their positions
from_menu = ttk.Combobox(window, values=["USD", "EUR", "GBP", "CHF", "CAD", "ZAR", "HKD"], width=10, textvariable=from_variable)
from_menu.place(x=10, y=180)
from_menu.current(0)

to_menu = ttk.Combobox(window, values=["USD", "EUR", "GBP", "CHF", "CAD", "ZAR", "HKD"], width=10, textvariable=to_variable)
to_menu.place(x=248, y=180)
to_menu.current(0)

# Create an entry widget for entering the amount to convert
amount_entry = Entry(window, font=("Arial 20 bold"), width=15, justify=CENTER)
amount_entry.place(x=70, y=240)

# Create a StringVar object to store the converted amount and a function to convert the currency
txt = StringVar()

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
        result_label = Label(window, textvariable=txt, font=("Arial 20 bold"))
        result_label.place(x=125, y=400)
    # If no amount was entered, display an error message
    else:
        txt.set("Please enter an amount")

# Create a function to reset the amount and converted amount
def reset():
    amount_entry.delete(0, END)
    txt.set("")

# Create buttons for converting and resetting and set their positions
convert_button = Button(window, command=convert, text="Convert", font=("Arial 20 bold"), fg="#EEEEEE", bg="#B0E0E6", width=7)
convert_button.place(x=60, y=300)

reset_button = Button(window, command=reset, text="Reset", font=("Arial 20 bold"), fg="#EEEEEE", bg="#B0E0E6", width=7)
reset_button.place(x=200, y=300)

# Start
#The mainloop() function runs the application window
window.mainloop()