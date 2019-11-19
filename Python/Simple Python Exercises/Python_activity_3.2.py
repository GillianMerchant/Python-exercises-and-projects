#!/usr/bin/env python3


# The listSum() function from Listing 4.2 in
# Introduction to Data Structures and Algorithms in Python,
# by Bradley N. Miller, David L. Ranum. Copyright 2005.

#Authors: M269 Module Team
#Date: 20/11/12

import random

callTotal = 0 #global variable

def listSum(numList):
#A global variable that can be called outside the function, increases by 1 at each recursion. Used to count the recursions.
    global callTotal  #Needed to modify global variable callTotal
    callTotal = callTotal + 1
#Set the current value of callTotal to a local var to use on this recursion .Shows which recursion we are on.
    thisCall = callTotal
    print('Call', thisCall, 'of function', 'with numList =', numList)
#the base case statement, taking the zeroth item from the list, and starting the unwinding statements. 
    if len(numList) == 1:
        print('Base case reached, so begin to unwind, returning', numList[0], 'to call', thisCall - 1)
        return numList[0]
    else:
#the recursion statement is here, calling the function with a reduced list taking slice [1: ]  Saved to a variable called sumOfSublist which will increase each time. 
        sumOfSublist = listSum(numList[1:])
        print("The value of sumOfSublist is now", sumOfSublist, "\n")
        result = numList[0] + sumOfSublist
        if thisCall - 1 == 0:
            print('unwinding,', 'call', thisCall, 'returning the result of', numList[0], '+', sumOfSublist)
        else:
            print('unwinding,', 'call', thisCall,  'returning the result of', numList[0], '+', sumOfSublist, 'to call', thisCall - 1)
        return result


#Create a list of random integers to use as the argument to listSum()
list1 = [1,3,5,7,9]
#for i in range(1, 6):
#    list1.append(random.randrange(1, 11))
    
#Test the function
print(listSum(list1))