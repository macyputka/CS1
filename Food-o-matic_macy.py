import random

foods = ["cauliflower","tilapia fillet","pork loin","green beans","rainbow carrots", "potatoes","three color squash","eggplant","eye round of beef","baguette"]#Parallel array created by a list of items
toppings = ["with balsamico","with garlic and olive oil","with minted yogurt","soup","chutney","salad","with salsa","over sticky rice","au jus","with basmati rice"]#Parallel array created by a list of items
price = [6, 35, 21, 13, 8, 8, 11, 9, 29, 7]#parallel array created by a list of items

while True:#loop of code indented below
    try:
        number_of_items = int(input("Hungry? Enter how many items you need!"))#Waiting for users imput (in numbers) in response to prompt 
        break#break or space in code for bettering viewing
    except ValueError:#code will pull out any error and if they do a different code it given next
        print("Hey enter an integer please!")#print text and restart while true loop

total_cost = 0#telling code that total cost will start at 0, then might change throughout code 

for i in range(number_of_items):#dentifies the loop then identifies the variable(and how many times has it iterated through the loop?),Connects the variable to the “list”,Identifies the “list” (how many times will it iterate through the loop?)

    food = random.choice(foods)#select a the users input number and select that number of pairs randomly from the parallel array
    print(f"{food} {random.choice(toppings)}, which will cost you ${price[foods.index(food)]}")#print and show reader three different items with their pair and price
    total_cost += price[foods.index(food)]#add the prices of all given items together 
print(f"Your total cost is ${total_cost}")#show user calculated prices 
    
