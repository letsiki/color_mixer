from tkinter import *
from color import Color

# import random
# def r():
#     return random.randint(0, 255)
# '#%02X%02X%02X' % (r(),r(),r())


def update_colors(event):
    color_left = Color(r1.get(), g1.get(), b1.get())
    canvas_left.config(bg=str(color_left))
    color_right = Color(r2.get(), g2.get(), b2.get())
    canvas_right.config(bg=str(color_right))
    color_bottom = color_left + color_right
    canvas_bottom.config(bg=str(color_bottom))


window = Tk()
window.title("Color Mixer")
window.config(padx=0, pady=0)

r1 = Scale(window, from_=0, to=255, orient=HORIZONTAL, command=update_colors)
g1 = Scale(window, from_=0, to=255, orient=HORIZONTAL, command=update_colors)
b1 = Scale(window, from_=0, to=255, orient=HORIZONTAL, command=update_colors)
r2 = Scale(window, from_=0, to=255, orient=HORIZONTAL, command=update_colors)
g2 = Scale(window, from_=0, to=255, orient=HORIZONTAL, command=update_colors)
b2 = Scale(window, from_=0, to=255, orient=HORIZONTAL, command=update_colors)
canvas_left = Canvas()
canvas_right = Canvas()
canvas_bottom = Canvas()
canvas_left.config(width=180, height=180)
canvas_right.config(width=180, height=180)
canvas_bottom.config(width=600, height=140)
r1.grid(column=1, row=1)
g1.grid(column=1, row=2)
b1.grid(column=1, row=3)
r2.grid(column=2, row=1)
g2.grid(column=2, row=2)
b2.grid(column=2, row=3)
canvas_left.grid(column=0, row=0, rowspan=4)
canvas_right.grid(column=3, row=0, rowspan=4)
canvas_bottom.grid(row=4, column=0, columnspan=4)
update_colors("")
window.mainloop()
