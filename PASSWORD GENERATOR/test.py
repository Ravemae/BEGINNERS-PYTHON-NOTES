import string
import random

small_letters = ''.join(random.sample(string.ascii_lowercase, 26))
capital_letters = ''.join(random.sample(string.ascii_uppercase, 26))
punctuation = ''.join(random.sample(string.punctuation, 10))
digits = ''.join(random.sample(string.digits, 9))
print("welcome to password generator")

user_name = input("what is your name")
user_input  = int(input("How many characters do you want your password to have: "))
combine_all_characters = list(small_letters + capital_letters + punctuation + digits)
random.shuffle(combine_all_characters)
real_password = combine_all_characters[:user_input]



print(''.join( real_password))



