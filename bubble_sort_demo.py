"""
Beginner
Create a list of a user-input number of random integers (between 0 and 100, inclusive). Output this list to the console
both before and after sorting the list using the Bubble Sort method. The numbers should be sorted in numerical
least-to-greatest order. The list should be output with square brackets wrapping the elements of the array, with commas
separating each element.
"""

import random as rand
from time import sleep

num_Range = 100
list_Size = int()
my_List = list()

# Requests numeric user input. Catches invalid input.
try:
    list_Size = int(input("Please choose a list length, enter any whole number: "))
except ValueError:
    print("Your entry was not a number, please follow the instruction. Program Terminated.")
    exit()

# Adds a random numbers to my_List until my_List has the number of elements chosen by the user.
for iteration in range(list_Size):
    my_List.append(rand.randrange(0, num_Range))

# Displays the initial list of random numbers.
time_Delay = 0.7
sleep(time_Delay)
print("\nGenerated", list_Size, "random elements...\n")
sleep(time_Delay)

print(my_List)

# Sorts the list numerically and displays it again.
sleep(time_Delay)
print("\nWill now proceed to rearrange...\n")
sleep(time_Delay)

needs_Sorting = True
max_Index = list_Size-1

while needs_Sorting:
    needs_Sorting = False
    for i in range(list_Size):
        if i < max_Index:
            if my_List[i] < my_List[i+1]:
                temp_Int = my_List[i+1]
                my_List[i+1] = my_List[i]
                my_List[i] = temp_Int
                needs_Sorting = True

print(my_List)
