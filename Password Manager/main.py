from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(10, 14)]
    password_symbols = [choice(symbols) for _ in range(2, 4)]
    password_numbers= [choice(numbers) for _ in range(2, 4)]

    password_list = password_numbers + password_letters + password_symbols

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

    # password = ""
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    get_password = password_entry.get()

    if len(website) <= 2 or len(get_password) == 0:
        messagebox.showinfo(title="oops", message="Please make sure you haven't omitted any field")

    is_ok = messagebox.askokcancel(title=website, message= f"These are the details entered:\nEmail: {email}"
                                   f"\nPassword : {password} \nIs it okay to save?")

    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} || {email} || {password}\n")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=20)


canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row =0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

gen_password = Button(text="Generate Password", command=generate_password)
gen_password.grid(column=2, row=3)

add_button= Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

#Entries

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "jluch@gmail.com")  # pre-populated with a default email
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)







window.mainloop()
