'''
Name: Macy Putka
Date: 12/1/23
Description: Come play rock paper scissors in python with me!
Challenges: Recording sore in the game, score limit, users imput will be translated into all lowercase, enter stop to end the game, invaild spelling or imput addition
Bugs: N/A
Sources: Ms. Maricano
'''

import random#tells computer to go to what we can call "the random library"

user_score = 0#stating the starting score of the game
bot_score = 0#stating the starting score of the game

score_limit = 6#stating the score limit for game, which is 6

options = ["rock", "paper", "scissors"]#create a list of play options

while True:#stating that is is an infinite loop
    if(user_score >= score_limit or bot_score >= score_limit):#creating a system to check whether the user's or the bot's score is higher than the score limit
        print("Game over!")#print the text "game over"
        break#stop the code completely

    player = str.lower(input("Rock, Paper, Scissors? or enter stop to stop"))#converts players input into all lowercase so matches list format, prints repeating game advancing question until either the user or the bot gets to 6 first
    computer = random.choice(options)#assign a random play to the computer
    
    if player == "stop": #if player's input is stop to do something special
        print("Thanks for playing!")#print "thanks for playing" after the users specical input
        break #allow a space to ocrur in order to end code
    elif player not in options:#if player enters a "invaild" or an input that is not listed, do something specific
        print("That's not a valid play. Check your spelling!") #player was set to True, but we want it to be False so the loop continues
        print("")#add an extra space so its easier to read
    elif player == "rock":#if player inputs "rock" from the list do a certain next step, which is compared this imput to the random selected compter choice
        if computer == "paper":#if the computers random choice ends up being "paper" aganist "rock" print the following and which is to communitcate to user that the computer and the user picked different imput so only one gets a point
            print("You lose!", computer, "covers", player)#Depending on the comparison of the two list items, explain why one would win over the other in terms of the rules of the game
            bot_score += 1#add a point to (either side technically) the bot score becuase they won this specific battle
            print("")#add an extra space so its easier to read
        if computer == "rock":#if computer inputs "rock" from the list do a certain next step, which is communitcate to user that the computer and the user picked the same imput so no one gets a point
                print("Tie!")#print "tie!"
                print("")#add an extra space so its easier to read
        if computer =="scissors": #when anything else occurs when the user enters "rock" and the random choice computer selects in not "paper"
            print("You win!", player, "smashes", computer)#Depending on the comparison of the two list items, explain why one would lose in terms of the rules of the game
            user_score += 1#add a point to (either side technically) the bot score becuase they won this specific battle
            print("")#add an extra space so its easier to read
    elif player == "paper":#if player inputs "rock" from the list do a certain next step, which is compared this imput to the random selected compter choice
        if computer == "scissors"::#if the computers random choice ends up being "paper" aganist "scissors" print the following and which is to communitcate to user that the computer and the user picked different imput so only one gets a point
            print("You lose!", computer, "cuts", player)#Depending on the comparison of the two list items, explain why one would win over the other in terms of the rules of the game
            bot_score += 1#add a point to (either side technically) the bot score becuase they won this specific battle
            print("")#add an extra space so its easier to read
        if computer == "paper":#if computer inputs "paper" from the list do a certain next step, which is communitcate to user that the computer and the user picked the same imput so no one gets a point
                print("Tie!")#print "tie!"
                print("")#add an extra space so its easier to read
        if computer == "rock":#if the computers random choice ends up being "paper" aganist "rock" print the following and which is to communitcate to user that the computer and the user picked different imput so only one gets a point
            print("You win!", player, "covers", computer)#Depending on the comparison of the two list items, explain why one would lose in terms of the rules of the game
            user_score += 1#add a point to (either side technically) the bot score becuase they won this specific battle
            print("")#add an extra space so its easier to read
    elif player == "scissors":#if player inputs "scissors" from the list do a certain next step, which is compared this imput to the random selected compter choice
        if computer == "rock":#if the computers random choice ends up being "scissors" aganist "rock" print the following and which is to communitcate to user that the computer and the user picked different imput so only one gets a point
            print("You lose...", computer, "smashes", player)#Depending on the comparison of the two list items, explain why one would win over the other in terms of the rules of the game
            bot_score += 1#add a point to (either side technically) the bot score becuase they won this specific battle
            print("")#add an extra space so its easier to read
        if computer == "scissors":#if computer inputs "scissors" from the list do a certain next step, which is communitcate to user that the computer and the user picked the same imput so no one gets a point
                print("Tie!")#print "tie!"
                print("")#add an extra space so its easier to read
        if computer == "paper":#if the computers random choice ends up being "paper" aganist "scissors" print the following and which is to communitcate to user that the computer and the user picked different imput so only one gets a point
            print("You win!", player, "cuts", computer)#Depending on the comparison of the two list items, explain why one would lose in terms of the rules of the game
            user_score += 1#add a point to (either side technically) the bot score becuase they won this specific battle
            print("")#add an extra space so its easier to read

    print(f"User: {user_score} - Bot: {bot_score}")#prints the final score, within the score limit

  
        
