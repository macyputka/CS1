
import random  # Import the random module to use random number generation functions


def chorus():# Define the chorus function
    print('''
But I keep cruisin'
Can't stop, won't stop movin'
It's like I got this music in my mind
Sayin' it's gonna be alright
'Cause the players gonna play, play, play, play, play
And the haters gonna hate, hate, hate, hate, hate
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off (hoo-hoo-hoo)
Heartbreakers gonna break, break, break, break, break
And the fakers gonna fake, fake, fake, fake, fake
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off (hoo-hoo-hoo)
''') # Print the lyrics of the chorus


def sing_song():# Define the sing_song function
    print('''I go on too many dates
But I can't make 'em stay
At least that's what people say, mm-mm
That's what people say, mm-mm''')# Print the first part of the song lyrics
    chorus()  # Call the chorus function to print the chorus
    print('''I never miss a beat
I'm lightnin' on my feet
And that's what they don't see, mm-mm
That's what they don't see, mm-mm
I'm dancin' on my own (dancin' on my own)
I make the moves up as I go (moves up as I go)
And that's what they don't know, mm-mm
That's what they don't know, mm-mm''')# Print the next part of the song lyrics
    chorus()  # Call the chorus function to print the chorus again

def add(num1, num2):# Define the add function
    print(num1 + num2)# Print the sum of num1 and num2


def print_elements(input_list):# Define the print_elements function
    for element in input_list:# Iterate through each element in the input_list
        print(element)# Print the current element



def element_in_list(input_list, element):# Define the element_in_list function
    return element in input_list# Return True if the element is in the input_list, otherwise False


def check_if_integer(param):# Define the check_if_integer function
    if "-" in param: # If the parameter contains a "-", remove it
        param = param[1:]
    return param.isnumeric() # Return True if the parameter is numeric, otherwise False



def get_integer():# Define the get_integer function
    while True: #Creates a while True loop
        try: #Running a sample of code
            return int(input("Please enter a number: ")) # Return the integer value of the user input
        except ValueError: #When error is found
            print("Please enter a valid number.") # Print an error message if the input is not a valid number



def get_random_num(num1, num2):# Define the get_random_num function
    return random.randint(num1, num2)# Return a random integer between num1 and num2 (inclusive)



def replacing(input_string, old_character, new_character):# Define the replacing function
    new_string = ""  # Initialize an empty string to store the new string
    for character in input_string: # Iterate through each character in the input_string
        if character == old_character:  # If the character matches old_character, add new_character to new_string
            new_string += new_character
        else:
            new_string += character  # Otherwise, add the original character to new_string
    return new_string # Return the modified string


def reverse(string):# Define the reverse function
    return string[::-1] # Return the reversed string



def checking_if_palindrome(string):# Define the checking_if_palindrome function
    return string == reverse(string) # Return True if the string is the same forwards and backwards, otherwise False



def find_my_initials(name):# Define the find_my_initials function
    initials = "" # Initialize an empty string to store the initials
    name_parts = name.split() # Split the name into parts
    for part in name_parts: # Iterate through each part of the name
        initials += part[0] # Add the first letter of the part to initials
    return initials.upper() # Return the initials in uppercase



def main():# Define the main function
    sing_song() # Call the sing_song function

    input_name = input("Enter a name: ")  # Prompt the user to enter a name
    first_initial = find_my_initials(input_name)  # Get the initials of the name
    print("First initials are:", first_initial)  # Print the initials


    print("")  # Print a blank line


    num1 = int(input("Enter in a number: "))  # Prompt the user to enter a number
    num2 = int(input("Enter in another number: "))  # Prompt the user to enter another number
    add(num1, num2)  # Call the add function with the two numbers
    input_str = input("Enter in 3 words separated by spaces: ")  # Prompt the user to enter 3 words
    print_elements(input_str.split())  # Split the input string into words and print each word


    print("")  # Print a blank line


    my_fruit_list = ["apple", "banana", "mango", "pineapple", "kiwi"]  # Define a list of fruits
    find_in_list = input("Enter a fruit to see if Python likes to eat it: ")  # Prompt the user to enter a fruit
    result = element_in_list(my_fruit_list, find_in_list)  # Check if the fruit is in the list
    print("Is", find_in_list, "in the list?", result)  # Print the result


    print("")  # Print a blank line


    print("*0 Cannot be entered*")  # Print a warning message
    num1 = get_integer()  # Get an integer from the user
    num2 = get_integer()  # Get another integer from the user
    random_num = get_random_num(num1, num2)  # Get a random number between num1 and num2
    print(num1, random_num, num2)  # Print the two numbers and the random number


    print("")  # Print a blank line


    input_str = input("Enter a word: ")  # Prompt the user to enter a word
    i1 = input("Enter a letter in your word to be replaced: ")  # Prompt the user to enter a letter to be replaced
    i2 = input("Enter a letter(s) to then do the replacing: ")  # Prompt the user to enter the replacement letter(s)
    result = replacing(input_str, i1, i2)  # Replace the letter in the word
    print("Now edited word:", result)  # Print the modified word


    print("")  # Print a blank line


    input_name = input("Enter in a name! -> ")  # Prompt the user to enter a name
    reversed_name_result = reverse(input_name)  # Reverse the name
    print("Your now reversed name is:", reversed_name_result)  # Print the reversed name


    print("")  # Print a blank line


    input_string = input("Enter a word to see if it is a palindrome: ")  # Prompt the user to enter a word
    result = checking_if_palindrome(input_string)  # Check if the word is a palindrome
    if result:
        print("This word is a palindrome.")  # Print if the word is a palindrome
    else:
        print("The word is not a palindrome.")  # Print if the word is not a palindrome


    print("")  # Print a blank line


main()# Call the main function to execute the program