from tkinter import *
from tkinter import ttk
from view import *
from tkinter import messagebox

# colours
white = "#ffffff"
black = "#000000"
blue = "#191970"

window = Tk()
window.title("My Contacts")
window.geometry('700x700')
window.configure(background=white)
window.resizable(width=False, height=False)

# creating 3 frames
frame_up = Frame(window, width=700, height=50, bg=blue)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(window, width=700, height=200, bg=white)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(window, width=700, bg=white, relief="flat")
frame_table.grid(row=2, column=0, columnspan=2, padx=10, pady=1, sticky=NW)
# this divides the window into 3. You might not notice because the bg of some were white

window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(0, weight=1)


# functions
def show():
    global tree
    list_header = ["Name", "Gender", "Telephone", "Email"]

    demo_list = viewer()

    tree = ttk.Treeview(frame_table, selectmode="extended", columns=list_header, show='headings')

    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
    # vsb stands for vertical scrollbar
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)
    # hsb stands for horizontal scrollbar

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_table.grid_rowconfigure(0, weight=1)
    frame_table.grid_columnconfigure(0, weight=1)

    # tree head
    tree.heading(0, text='Name', anchor=NW)
    tree.heading(1, text='Gender', anchor=NW)
    tree.heading(2, text='Telephone', anchor=NW)
    tree.heading(3, text='Email', anchor=NW)

    # tree columns
    tree.column(0, width=200, anchor='nw')
    tree.column(1, width=180, anchor='nw')
    tree.column(2, width=150, anchor='nw')
    tree.column(3, width=150, anchor='nw')

    for item in demo_list:
        tree.insert('', 'end', values=item)



show()

def insert():
    Name = e_name.get()
    Gender = c_gender.get()
    Telephone = e_telephone.get()
    Email = e_email.get()

    data = [Name, Gender, Telephone, Email]

    if Name == '' or Gender == '' or Telephone == '' or Email == '':
        messagebox.showwarning('data','Please fill in all fields')
    else:
        add(data)
        messagebox.showinfo('data','Data added successfully')

        e_name.delete(0,'end')
        c_gender.delete(0, 'end')
        e_telephone.delete(0, 'end')
        e_email.delete(0, 'end')

        show()
# Adjust the grid configuration of frame_table to fill the entire space
frame_table.grid(row=2, column=0, sticky="nsew")

def to_update():
    try:
        tree_data = tree.focus() # gets data that user selects
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']

        Name = str(tree_list[0])
        Gender = str(tree_list[1])
        Telephone = str(tree_list[2])
        Email = str(tree_list[3])

        e_name.insert(0, Name)
        c_gender.insert(0, Gender)
        e_telephone.insert(0, Telephone)
        e_email.insert(0, Email)

        def  confirm():
            new_name = e_name.get()
            new_gender = c_gender.get()
            new_telephone = e_telephone.get()
            new_email = e_email.get()

            data = [new_telephone, new_name, new_gender,  new_telephone, new_email]
            update(data)

            messagebox.showinfo('Success', 'data updated successfully')

            e_name.delete(0, 'end')
            c_gender.delete(0, 'end')
            e_telephone.delete(0, 'end')
            e_email.delete(0, 'end')

            for widget in frame_table.winfo_children():
                widget.destroy() #destroying old data to show updated version

            b_confirm.destroy()

            show()
        b_confirm = Button(frame_down, text="Confirm", width=10, height=1, bg=blue, font=('Ivy 8 bold'), fg=white, command=confirm)
        b_confirm.place(x=230, y=110)
    except IndexError:
        messagebox.showerror('Error', 'Select one of them from the table')
# Configure the treeview to fill the entire frame_table
tree.grid(row=0, column=0, sticky="nsew")
tree.rowconfigure(0, weight=1)
tree.columnconfigure(0, weight=1)

def to_remove():
    try:
        tree_data = tree.focus()  # gets data that user selects
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']
        tree_telephone = str(tree_list[2])

        remove(tree_telephone)
        messagebox.showinfo('success', "Data has been deleted successfully")

        for widget in frame_table.winfo_children():
            widget.destroy()  # destroying old data to show updated version
        show()
    except IndexError:
        messagebox.showerror('Error', 'Select one of them from the table')

def to_search():
    telephone = e_search.get()
    data = search(telephone)

    def delete_command():
        tree.delete(*tree.get_children())
    delete_command()
    for item in data:
        tree.insert('','end',values=item)
    e_search.delete(0,'end')
# frame_up widgets
app_name = Label(frame_up, text="My Contacts", height=1, font=('Courier 17 bold'), bg=blue, fg=white)
app_name.place(x=5, y=5)

# frame_down widgets
l_name = Label(frame_down, text="Name:", width=20, height=1, font=('Ivy 10'), bg=white, anchor=NW)
l_name.place(x=10, y=15)
e_name = Entry(frame_down, width=25, justify='left', highlightthickness=1,
               relief="solid")  # creating entry where your name would be entered
e_name.place(x=80, y=15)

l_gender = Label(frame_down, text="Gender:", width=20, height=1, font=('Ivy 10'), bg=white, anchor=NW)
l_gender.place(x=10, y=53)
c_gender = ttk.Combobox(frame_down, width=24)  # creating entry where your gender would be entered
c_gender['values'] = ['Female', 'Male']
c_gender.place(x=80, y=53)

l_telephone = Label(frame_down, text="Telephone:", height=1, font=('Ivy 10'), bg=white, anchor=NW)
l_telephone.place(x=10, y=87)
e_telephone = Entry(frame_down, justify='left', highlightthickness=1, width=25,
                    relief="solid")  # creating entry where your name would be entered
e_telephone.place(x=100, y=87)

l_email = Label(frame_down, text="Email:", height=1, font=('Ivy 10'), bg=white, anchor=NW)
l_email.place(x=10, y=122)
e_email = Entry(frame_down, justify='left', highlightthickness=1, width=25, relief="solid")  # creating entry where
# your name would be entered
e_email.place(x=100, y=122)

b_search = Button(frame_down, text="Search", height=1, bg=blue, font=('Ivy 8 bold'), fg=white,command=to_search)
b_search.place(x=400, y=15)  # creating a search button
e_search = Entry(frame_down, width=16, justify="left", font=("Ivy 11"), highlightthickness=1, relief="solid")
e_search.place(x=500, y=15)  # creating an entry for search

b_view = Button(frame_down, text="View", width=10, height=1, bg=blue, font=('Ivy 8 bold'), fg=white,command=show)
b_view.place(x=400, y=52)  # creating a view button

b_add = Button(frame_down, text="Add", width=10, height=1, bg=blue, font=('Ivy 8 bold'), fg=white, command=insert)
b_add.place(x=550, y=52)  # creating an add button

b_update = Button(frame_down, text="Update", width=10, height=1, bg=blue, font=('Ivy 8 bold'), fg=white, command=to_update)
b_update.place(x=550, y=90)  # creating an update button

b_delete = Button(frame_down, text="Delete", width=10, height=1, bg=blue, font=('Ivy 8 bold'), fg=white, command= to_remove)
b_delete.place(x=550, y=126)  # creating a delete button

window.mainloop()
