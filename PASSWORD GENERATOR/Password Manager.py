from tkinter import *
import random as r
import string as s
from tkinter import messagebox

def generate_password():
    upper_letters = s.ascii_uppercase
    lower_letters = s.ascii_lowercase
    punctuation = s.punctuation
    numbers = s.digits
    first_letter = ''.join(r.sample(upper_letters, 4))
    second_letter = ''.join(r.sample(lower_letters, 3))
    comma = ''.join(r.sample(punctuation, 4))
    third_value = ''.join(r.sample(numbers ,3))

    all_values = first_letter + second_letter + comma +third_value

    password = list(all_values)
    r.shuffle(password)
    #print(password)

    # Print the shuffled password (convert list back to string)
    shuffled_password = ''.join(password)
    password_entry.insert(0,shuffled_password)

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) ==0 or len(email)==0 or len(password)==0:
        messagebox.showerror(text="oops", message= "pls fill in the fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"please confirm the details entered email: {email}, \n password {password} press okay to continue ")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website}|{email}|{password}")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)



website_label = Label(text="Website: ")
website_label.grid(row=1,column=0)
email_label = Label(text="Email: ")
email_label.grid(row=2,column=0)
password_label = Label(text= "password")
password_label.grid(row=3,column=0)


website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)

password_entry = Entry(width=35)
password_entry.grid(row=3,column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3,column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1,columnspan=2)
window.mainloop()