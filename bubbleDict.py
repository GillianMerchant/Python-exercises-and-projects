def dictBubble(aDictList):
    # outer loop is repeated length -1 times. Range() produces numbers from length-1 backwards to 1. 
    print("Length of the list is", len(aDictList), "\n")
    for iteration in range(len(aDictList)-1,0,-1):
        print("Outer loop is now on", iteration, "\n")
# inner loop uses each iteration number from outer loop as max and iterates through list from 0, indexing list
        for i in range(iteration):
            print("The value of i is", i, "and the child at the place in the list is", aDictList[i]["name"])
#if the item at the current index is larger than the next one
            print("Check if the age of", aDictList[i]["name"], "is greater than the age of",aDictList[i+1]["name"])
            if(aDictList[i]["age"]>aDictList[i+1]["age"]):
#use a holding space for the current value to enable swap
                print("Yes we have found the age of", aDictList[i]["name"], "is greater so will swap the items.")
                temp=aDictList[i]
                aDictList[i] = aDictList[i+1]
                print("Now", aDictList[i]["name"], "is at position", i, end=" ")
                aDictList[i+1] =temp
                print("and",aDictList[i+1]["name"], "is at position", i+1,"\n" )
             
    print("The list of kids has been ordered by age, ascending. First in the list is now", aDictList[0]["name"], "and last is", aDictList[2]["name"] )

malc = {
  "name": "Malc",
  "age": 11,
  "hair": "brown"
}

will = {
  "name": "Will",
  "age": 8,
  "hair": "red"
}

iona = {
  "name": "Iona",
  "age": 5,
  "hair": "blonde"
}
#set up a list with the kids details in dictionary objects
kids = [malc, will, iona]
print(dictBubble(kids))
