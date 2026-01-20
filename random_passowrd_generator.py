import random

alphabate  = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
    "U", "V", "W", "X", "Y", "Z"
]

symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", 
    "-", "_", "+", "=", "{", "}", "|", "\\", 
    ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/",
    "~", "`"
]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]  # make numbers as strings

all_in_one = alphabate + symbols + numbers

while True:
    user_input = input("Enter the length of password: ").strip()
    
    if not user_input.isdigit():
        print("Please enter a number like 1, 2, 3 ...")
        continue
    
    length = int(user_input)

    password = "".join(random.choice(all_in_one) for _ in range(length))
    print(f"Your random password is ----> {password}")
    
    agin_input = input("Do you want to create a new password? (yes/no): ").strip().lower()
    if agin_input == "no":
        print("Thanks for using the random password generator 😊")
        break
