#A selection sort from Miller & Ranum.  With lots of comments and print statements added by me to illuminate the process!
#I have used this to sort a list of flowers alphabetically and in reverse alphabetical order. 

def selectionSort(aList):
#set the fillslot iterator. This goes backwards from the end of the list to 1
#The fillslot marks the slot which is to be filled next
#ie everything to the right is sorted  meaning that only the unsorted portion of list is checked each time. 
    print("Sorting my flowers into alphabetical order\n")
    for fillslot in range(len(aList)-1,0,-1): 
        positionOfMax = 0
        print("Fillslot is currently position", fillslot, "and the value of it is", aList[fillslot], "\n")
        for location in range(1, fillslot +1):
            print("The current slot being checked is", location, "and the value of it is", aList[location])
#If the value at current position is greater than the value at the last location that variable positionOfMax was set to
# set  positionOfMax to this position.Once the inner for loop has finished positionOfMax will be the max in the whole unsorted portion.
            if aList[location]>aList[positionOfMax]:
               positionOfMax = location
               print("positionOfMax has moved to position", location)
#hold the value in fillslot in a temp variable to allow it to be swapped with the value at positionOfMax
        temp = aList[fillslot]
        aList[fillslot]=aList[positionOfMax]
        aList[positionOfMax]=temp
        print("Now the max value found:", aList[fillslot], " has been moved to the position", fillslot,"and the value", aList[positionOfMax],"is now in position", positionOfMax,"\n")
#once the sorting is complete return the sorted list        
    return aList

def selectionSortReverse(aList):
#another version but with reverse alphabetical sorting
    print("Sorting my flowers into REVERSE alphabetical order\n")
    for fillslot in range(len(aList)-1,0,-1): 
        positionOfMax = 0
        print("Fillslot is currently position", fillslot, "and the value of it is", aList[fillslot], "\n")
        for location in range(1, fillslot +1):
            print("The current slot being checked is", location, "and the value of it is", aList[location])
#This is the only bit that needs to change
            if aList[location]<aList[positionOfMax]:
               positionOfMax = location
               print("positionOfMax has moved to position", location)
        temp = aList[fillslot]
        aList[fillslot]=aList[positionOfMax]
        aList[positionOfMax]=temp
        print("Now the max value found:", aList[fillslot], " has been moved to the position", fillslot,"and the value", aList[positionOfMax],"is now in position", positionOfMax,"\n")   
    return aList

flowers = ["begonia", "rhododendron", "marigold", "rose", "iris", "buttercup", "lily", "allium"]

print("*"*150,"\nMy  list of flowers in alpha is", selectionSort(flowers))
print("*"*150,"\n","*"*150)
print("My  list of flowers in reverse alpha is", selectionSortReverse(flowers))