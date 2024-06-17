"""Writing a list of numbers that are less than a certain number from the given list"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

print("In this program, we are going to get numbers less than 5 from the given list of 'a' into the new list of 'b'.")
for number in a:
    if number < 5:
        b.append(number)

print(b)

print([num for num in a if num < 5]) 

#asking the user to input a number for the condition that collects the numbers from 'a' which are less than the input number into a list
usernum = int(input("Enter a number to check: "))
c = [numberr for numberr in a if numberr < usernum]
print(c)