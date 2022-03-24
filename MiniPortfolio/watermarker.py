# Basic program to add watermark text to an image.
# Use Up, Down, Left, Right arrow keys to move watermark text
# Press Enter to save image

# IMPORTS
from tkinter import *
from tkinter import simpledialog, messagebox, filedialog
from PIL import Image, ImageGrab
import os

# CONSTANTS
MAX_SIZE = 600
FONT_NAME = 'Helvetica'
FONT_SIZE = 15
MOVE_INCREMENT = 10

# SET UP tkinter WINDOW
window = Tk()
window.title("Watermarker by EJ")
window.config(padx=50, pady=50)


# MOVE WATERMARK TEXT ON SCREEN
def move_left(event):
    global watermark_x
    watermark_x -= MOVE_INCREMENT
    canvas.moveto(watermark, x=watermark_x, y=watermark_y)


def move_right(event):
    global watermark_x
    watermark_x += MOVE_INCREMENT
    canvas.moveto(watermark, x=watermark_x, y=watermark_y)


def move_up(event):
    global watermark_y
    watermark_y -= MOVE_INCREMENT
    canvas.moveto(watermark, x=watermark_x, y=watermark_y)


def move_down(event):
    global watermark_y
    watermark_y += MOVE_INCREMENT
    canvas.moveto(watermark, x=watermark_x, y=watermark_y)


def save_image(event):
    x = window.winfo_rootx() + canvas.winfo_x()
    y = window.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    ImageGrab.grab().crop((x, y, x1, y1)).save("watermarked.png")
    messagebox.showinfo(title="Success!", message="Your image has been saved as watermarked.png")


# BIND MOVEMENT FUNCTIONS WITH KEYS
window.bind('<Left>', move_left)
window.bind('<Right>', move_right)
window.bind('<Up>', move_up)
window.bind('<Down>', move_down)
window.bind('<Return>', save_image)

# Prompt to save watermark text
watermark_text = simpledialog.askstring(title='Watermark Text',
                                        prompt='Type out your watermark text:')

# Notify user that they will be uploading their image in the next step
messagebox.showinfo(title="Info",
                    message="For the next step, you will be selecting your image to upload.")

# Ask the user to select a single file name.
my_filetypes = [('image files', ['.jpg', '.png', '.gif'])]
uploaded_img = filedialog.askopenfilename(parent=window,
                                          initialdir=os.getcwd(),
                                          title="Please select a file:",
                                          filetypes=my_filetypes)

# RESIZE MAIN IMAGE
with Image.open(uploaded_img) as original:
    dim_ratio = original.width / original.height
    if original.width > original.height:
        width = MAX_SIZE
        height = round(MAX_SIZE / dim_ratio)
    elif original.width < original.height:
        height = MAX_SIZE
        width = round(MAX_SIZE * dim_ratio)
    else:
        width, height = MAX_SIZE, MAX_SIZE
    resized_img = original.resize((width, height))
    resized_img.save("image.png")

# ADD PHOTO TO CANVAS
canvas = Canvas(width=width, height=height)
img = PhotoImage(file='image.png')
canvas.create_image(width / 2, height / 2, image=img)
watermark_x = width / 2
watermark_y = height / 2
watermark = canvas.create_text(watermark_x, watermark_y,
                               text=watermark_text,
                               fill="white",
                               font=(FONT_NAME, FONT_SIZE))
canvas.pack()

# Let the user know how to move watermark text and save the image.
messagebox.showinfo(title="Info",
                    message="Use the arrow keys to move the watermark text\n"
                            "Press Enter to save the image")

window.mainloop()
