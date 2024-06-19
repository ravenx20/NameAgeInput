"This is a program that returns a list of elements that return common ones from both lists."
#Importing random for the future uses
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = []
# for mem in b:
#     if mem in a:
#         result.append(mem)

# print(f"The list of elements that are common for both given lists: {result}.")

#Generating two random lists
#reference method taken from https://www.geeksforgeeks.org/generating-random-number-list-in-python/

rand_list1 = []
rand_list2 = []
n1 = random.randint(1,8)
n2 = random.randint(1,13)

for rmem1 in range(n1):
    rand_list1.append(random.randint(1,20))

for rmem2 in range(n2):
    rand_list2.append(random.randint(1,20))

for memran in rand_list2:
    if memran in rand_list1:
        result.append(memran)

print(f"The list of elements that are common for the two random lists: {result}.")