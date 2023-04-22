from tkinter import *

# Configure the window with a background color, size, and title
def configure_the_window(window):
    window.config(bg="#242424")
    window.geometry("400x450")
    window.title("Currency Converter")

# Create labels for "From" and "To" currencies and set their positions
def from_to_labels(window, font_size_type):
    Label(window, text="From", font=(font_size_type), bg="#242424", fg="#EEEEEE").place(x=10, y=150)
    Label(window, text="To", font=(font_size_type), bg="#242424", fg="#EEEEEE").place(x=248, y=150)