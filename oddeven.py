"""This program lets the user to enter a number that he wants to know whether even or odd"""

print("Welcome to the program! Have fun using it! Enter \"ctrl + z\" to quit the program.\n")
try:
    while True:
        try:
            num = int(input("Enter the number to be divided: "))
            if num % 2 == 0:
                print("This number is even.")
                if num % 4 == 0:
                    print('Wow! This is also divisible by 4!')
            else:
                print("This number is odd.")

            check = int(input("Enter another number to divide by: "))
            if num % check == 0:
                print(f"{num} is divisible by {check}!")
            else:
                print(f"{num} is not divisible by {check}. What a shame...")
            break
        except ValueError:
            print("This is not a number!")
            continue
except EOFError:
    print("Goodbye!")

