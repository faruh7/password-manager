from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


def search_data():
    name_to_search = website_entry.get()
    try:
        with open('data.json', 'r') as file:
            some_kind_data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title=f"{name_to_search}", message="No Data File Found")
    else:
        if name_to_search in some_kind_data:
            data_to_show = some_kind_data[name_to_search]
            messagebox.showinfo(title=f"{name_to_search}", message=f"Email: {data_to_show['email']}\n"
                                                                   f"Password: {data_to_show['password']}")
        else:
            messagebox.showinfo(title=f"{name_to_search}", message="No details for the website exists")


def pass_generator():
    pass_generated.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    rand_letters = [choice(letters) for _ in range(randint(8, 10))]
    rand_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    rand_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = rand_letters + rand_symbols + rand_numbers

    shuffle(password_list)
    password = "".join(password_list)
    pass_generated.insert(END, string=f"{password}")
    pyperclip.copy(password)


def save_data():
    website_name = website_entry.get()
    user_name = user_entry.get()
    new_password = pass_generated.get()
    new_data = {
        website_name: {
            "email": user_name,
            "password": new_password,
        }
    }

    if len(website_name) == 0 or len(user_name) == 0 or len(new_password) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty!")
    else:
        try:
            with open('data.json', 'r') as file:
                some_data = json.load(file)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            some_data.update(new_data)
            with open('data.json', 'w') as file:
                json.dump(some_data, file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            user_entry.delete(0, 'end')
            pass_generated.delete(0, 'end')


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
# Entries
website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()
user_entry = Entry(width=52)
user_entry.grid(column=1, row=2, columnspan=2)
pass_generated = Entry(width=33)
pass_generated.grid(column=1, row=3)
# Buttons
search_button = Button(text="Search", width=14, command=search_data)
search_button.grid(column=2, row=1)
generate_button = Button(text="Generate Password", command=pass_generator)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=44, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
