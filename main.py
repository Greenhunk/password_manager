from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    # entry_password.insert(0, password)

    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Tanvir's Password_manager")
    window.config(padx=50, pady=50)

    canvas = Canvas(height=200, width=200)
    lock_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=lock_img)
    canvas.grid(row=0, column=1)

    label_website = Label(text="Website")
    label_website.grid(row=1, column=0)
    label_email = Label(text="Email/Username")
    label_email.grid(column=0, row=2)
    label_password = Label(text="Password")
    label_password.grid(column=0, row=3)

    entry_website = Entry(width=21)
    entry_website.grid(column=1, row=1)
    entry_website.focus()
    entry_email = Entry(width=35)
    entry_email.grid(column=1, row=2, columnspan=2)
    entry_password = Entry(width=21)
    entry_password.grid(column=1, row=3)

    button_password = Button(text="Generate Password", width=14, command=generate_password)
    button_password.grid(column=2, row=3)
    button_add = Button(text="Add", width=36, command=save)
    button_add.grid(column=1, row=4, columnspan=2)
    button_search = Button(text="Search", width=10, command=search)
    button_search.grid(column=2, row=1)

    window.mainloop()