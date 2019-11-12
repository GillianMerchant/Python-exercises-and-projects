import random

#This is an exercise from codementor.
#The computer randomly generates a number between 0 and 20. The user needs to guess what the number is.
#If the guess is wrong, tell them their guess is too high or too low.


"""
Name: GuessRandom
Inputs: An integer guess i and a random generated number g
Outputs: A string s to give the results

Initial Insight:
Get the input i from the user to start the process.
Generate the random number g between 0 and 20 and compare with the input.
If i is equal to g, return the string s saying that it matches.
If i is less than g, return s saying the guess is  too low
If i is greater than g, return s saying the guess is too high

Specify the alogorithm in structured english:
call the function with an argument of i
set up empty string s
use math random to generate an int g >=0 and <=20
IF i=g (s = "just right")
  ELSE IF i<g (s = "too low")
    ELSE (s="too high")
return s
"""

def checkFunction(i):
    s=""
    g = random.randrange(0,20)
    print("This is the random number:", g, ". Your number was", i, ".")
    if(i==g):
        s = "Perfect match!"
    elif(i<g):
        s = "Uh oh too  low!"
    else:
        s = "Oops too high...."
    
    return s

i = 5
(print(checkFunction(i)))
