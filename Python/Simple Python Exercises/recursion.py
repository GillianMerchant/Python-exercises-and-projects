#A simple example using print statements to show what happens in recursion

def listSum(numList):
    print("Calling the function with the argument", numList)
    if len(numList)==1:
        print("The list is only 1 item long and this item is", numList[0])
        return numList[0]
    else:
        print("The item at zero position is", numList[0], ". This has been added to the returning value.\n")
        return numList[0] + listSum(numList[1:])
    

myList = [1,3,5,7,9]
print(listSum(myList))
    
