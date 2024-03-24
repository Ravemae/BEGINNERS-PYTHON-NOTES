#Project calculator using def()
#call add fintion

def add():
  x = int(input("Please input the first number: "))
  y = int(input("input the second number: "))
  results = f"the results of your request {x+y}"
  print(results)
  print("thank you for calculating  with us")
  return results

def subtraction():
  x = int(input("Please input the first number:"))
  y = int(input("input the second number: "))
  results = f"the results of your request {x-y}"
  print(results)
  print("thank you for calculating  with us")
  return results

def division():
  x = int(input("Please input the first number: "))
  y = int(input("input the second number: "))
  results = f"the results of your request {x/y}"
  print(results)
  print("thank you for calculating  with us")
  return results

def multiplication():
  x = int(input(("Please input the first number: ")))
  y = int(input("input the second number: "))
  results = f"the results of your request {x*y}"
  print(results)
  print("thank you for calculating  with us")
  return results
#first define functions

def select_option():
  print("Hello there welcome to project calculator")
  option = input("please select your operation \n1. addition\n2. subtraction\n3. divsion \n4. multiplication\n")
  
  if option == "addition" or option == "1":
    add()
  elif option == "subtraction" or option == "2":
    subtraction()

  elif option == "divsion" or option == "3":
    division()
  elif option == "multiplication" or option =="4": 
    multiplication()
  else:
    print("pls inpout a valid option")
    more_operation = input("do you want to perform another operation: ")
    if more_operation == "yeah" or more_operation == "yes" or more_operation == "sure":
      select_option()
    else:
      print("hope to see you next time")
      
    return select_option