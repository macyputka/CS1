'''
Author: Macy Putka
Description: Have fun while asking the MAGIC 8 BALL questions!
Date: 11/13/23
Bugs: N/A
Challenges: Many different responses for the variable "answers", MAGIC 8 displayed at top, continues in a cycle after valid imput by user with a "?", if user does not imput a "?" code will ask the user to imput different response with one in it.
Sources: W3schools, W3resources
'''

import random #automaically or randomly display the following "print" commands

print('  __  __          _____ _____ _____    ___  ')#uses the print command to display the string that makes up the big "magic 8" title.
print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')#uses the print command to display the string that makes up the big "magic 8" title.
print(' | \  / |  /  \ | |  __  | || |      | (_) |')#uses the print command to display the string that makes up the big "magic 8" title.
print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')#uses the print command to display the string that makes up the big "magic 8" title.
print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')#uses the print command to display the string that makes up the big "magic 8" title.
print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')#uses the print command to display the string that makes up the big "magic 8" title.
print('')#uses the print command to display a space.
print('')#uses the print command to display a space.

answers = ["No.","Yes.","Maybe","ask again later","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","I do not know yet","Signs point to yes.","It may depend, try again.","Ask again later.","Better not tell you now.","Cannot predict that right now.","Concentrate and ask again.","Don't count on it.","Magic 8 ball says no.","Oh my friend, no.","Outlook not so good.","Very doubtful about that"] #List answers that are possible response's to the variable "question"

while True: #infinite cycle that occurs for variable "questions" when true == true
    question=input("Ask the magic 8 ball a yes or no question (or press enter to quit): ") #prompts user to respond and stores answer in a variable called question

    if question=="":#if the user's imput is the return space in repsonse to the variable question
        print("Thanks for playing. Stopping the Game Now!")#uses the print command to display the string that prints "Thanks for playing. Stopping the Game Now!"
        break #prints and displays a space.

    elif "?" in question:#if the user's answer does or does not include a "?" there will be different responses.
        print(random.choice(answers))#print a random response for the imput using available response from variable "answer" by using "radom.choice" in response to the user's imput (a question) with a "?"
    else:#if user imputs text without a question mark (therefore not a question) a different command occurs.
        print("Ask a question!")#if no "?" in users's imput, display text: "Ask a question".


