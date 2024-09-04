from tkinter import *
from tkinter import ttk

#colours
white = "#ffffff"
black = "#000000"
blue = "#191970"

window = Tk()
window.title("My Contacts")
window.geometry('700x700')
window.configure(background=white)
window.resizable(width=False, height=False)

# creating 3 frames
frame_up = Frame(window, width=700 , height=50, bg=blue)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(window, width=700 , height=150, bg=white)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(window, width=700 , height=100, bg=white)
frame_table.grid(row=2, column=0, columnspan=2, padx=0, pady=1)
# this divides the window into 3. You might not notice because the bg of some were white

#frame_up widgets
app_name = Label(frame_up, text="My Contacts", height=1, font=('Courier 17 bold'), bg=blue, fg=white)
app_name.place(x=5, y=5)

window.mainloop()