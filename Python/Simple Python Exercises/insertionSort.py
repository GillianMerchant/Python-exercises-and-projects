# an insertion sort example from Miller & Ranum

def insertionSort(aList):
    print("Starting the insertionSort function with the list", aList, "\n")
#don't start at zero as no point comparing item to itself! Start at 1 to compare the second item (index=1) to the first (index=0).
    for index in range(1, len(aList)):
#get the value of the item you are comparing into a holding variable. This is the first one to the right of the sorted area.
        currentValue = aList[index]
        print("Moving the value", currentValue, "at position", index, "to the holding area")
        position = index
        print("value of index", index)
        print("value of currentValue", currentValue)
        print("value of aList[position]", aList[position])
        print("value of aList[position-1]", aList[position-1], "\n")

#compare current value with one in the sorted area. If the one in the sorted area is greater
        while position>0 and aList[position-1]>currentValue:
            print("Now in the while loop")
            print("value of index", index)
            print("value of currentValue", currentValue)
            print("value of aList[position]", aList[position])
            print("value of aList[position-1]", aList[position-1], "\n")
            print("We have found that the value", aList[position-1], "at position", [position-1], "is greater than the current value of", currentValue, "at position", index, "\n")
#then move the larger value to the right.
#The value in that slot will have been saved elsewhere - either in the holding area or further right in the sorting area. 
            aList[position]=aList[position-1]
            print("Reassignment of position", position, "to value",aList[position-1] )
            print("value of aList[position]", aList[position])
            print("value of aList[position-1]", aList[position-1], "\n")
#then reduce the value of position by 1 so on the next loop you are comparing with the previous item in the sorted area
            position = position-1
            print("new value of position is", position, "ready for next loop. If it's a zero then back to the outer loop.\n")
        aList[position]=currentValue
        print("The currentValue of", currentValue, "is moved out of holding area and saved back to position", position, ". The list now looks like this:", aList, "\n")
    print("The list has been sorted and looks like this", aList)

countries = ["china", "brazil", "algeria", "zaire", "korea", "scotland"]
print(insertionSort(countries))