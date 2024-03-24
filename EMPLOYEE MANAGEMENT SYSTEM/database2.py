from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("user_credentials")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS credentials(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)              
""")
conn.commit()
conn.close()
window = Tk()
def display_credentials():
    conn = sqlite3.connect("user_credentials.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM credentials" )
    data = cursor.fetchall()
    conn.close()

window.title("DATA BASE for Email and password management ")

email_label = Label(text="Email")
email_label.grid(row=0, column=0, padx=10, pady=10, sticky=S)
email_entry = Entry(window)
email_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = Label(text="Password")
password_label.grid(row=1,column=0, padx=10, pady=10, sticky=W)
password_entry = Entry(window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

save_button = Button(window, text="save credentials")
save_button.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

display_button = Button(text="Display credentials")
display_button.grid(row=3, column=1, columnspan=2, pady=10)

result_text = Text(window, height=10, width=40)
result_text.grid(row=4 ,column=0, columnspan=3, pady=10)
window.mainloop()