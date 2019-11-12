"""An example of a bubble sort as described in Miller & Ranum 2011 p209-211.
I adapted the version in Miller & Ranum which just sorted a list of ints, to one sorting a list of dictionary objects
holding data about my children, by the age of the child.
This more efficient version of the bubble sort will exit once the list is sorted even if all the loops have not finished.
GM Nov 2019
"""

def dictBubble(aDictList):
    # outer loop is repeated length -1 times. Range() produces numbers from length-1 backwards to 1. 
    print("Length of the list is", len(aDictList), "\n")
    #use a while loop so can exit as soon as an inner loop finds no changes to make. Avoids unnecessary loops.
    outOfOrder = True
    iteration = (len(aDictList)-1)
    while iteration >0 and outOfOrder:
        outOfOrder = False
        print("Outer loop is now on", iteration, "\n")
# inner loop uses each iteration number from outer loop as max and iterates through list from 0, indexing list
        for i in range(iteration):
            print("The value of i is", i, "and the child at the place in the list is", aDictList[i]["name"])
#if the item at the current index is larger than the next one
            print("Check if the age of", aDictList[i]["name"], "is greater than the age of",aDictList[i+1]["name"])
            if(aDictList[i]["age"]>aDictList[i+1]["age"]):
#set condition checker to True meaning we continue with the next loop
                outOfOrder=True
#use a holding space for the current value to enable swap
                print("Yes we have found the age of", aDictList[i]["name"], "is greater so will swap the items.")
                temp=aDictList[i]
                aDictList[i] = aDictList[i+1]
                print("Now", aDictList[i]["name"], "is at position", i, end=" ")
                aDictList[i+1] =temp
                print("and",aDictList[i+1]["name"], "is at position", i+1,"\n" )
             
    print("The list of kids has been ordered by age, ascending. First in the list is now", aDictList[0]["name"], "and last is", aDictList[2]["name"] )

m = {
  "name": "M",
  "age": 11,
  "hair": "brown"
}

w = {
  "name": "W",
  "age": 8,
  "hair": "red"
}

i = {
  "name": "I",
  "age": 5,
  "hair": "blonde"
}
#set up a list with the kids details in dictionary objects
kids = [m, w, i]
print(dictBubble(kids))
