from tkinter import *
import tkinter.messagebox as mb
from conversionInfo import *

window = Tk()
window.title("Metric to Imperial Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)


def update_display(*args):
    direction = radio_state.get()
    option = menu_state.get()

    if direction == "i2m":
        from_unit.config(text=data[option]["imperial"])
        to_unit.config(text=data[option]["metric"])
    else:
        from_unit.config(text=data[option]["metric"])
        to_unit.config(text=data[option]["imperial"])
    to_value.config(text="X")


def calculate():
    direction = radio_state.get()
    option = menu_state.get()
    start_value = from_value.get()

    try:
        start_value = int(from_value.get())
    except ValueError:
        mb.showerror("Advice from EJ", "Type a number, silly!")


    value = str(round(data[option][direction](start_value), 2))
    to_value.config(text=value)


# TODO: Dropdown menu for conversion options
conversion_options = list(data.keys())
menu_state = StringVar()
menu_state.set(conversion_options[0])

menu = OptionMenu(
    window,
    menu_state,
    *conversion_options,
    command=update_display)
menu.grid(row=0, column=0, columnspan=5)
menu.config(width=15)

# TODO: Radio buttons dictating conversion direction
radio_state = StringVar()
radio_state.set("m2i")

m2i = Radiobutton(
    text="To Imperial",
    value="m2i",
    variable=radio_state,
    command=update_display)
m2i.grid(row=1, column=0, columnspan=2)

i2m = Radiobutton(
    text="To Metric",
    value="i2m",
    variable=radio_state,
    command=update_display)
i2m.grid(row=1, column=3, columnspan=2)

# TODO: Input boxes for FROM value
from_value = Entry()
from_value["width"] = 5
from_value.grid(row=2, column=0)

# TODO: Text field for FROM unit
from_unit = Label(text="km")
from_unit.grid(row=2, column=1)

# TODO: =
equals = Label(text="=")
equals.grid(row=2, column=2)
equals.config(pady=20)

# TODO: Input boxes for TO value
to_value = Label(text="X")
to_value["width"] = 5
to_value.grid(row=2, column=3)

# TODO: Text field for TO unit
to_unit = Label(text="miles", justify="left")
to_unit.grid(row=2, column=4)

# TODO: Calculate Button
button = Button(text=" calculate ", command=calculate)
button.grid(row=3, column=1, columnspan=3)


window.mainloop()
