#dated 2-24-24 i will be making a calculator with tkinter 
from tkinter import *

window = Tk()
window.title("Vera Calculator")
window.config(padx=20, pady=100)
#now i want to make an entry space that the user's action will be displayed

entry = Entry(width=40, justify=RIGHT, )

entry.grid(row=0, column=0)
# giving a function to add the numbers the entry box 


numbers = [0,1,2,3,4,5,6,7,8,9]

signs = ['+','-','/','*']

def number_one():
    entry.insert(0,numbers[1])
def number_two():
    entry.insert(0,numbers[2])
def number_three():
    entry.insert(0,numbers[3])
def number_four():
    entry.insert(0,numbers[4])
def number_five():
    entry.insert(0,numbers[5])
def number_six():
    entry.insert(0,numbers[6])
def number_seven():
    entry.insert(0,numbers[7])
def number_eight():
    entry.insert(0,numbers[8])
def number_nine():
    entry.insert(0,numbers[9])   

def add():
    entry.insert(0,signs[0])
    first = entry.get()

    second = entry.get()
    print(first)
    
    
    
    entry.delete(0,END)
    
def equals():
    second = list(entry.get())
    int(second.pop[0])
    david = first + second
    print(david)  



def minus():
    entry.insert(0,signs[1])
def multiply():
    entry.insert(0,signs[3])
def divide():
    entry.insert(0,signs[2])


    


#Now that the entry is being made i want to i want to make buttons for each digits
one = Button(text="1", width=30, cursor="hand2", command=number_one)
one.grid(row=1,column=0)

two = Button(text="2", width=30,cursor="hand2", command=number_two )
two.grid(row=1,column=1)

three = Button(text="3", width=30,cursor="hand2", command=number_three)
three.grid(row=1,column=2)

four = Button(text="4", width=30,cursor="hand2", command=number_four)
four.grid(row=2,column=0)

five = Button(text="5", width=30, cursor="hand2",command=number_five)
five.grid(row=2,column=1)

six = Button(text="6", width=30,cursor="hand2", command=number_six)
six.grid(row=2,column=2)

seven = Button(text="7", width=30,cursor="hand2", command=number_seven)
seven.grid(row=3,column=0)

eight = Button(text="8", width=30,cursor="hand2", command=number_eight)
eight.grid(row=3,column=1)

nine = Button(text="9", width=30,cursor="hand2", command=number_nine)
nine.grid(row=3,column=2)

zero = Button(text="0", width=30,cursor="hand2")
zero.grid(row=4, column=0)




#now that i have called the numbers i will now call the signs the like sof + - * /

plus_sign = Button(text="+", width=10 , command=add)
plus_sign.grid(row=1,column=3)

minus_sign = Button(text="-", width=10)
minus_sign.grid(row=2, column=3)

mult_sign = Button(text="x", width=10)
mult_sign.grid(row=3, column=3)

division = Button(text="/", width=10)
division.grid(row=4, column=1)

clear = Button(text="C", width=10, )
clear.grid(row=4, column=2) 
first = entry.get()

second = entry.get()

#ABANDONED
window.mainloop()