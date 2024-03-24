import string
import random

small_letters = ''.join(random.sample(string.ascii_lowercase, 26))
capital_letters = ''.join(random.sample(string.ascii_uppercase, 26))
punctuation = ''.join(random.sample(string.punctuation, 10))
digits = ''.join(random.sample(string.digits, 9))

user_input = int(input("How many characters do you want your password to have: "))
combine_all_characters = list(small_letters + capital_letters + punctuation + digits)
random.shuffle(combine_all_characters)

# Check if the desired length is greater than the length of the combined characters
if user_input > len(combine_all_characters):
    print("Error: Desired length exceeds the available characters.")
else:
    # Trim the list to the desired length
    final_password = combine_all_characters[:user_input]
    print(''.join(final_password))

#
    