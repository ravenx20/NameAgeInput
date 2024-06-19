"""This is a program that lets us know the divisor of the number input by the user"""
print("Welcome to the divisor finder program! We will find out the divisor of the input! Please enter 'ctrl + z' to exit the program.")
innum = int(input("Enter a number: "))
resultlist = []

for num in range(1,innum + 1):
    if innum % num == 0:
        resultlist.append(num)

print(f"The divisors of the input number are : {resultlist}")