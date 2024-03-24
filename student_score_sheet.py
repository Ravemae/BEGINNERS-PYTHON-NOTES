#create a program that checks a student score if students enter 70 it should print


# print("Hello there welcome to Results Checker")
# scores = int(input("Plase enter your results "))
# try:
#    if scores in range(0,39):
#       print("Unknown Results")
#    elif scores in range(40, 59):
#       print("Fail")
#    elif scores in range(50, 69):
#       print("D")
#    elif scores in range(70, 79):
#       print("C")
#    elif scores in range(80, 89):
#       print("B")
#    elif scores in range(90, 100):
#       print("A")


a = int(input("input the first number: "))
b = int(input("input the second number: "))
c = int(input("input the third number: "))

if a>b>c:
    print("the first number is the greater number: ")
if b>a>c:
    print(" the second number is the greater number")
if c>b>a:
    print("C is the greater number")