alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
           "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
           "t", "u", "v", "w", "x", "y", "z"]

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:

        if char in alphabets:
            position = alphabets.index(char)
            new_postion = position + shift_amount
            end_text += alphabets[new_postion]
        else:
            end_text += char
    print(f"Here is the {cipher_direction}d result: {end_text}")
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message here: \n").lower()
    shift = int(input("Type your shift number:\n"))

    shift = shift % 26

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if restart == "no":
        should_end = True
        print("GoodBye")