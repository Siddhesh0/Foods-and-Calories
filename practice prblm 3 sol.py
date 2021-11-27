                             # FOODS AND CALORIES
"""
You visit the restaurant called siddhesh gavare and food items in their restaurant are sorted on their
amount of their calories. you have to reverse the list of food items with their calories.

you have to use following three methods to reverse string:
            Inbuilt method of python
            Listname[::-1] slicing trick
            swapping first element with last one and second with last second and so on....

INPUT:

Take list as input from user

OUTPUT:
[1, 4, 5]
[1, 4, 5]
[1, 4, 5]

All three methods will give same output

Author: Siddhesh
Date: 21 Nov 2021
Purpose: Practice problem
"""

# Take the size of the list from the user
print("Enter the no. of list to be display\n")
size =int(input("Enter the size of list\n"))

# create a blank list
my_list = []

# Take the input from the user one buy one
for i in range(size):
    my_list.append(int(input("Enter the numbers\n")))

print("Your list is", my_list)

# reverse the string
siddhesh = my_list[:]
siddhesh.reverse()
print("The first reversed list of", my_list, "is", siddhesh)

# Listname[::-1] slicing trick
print("The second reversed list of", my_list, "is", my_list[::-1])

# swapping first element with last one and second with last second and so on....3
# print("The third reversed list of", my_list, "is", my_list[::-1])
