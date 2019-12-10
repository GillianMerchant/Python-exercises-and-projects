# Write a function which takes a list as argument and returns true if the list is a heap, otherwise false.
# The function should iterate backwards through the list, from the last item down to the one at position 2,
# comparing each item with its parent.
#( Hint: you saw in Python activity 3.1 how to iterate backwards through a list.)

# GM attempt:
# If the list is a heap then each item will not be greater than its parent
# Start at the end. Compare the item at the end to the parent item which will be at index //2.
# Note that we will need to add a zero in at position 0 in the list for this to work. We could do it without this but would change the division results!
# Then in a loop move back through the list. Use range function from -1 with steps of -1.
# If an instance is found where the parent is greater than the child, stop the loop as the answer has been found to be false. 

def isListHeap(aList):
# set up the boolean to indicate when an unordered item has been found (meaning list is not a heap)
    isHeap = True
# add an initial zero to the list for mathematical purposes.
# This maintains the second index (i=1) at the root of the tree and means that child's index //2 will index parent.
# Use a slice to make a copy.
    fullList = [0] + aList[:]
# set up a loop to iterate through the range backwards up to i =2.
    # Note the range start, stop and step params are len-1, 1, -1 and not len-1,2,-1. This is because the second parameter in range() is exclusive ie we go up to but not including the i=1 item. 
    for i in range(len(fullList)-1,1,-1):
        if fullList[i]<fullList[i//2]:
            isHeap=False
            break
                
    return isHeap


myList = [1,2,9,4,5,6,7]
print("Check if list is a heap:", isListHeap(myList))
    