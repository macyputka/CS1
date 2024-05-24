import sys#imports the library names that is called sys
import random#finds things in the random library

def add_entry(websites, usernames, passwords):#creating a function called new_entry that coresponds with websites, usernames and passwords
        websites.append(input("Please enter in your website name:"))#add to list (websites) from users input
        usernames.append(input("Please enter in your username:"))#add to list (uswernames) from users input
        passwords.append(input("Please enter in your password:"))#add to list (passwords) from users input

def print_entry(websites, usernames, passwords, i):#creating a function called print_entry that corresponds with websites, usernames and passwords based on the index of i
        print(f'''\nWebsite:{websites[i]}
                Username: {usernames[i]} 
                Password:{passwords[i]}''')#prints specific function including the findings of i
def main():#creating a main function to call the password keeper
        websites = [] #creates empty list called websites
        usernames = [] #creates empty list called usernames
        passwords = [] #creates empty list called passwords

        add_entry(websites, usernames, passwords) #calls the function add_entry and addes to the inital entry
            
        while True:#creating a loop to keep the program running until user exits
                options = '''\nPlease push:
                             1 key = enter a new password.
                             2 key = printing all of your websites, usernames, and passwords.
                             3 key = acessing a previous password.
                             4 key = editing a previous password.
                             5 key  = editing a previous username.
                             6 key= create strong password.
                             7 key = to exit.
                             0 key = Enter Password Keeper'''#identifing new variable
                mode = input(options)#creating a input variable for the user to enter to controll what happens next
                
                if mode == "7": #lastly if the user enters the 7 key
                    break#ends the program
                elif mode == "0":#when the user enters the 0 key
                        print(options)#print the options variable
                elif mode == "1": #if the user selects the 1 key
                    add_entry(websites, usernames, passwords)#return the add entry function to the user
                elif mode == "2": #if the user selects the 2 key
                    for i in range(len(websites)): #go through the index's of the the list and uses the function
                      print_entry(websites, usernames, passwords, i)#prints corresponding lists
                elif mode == "3": #if the user selects the 3 key
                    web = input("Enter the name of the website of the password you would like to acess:")#ask the user which website they want to access
        
                    if web in websites: #checking if the website is in the list
                     #i = (find the index of web in websites)
                     print_entry(websites, usernames, passwords, websites.index(web))#printing the entry
                    else:#lastly this will happen
                        print(f" ' {web} has not been entered, please retry.")#printing for the user including the website in the list
                elif mode == "4":#when the user enters the 4 key
                    web = input("Enter the name of the website of the password you would like to change/edit:")#ask the user which website they want to access
                    
                    if web in websites:#checking if websites is in the list
                       #i = (find the index of web in websites)
                       passwords[websites.index(web)] = input("Enter new password: ")#updating the password by replacing it by its index from users input
                elif mode == "5":#when the user enters the 5 key
                    web = input("Enter the name of the website of the password you would like to change/edit:")#ask the user which website they want to access
                    
                    if web in websites:#checking if websites is in the list
                      #i = (find the index of web in websites)
                      usernames[websites.index(web)] = input("Enter new username: ")#updating the username by replacing it by its index from the users input
                elif mode == "6":#if the user presses the 6 key
                        pswd = [] #creates a new emoty list
                        digits = list("0123456789")#creating a variable list
                        special_characters = list("!@#$%^&*")#creating a variable list
                        lowercase = list("qwertyuiopasdfghjklzxcvbnm")#creating a variable list
                        uppercase = list("QWERTYUIOPASDFGHJKLZXCVBNM")#creating a variable list
        
                        for i in range(3):#repeats these next actions 3 times
                                pswd.append(random.choice(digits))#add a digit to the new password
                                pswd.append(random.choice(special_characters))#add a special character to the new password
                                pswd.append(random.choice(lowercase)) #add a lowercase letter to the new password
                                pswd.append(random.choice(uppercase))#add a uppercase letter to the new password
                        random.shuffle(pswd)#shuffle randomly the new password
                        print(''.join(pswd))#add/join new password that has been created to the list
                else:#if anything else doesn't happen do this next
                    print(f"invalid")#prints if user entry does not fit in menu
                        

main()#calling the main function

