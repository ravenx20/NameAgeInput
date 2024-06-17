"""This program is to let the user enter their name and their age."""

print("\nHello! have fun using this program! If you wish to quit the program, enter 'ctrl + Z'.\n")

try:
    while True:
        try:
            name = input("What is your name?\n")
            print("So your name is " + name.title() + ".\n")
            break
        except ValueError:
            print("Please enter your name in alphabets if there are any numbers in it.")
            continue
        

    while True:
        try:
            age = input("What is your age?\n")
            int(age)
            print("You are " + age + " then.\n")
            break
        except ValueError:
            print(age + " is not a number. Please try again.\n")
            continue

    year = 2024
    agestring = "You will turn 100 after " + str(100 - int(age)) + " years in the year \"" + str(2024 + 100 - int(age)) + "\".\n"

    if int(age) < 100:
        print(agestring)
    else:
        print("Wait.... You are so old!")

    while True:
        try:
            copy = int(input("Enter the number of copies of this message you want: "))
            print(copy * ("\n" + agestring))
            break
        except ValueError:
            print("You are not entering a number. Try again.")
            continue

except EOFError:
    print("You are exiting the program. Goodbye!")