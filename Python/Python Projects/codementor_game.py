import random
# This is an exercise from codementor to create a game of rock, paper, scissors where the user plays against the computer.
# It uses the random.choice() function to pick the computer's choice. The user's choice is entered as the argument in the fucntion call. 
# Next step might be to keep a scoring tally. This would need to be done outside this function possibly with recursion?
# Have set up the counters to keep score for now even though they won't work just yet.

"""
Name rpsGame
Input a choice from player and a random generated choice from computer
Output a string saying you win or you lose, and an int / string indicating score

Initial Insight
Get the input i from the user to start the process. User may input any of the elements of the game as a string
Program validates that the string is one of a collection (use in array?)
The computer generates an item g using random choice
Some logic takes place:

user   computer
rock v rock = draw
rock v paper = paper
rock v scissors = rock
paper v rock = paper
paper v paper = draw
paper v scissors = scissors
scissors v rock = rock
scissors v paper = scissors
scissors v scissors = draw

Set the content of the string according to if the user has won, lost or drawn.
Return string. 

Specify the alogorithm in structured english:
CALL the function with a string input i
set g to random.choice(r,p,s)
set w winner empty string
IF i is not in array of answers
   set s to "pick a proper item"  exit loop
   return?
WHILE i == "rock"
   if (g==rock) w is draw
   if (g==paper) w is computer wins
   if (g==scissors) w is you win
WHILE i == "paper"
   if (g==rock) w is you win
   if (g==paper) w is draw
   if (g==scissors) w is computer wins
WHILE i == "scissors"
   if (g==rock) w is computer wins  
   if (g==paper) w is you win
   if (g==scissors) w is  draw
return w  

write the python!"""
   

def rpsGame(i):
    #set up counters for when 
    user = 0
    computer = 0
    gameArray = ["rock", "paper", "scissors"]
    g = random.choice(gameArray)
    print("The computer has chosen", g, "and you have chosen", i)
    #set up strings
    s = ""
    d = "It's a draw!"
    c = "Sorry, computer wins"
    u = "Fantastic! You win!!!"
    x = "Sorry - that's not a valid choice"
    
    if(i not in gameArray):
        s = x
    
    else:
        if(i=="rock"):
            if(g=="rock"):
               s = d
            elif(g=="paper"):
               s = c
               computer = computer+1
            else:
               s = u
               user = user +1
    
        elif(i=="paper"):
            if(g=="rock"):
               s = u
               user = user +1
            elif(g=="paper"):
               s = d
            else:
               s = c
               computer = computer+1
           
        else:
            if(g=="rock"):
               s = c
               computer = computer+1
            elif(g=="paper"):
               s = u
               user = user +1
            else:
               s = d       
    
    print(s)
  #print("Scoreboard")
  # print("Computer:", computer, "You:", user)
  # if(computer>user):
  #      print("Computer is winning!")
  #  elif(computer==user):
  #      print("It's a draw so far")
  #  else:
  #      print("You're winning!")
   

choice = "scissors"
print(rpsGame(choice))
