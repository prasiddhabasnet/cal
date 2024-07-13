from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save():
    website = web_entries.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:

            f = open("data.txt", "a")
            f.write(f"{website} | {email} | {password}")
            web_entries.delete(0, END)
            password_entry(0, END)





window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

#canvas weight
title_label = Label(text="Login")
title_label.grid(column=1, row=0)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=1)

#label
Website_label = Label(text="Website:")
Website_label.grid(row=2, column=0)

email_label = Label(text="Email/username:")
email_label.grid(row=3, column=0)
password_label = Label(text="password:")
password_label.grid(row=4, column=0)

#ENtries
web_entries = Entry(width=35)
web_entries.grid(row=2, column=1, columnspan=2)
web_entries.focus() #focus in the line
email_entry = Entry(width=35)
email_entry.grid(row=3, column=1)
email_entry.insert(0, "@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=4, column=1)


#Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=4, column=3)
add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=6, column=1)





window.mainloop()