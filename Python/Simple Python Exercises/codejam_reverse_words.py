#This is an exercise from google codejam,  to reverse a list of words
#I set up a few test cases for manual checking
# Next step would be to think about how this might be tested by an algorithm


def reverseFunc(list):
    i=0
    print("Reversing list", list, ". Thelength of the list is", len(list))
    newList = []
    size = len(list)
    while i<size:
        newList.append(list.pop())
        i=i+1
    newList.append
    return newList
    
testList = []
myList = ["hello", "said", "gill"]
myShortList = ["hi"]
myEmptyList = []
myLongList = ["start", "here","what", "does", "this", "help","what", "does", "this", "say","a", "b", "c","does", "this", "help","what", "does", "this", "say","a", "does", "this", "help","what", "does", "this", "this", "say","a", "b", "c","does", "this", "help","what", "does", "this", "say","a", "does", "this", "help","what", "does", "this","this", "say","a", "b", "c","does", "this", "help","what", "does", "this", "say","a", "does", "this", "help","what", "does", "this","this", "say","a", "b", "c","does", "this", "help","what", "does", "this", "say","a", "does", "this", "help","what", "does", "this","this", "say","a", "b", "c","does", "this", "help","what", "does", "this", "say","a", "does", "this", "help","what", "does", "this","this", "say","a", "b", "c","does", "this", "help","what", "does", "this", "say","a", "does", "this", "help","what", "does", "this","this", "say","a", "b", "c","does", "this", "help","what", "does", "this", "say","a", "does", "this", "help","what", "does", "this","this", "say","a", "b", "c","does", "this", "help","what", "does", "this", "say","a", "does", "this", "help","what", "does", "this","this", "say","a", "b", "c","does", "this", "help","what", "does", "this", "say","a", "does", "this", "help","what", "does", "this","this", "say","a", "b", "c","does", "this", "help","what", "does", "this", "say","a", "does", "this", "help","what", "does", "this","this", "say","a", "b", "c","does", "this", "help","what", "does", "this", "say","a", "does", "this", "help","what", "does", "this","this", "say","a", "b", "c","does", "this", "help","what", "does", "this", "say","a", "does", "this", "help","what", "does", "this","end"]
myIntList = [1,2,3]
testList = [myList, myShortList, myEmptyList, myLongList, myIntList]
for i in testList:
    print("The contents of the list in reverse is",  reverseFunc(i))




