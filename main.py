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

frame_table = Frame(window, width=700 , height=100, bg=blue)
frame_table.grid(row=2, column=0, columnspan=2, padx=0, pady=1)
# this divides the window into 3. You might not notice because the bg of some were white

#frame_up widgets
app_name = Label(frame_up, text="My Contacts", height=1, font=('Courier 17 bold'), bg=blue, fg=white)
app_name.place(x=5, y=5)

# frame_down widgets
l_name = Label(frame_down, text="Name:", width=20, height=1, font=('Ivy 10'), bg=white, anchor=NW )
l_name.place(x=10, y=15)
e_name = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid") # creating entry where your name would be entered
e_name.place(x=80,y=15)

l_gender = Label(frame_down, text="Gender:", width=20, height=1, font=('Ivy 10'), bg=white, anchor=NW )
l_gender.place(x=10, y=53)
c_gender = ttk.Combobox(frame_down, width=27) # creating entry where your gender would be entered
c_gender['values'] = ['Female', 'Male']
c_gender.place(x=80,y=53)

l_telephone = Label(frame_down, text="Telephone:", height=1, font=('Ivy 10'), bg=white, anchor=NW )
l_telephone.place(x=10, y=87)
e_telephone = Entry(frame_down, justify='left', highlightthickness=1, width=25, relief="solid") # creating entry where your name would be entered
e_telephone.place(x=100,y=87)

l_email = Label(frame_down, text="Email:", height=1, font=('Ivy 10'), bg=white, anchor=NW )
l_email.place(x=10, y=122)
e_email = Entry(frame_down, justify='left', highlightthickness=1, width=25, relief="solid") # creating entry where your name would be entered
e_email.place(x=100,y=122)


window.mainloop()