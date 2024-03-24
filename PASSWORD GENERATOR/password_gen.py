import string as s
import random as r
    
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
    return shuffled_password
   # print(shuffled_password)



def user():
    password = generate_password()
    print("welcoome to password generator. Please press enter to continue")
    user_firstname  = input("what is your first name")
    user_lastname = input ("what is your last name ")
    user_name = input("what is your preferred username")
    Age = int(input("how old are you"))
    country = input("what country are you from")
    
    
    print(f"{user_name}, this is your password ",password )
    
    print("User saved")
user()

