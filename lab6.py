# Edley Forestal

def encode(password):
    final = ''
    for item in password:
        final += str((int(item) + 3) % 10)
    return final

def decode(password):
    final = ''

    for numbers in password:
        new_numbers = str((int(numbers) - 3) % 10)
        final += new_numbers
    return final

def main():
    quit = False
    encoded = ''
    original = ''
    while quit != True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        
        user = int(input("Please enter an option: "))
        
        if user == 1:
            original = input("Please enter your password to encode: ")
            encoded = encode(original)
            print("Your password has been encoded and stored!")
        elif user == 2:
            print(f"The encoded password is {encoded}, and the original password is {original}.")
        elif user == 3:
            break
        else:
            print("Hi")
            
if __name__ == "__main__":
    main()