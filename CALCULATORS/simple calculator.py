from tkinter import *
root = Tk()
root.title("Simple calculaotr")
v =Entry(root, width=35, borderwidth=5)
v.grid(row= 0, column=0, columnspan=3, padx=10, pady=10)


def button_click(real_number):
    current = v.get()
    v.delete(0,END)
    v.insert(0,str(current+ str(real_number)))
def clear():
    v.delete(0, END)
def add():
  first_number =v.get()
  global first_num
  global math 
  math="addition"
  first_num = int(first_number)
  v.delete(0, END)
def subtraction():
  first_number =v.get()
  global first_num
  global math 
  math="subtraction"
  first_num = int(first_number)
  v.delete(0, END)
def mulitiply():
   first_number =v.get()
   global first_num
   global math 
   math="multiplication"
   first_num = int(first_number)
   v.delete(0, END)
def division():
   first_number =v.get()
   global first_num
   global math 
   math="division"
   first_num = int(first_number)
   v.delete(0, END)

def equals():
   second_number = v.get()
   v.delete(0, END)
   if math =="addition":
      v.insert(0, first_num + int(second_number))
   elif math == "subtraction":
      v.insert(0,first_num - int(second_number))
   elif math =="multiplication":
      v.insert(0, first_num + int(second_number))
   elif math == "division":
      v.insert(0, first_num / int(second_number))
   
   pass
button_1 = Button(root, text="1", padx=40, pady=40, command= lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=40, command= lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=40, command= lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command= lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command= lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command= lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command= lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command= lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command= lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command= lambda: button_click(0))
button_add= Button(root, text="+", padx=40, pady=20, command=add)
button_subtract = Button(root, text="-", padx=40, pady=20, command=subtraction)
button_divide = Button(root, text="/", padx=40, pady=20, command=division)
button_multiply = Button(root , text="x", padx=40, pady=20, command=mulitiply)
button_equals = Button(root, text="=", padx=40, pady=40, command=equals) 
button_clear = Button(root, text="C", padx=40, pady=20, command=clear)



button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=2)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=0)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=1, column=1)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_clear.grid(row=4, column=0)
button_equals.grid(row=3, column=3)
button_divide.grid(row=4,column=1)
button_multiply.grid(row=4, column=2)
root.mainloop()
