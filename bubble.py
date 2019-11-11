def intBubble(aList):
# outer loop is repeated length -1 times. Range() produces numbers from length-1 backwards to 1. 
    for iteration in range(len(aList)-1,0,-1):
        print("Outer loop is now on", iteration)
# inner loop uses each iteration number from outer loop as max and iterates through list from 0, indexing list
        for i in range(iteration):
            print("The value of i is", i, "and the item at the place in the list is", aList[i])
#if the item at the current index is larger than the next one
            if(aList[i]>aList[i+1]):
#use a holding space for the current value to enable swap
                temp=aList[i]
                aList[i] = aList[i+1]
                aList[i+1] =temp
    print("The sorted list is", aList)

myList = [5,3,8,2,9]
print(intBubble(myList))