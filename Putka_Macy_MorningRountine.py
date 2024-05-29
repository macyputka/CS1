'''
Author: Macy Putka
Description: A typical series of events that depict my typical morning routine through code.
Date: 10/31/23
Bugs: N/A
Challenges: Str.lower(to controll user errors)
Sources: N/A

'''


print("Alarm!")#uses the print command (built in Python function) to display the string marked by the quotations


school_day = str.lower(input("Is it a school day or no?"))#prompts user to respond and stores answer in a variable called school_day while converting the imput into all lowercase


if(school_day == "yes"):#asks whether the variable school_day is equal to the string “yes”

    print("Hit stop on alarm and wake up")#then displays the statement: Hit stop on alarm and wake up.

    cold = str.lower(input("Is it cold?"))#prompts user to respond and stores answer in a variable called cold while converting the imput into all lowercase

    if(cold == "yes"): #if the variable cold is equal to the string “yes”
        print("Put a hoodie on")#then display the statement: Put a hoodie on.

        print("Now you should be warm")#uses the print command (built in Python function) to display the string marked by the quotations

        hungry = str.lower(input("Are you hungry this morning?"))#prompts user to respond and stores answer in a variable called hungry while converting the imput into all lowercase

        if(hungry == "yes"):#asks whether the variable hungry is equal to the string “yes”
            print("Eat some cereal, then afterwards put your dishes away")#then displays the statement: Eat some cereal, then afterwards put your dishes away.

            print("Then after brush your teeth")#then display the statement: Then after brush your teeth.

            hair = str.lower(input("Are you having a bad hair day?"))#prompts user to respond and stores answer in a variable called hair while converting the imput into all lowercase

            if(hair == "yes"):#asks whether the variable hair is equal to the string “yes”
                print("Brush your hair and put it up")#then display the statement: Brush your hair and put it up.

                print("Then go to school and have some fun!")#if the above is a true statement, the program goes to this line and displays the statement: Then go to school and have some fun!

            elif(hair == "no"):#asks whether the variable hair is equal to the string “no”
                print("Leave hair down and style it for school")#then display the statement: Leave hair down and style it for school.

                print("Then go to school and have some fun!")#then display the statement: Then go to school and have some fun!

        elif(hungry == "no"):#asks whether the variable hungry is equal to the string “no”
            print("Just brush your teeth")#then display the statement: Just brush your teeth.

            hair = str.lower(input("Are you having a bad hair day?"))#prompts user to respond and stores answer in a variable called hair while converting the imput into all lowercase

            if(hair == "yes"):#asks whether the variable hair is equal to the string “yes”
                print("Brush your hair and put it up")#then display the statement: Brush your hair and put it up.

                print("Then go to school and have some fun!")#then display the statement: Then go to school and have some fun!

            elif(hair == "no"):#asks whether the variable hair is equal to the string “no”
                print("Leave hair down and style it for school")#then display the statement: Leave hair down and style it for school.

                print("Then go to school and have some fun!")#then display the statement: Then go to school and have some fun!

    elif(cold == "no"):#asks whether the variable cold is equal to the string “no”
        print("Okay then!")#then display the statement: Okay then!

        hungry = str.lower(input("Are you hungry this morning?"))#prompts user to respond and stores answer in a variable called hungry while converting the imput into all lowercase

        if(hungry == "yes"):#asks whether the variable hungry is equal to the string “yes”
            print("Eat some ceral, afterward, put your dishes away")#then display the statement: Eat some ceral, afterward, put your dishes away.
            
            print("Then after brush your teeth")#then display the statement: Then after brush your teeth.

            hair = str.lower(input("Are you having a bad hair day?"))#prompts user to respond and stores answer in a variable called hair while converting the imput into all lowercase

            if(hair == "yes"):#asks whether the variable hair is equal to the string “yes”
                print("Brush your hair and put it up")#then display the statement: Brush your hair and put it up.

                print("Then go to school and have some fun!")#then display the statement: Then go to school and have some fun!

            elif(hair == "no"):#asks whether the variable hair is equal to the string “no”
                print("Leave hair down and style it for school")#then display the statement: Leave hair down and style it for school.

                print("Then go to school and have some fun!")#then display the statement: Leave hair down and style it for school.

        elif(hungry == "no"):#asks whether the variable hungry is equal to the string “no”
            print("Brush your teeth then")#then display the statement: Leave hair down and style it for school.

            hair = str.lower(input("Are you having a bad hair day?"))#prompts user to respond and stores answer in a variable called hair while converting the imput into all lowercase

            if(hair == "yes"):#asks whether the variable hair is equal to the string “yes”
                print("Brush your hair and put it up")#if the above is a true statement, the program goes to this line and displays the statement: Brush your hair and put it up.

                print("Then go to school and have some fun!")#if the above is a true statement, the program goes to this line and displays the statement: Then go to school and have some fun!

            elif(hair == "no"):#asks whether the variable hair is equal to the string “no”
                print("Leave hair down and style it for school")#then display the statement: Leave hair down and style it for school.

                print("Then go to school and have some fun!")#then display the statement: Then go to school and have some fun!

           
elif(school_day == "no"):#asks whether the variable school_day is equal to the string “no”
    print("Hit stop and go back to sleep")#then display the statement: Hit stop and go back to sleep.

