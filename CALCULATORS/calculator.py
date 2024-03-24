import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(screen_var.get())
            screen_var.set(str(result))
        except Exception as e:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

root = tk.Tk()
root.title("Calculator")

# Variable to hold the input and result
screen_var = tk.StringVar()

# Entry widget to display input and results
screen = tk.Entry(root, textvar=screen_var, font=("Helvetica", 18))
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10, sticky="nsew")

# Button labels
button_labels = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

# Create and place buttons
row_val = 1
col_val = 0
for button_label in button_labels:
    button = tk.Button(root, text=button_label, padx=20, pady=20, font=("Helvetica", 18))
    button.grid(row=row_val, column=col_val, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")
    button.bind("<Button-1>", on_button_click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure rows and columns to expand with the window
for i in range(4):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
