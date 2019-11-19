#An example from the M269 module materials
#I have annotated and added print statements to clarify the process

#This example of recursion is not very intuitive. The recursion call proceeds backwards through the list
# ie calling itself with argument -1 each time.
# I think this is to allow it to then work forwards through the list when unwinding.

import random


def recursiveInsertionSort(aList, startPosition):
    print ("Function called for list", aList, "and starting position", startPosition)
    if startPosition == 0: #there is only 1 item in the sorted part of the list so function call ends
         return
    else:
        recursiveInsertionSort(aList, startPosition - 1)
        print("Unwinding for startPosition", startPosition)
        currentValue = aList[startPosition]
        position = startPosition
        print("Position is", position)
        while position > 0 and aList[position - 1 ] > currentValue:
            print("Value", aList[position], "in position", position, "is now going to be replaced with", aList[position - 1], "from the previous position.")
            aList[position] = aList[position - 1]
            position = position - 1
        aList[position] = currentValue
        





#Create an unsorted list of random integers to use as the argument to the above function
list1 = []
for i in range(10):
    list1.append(random.randrange(1, 101))
    
recursiveInsertionSort(list1, len(list1) - 1)
print(list1)
#print("The sorted list is", recursiveInsertionSort(list1, len(list1) - 1) )