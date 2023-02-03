
import random
from tkinter import *

from tkinter import  messagebox
from random import randint, choice, shuffle
import tkinter as tk


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '.', '<', '>', '/', '?']


# Number of letters
def passwordGenerator():
    nr_letter = randint(8, 10)
    # Number of Symbols
    nr_symbols = randint(2, 4)
    # Number of Numbers
    nr_numbers = randint(2, 4)

    password_letter = [choice(letters) for _ in range(nr_letter)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letter + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)


def save():
    password = password_entry.get()
    email = email_entry.get()
    website = website_entry.get()
    if len(password) == 0 or len(website) == 0:
        messagebox.showwarning("Please some field is empty ")
    else:
        messagebox.askokcancel("Did you want to save")

window = tk.Tk()
window.title("Password Manager")
window.config(padx=70, pady=70)

canvas = Canvas(height=200, width=200)
log_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=log_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=36)
email_entry.grid(row=2, column=1,  columnspan=2)
email_entry.insert(0, "Thoravgs4@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=passwordGenerator)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36,command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()

