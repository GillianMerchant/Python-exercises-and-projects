#Having reversed a list of words I wanted to try a string - this may have been a codejam exercise
# The function reverses a list of strings in one go and prints them with a prefix. 

def reverseString(linesList):
    myList = []
    index = 0
    print("length of lines list is ", len(linesList))
    while index <(len(linesList)):
# split up the current list at every space and save as list
        myList = linesList[index].split(' ')
        print("The string split up is", myList)
    
        reverseList = []
    
        size = len(myList)
        i=0
        while i<size:
# use pop and append to move words from end of one list to start of a new one
# note this will empty the argument list. Ok as we don't need it again here. 
            reverseList.append(myList.pop())
            i=i+1
# once all the items have been moved from one list to the other, convert to a string, joining with a space
        finalString =  ' '.join(reverseList)
        caseString = "Case #"
        completeString = caseString + str(index+1) + " " + finalString
        index=index+1
        print(completeString)


myString1 = "hello and how are you today?"
myString2 = "what does this look like backwards?"
myString3 = "ey up lass"
myString4 = "dfkgjklgj klfjkjkfg "
myString5 = "123 36 67 68"
myList = []
myList.append(myString1)
myList.append(myString2)
myList.append(myString3)
myList.append(myString4)
myList.append(myString5)
print ("List is", myList)
print(reverseString(myList))
