#****************************************************************
#Name: GOODNEWS GOODNEWS

#
#ANA1001 Lab 5
#****************************************************************


#Question Number 1

'''Create a dictionary to store six pieces of information about yourself. Store things like your first name, last name, favourite pizza topping, and the city in which you live. You should have keys such as first_name, last_name, age, city and so on. Print each piece of information stored in your dictionary using a for loop and .items().'''

#Creating dictionary to store six pieces of Information.
info = {"first name":"Goodnews", 
        "last name":"Agbadu","age":27,
        "school":"Cambrian",
        "city":"Sudbury",
        "favourite food":"Cake"
        }

#printing out information using a for loop
for key, value in info.items():
  print(f"{key.title()} - {value}")

#Question Number 2

'''Use a dictionary to store five classmates and their favourite colours. Each classmate (the key) should have at least three colours (the value) stored in a list. Use a for loop to print each person’s name and their favourite colour.'''


#Using a dictionary to store five classmates and their favourite colours.
classmates = {"oluchi":["green", "red", "yellow"], "sharon":["black", "red", "yellow"],"victor":["white", "red", "yellow"],"ziggy":["orenge", "red", "yellow"],"sam":["pink", "red", "yellow"]}
for key, value in classmates.items():
  print(f"{key.title()} favourite colours are : {value[0].title()},{value[1].title()} and {value[2].title()}.")

#Question Number 3
'''Make several dictionaries, where each dictionary represents a different person. In each dictionary, include the persons choice of food( for example, eggs) and meal (for example, breakfast). Store these dictionaries in a list called meals. Next, loop through your list of dictionaries using a for loop, and as you do, print everything you know about each person, meal and food in a readable format. Refrain from printing out whole dictionaries.'''


#dictionaries including the persons choice of food and meal
goodnews = {"name":"Goodnews","food":"rice","meal":"dinner"}
oluchi = {"name":"Oluchi","food":"beans","meal":"breakfast"}
sharon = {"name":"Sharon","food":"yam","meal":"lunch"}

#Storing these dictionaries in a list called meals
meals = [goodnews,oluchi,sharon]
#using a for loop to loop through the dictionary 
for meal in meals:
  print(f"{meal['name']} favourite food is {meal['food'].title()}, but would love to have icecream for {meal['meal'].title()}")


#Question Number 4
'''Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a sub dictionary of information about each city and include the country that the city is in, its approximate population, and three facts about that city. The keys for each city’s dictionary should be something like country, population, and facts, but you are welcome to make up your own keys and values that describe the city. Print the name of each city and all of the information you have stored about it.'''

#dictionary called cities
cities = {
          "Sudbury":{"location":"Ontario Canada","population":20000,"facts":"Nature"},
          "New York":{"location":"USA","population":50000,"facts":"business Hub"},
          "Lagos":{"location":"Nigeria","population":4000,"facts":"Music"}
          }

for key,value in cities.items():
  print(f"{key} is a city in {value['location']}, it has {value['population']} people and one fact about the city is: {value['facts']}.")#Printing the name of each city and all of the information stored about it.


#question Number 5
'''Make a dictionary called stock_prices and put three keys (stock names) into it. The values should be lists that contain 10 stock prices for each stock. Using a for loop, print out the name and the average price for each stock. '''
from statistics import mean
stock_prices = {"Facebook":[20,30,40,50,60,70,80,90,100,111],"tesla":[22,39,41,52,60,77,98,90,134,111],"apple":[22,32,48,54,65,76,87,98,109,111],
              }
for key,value in stock_prices.items():
  avg = mean(value)
  print(f"{key.title()}: average stock price is {avg}")


#Question Number 6
'''You are running for president. Build an election simulator. 

In your program, use a for loop to run the program five times. Create a variable for popularity score that starts at 0. Within each loop, create an event (print something about the event), and at each of the events add a random amount of approval to the overall total. Show (print out) what happens at each step (print how much popularity was gained), and let the user know the final result (if the candidate has over 50% of the vote they win, otherwise they lose).

For example:

Adi gives a speech and earns 15% popularity! The popularity is now 15 %.
Adi gives a speech and earns 16% popularity! The popularity is now 31 %.
Adi gives a speech and earns 20% popularity! The popularity is now 51%.
Adi gives a speech and earns 5% popularity! The popularity is now 56%.
Adi gives a speech and loses 10% popularity! The popularity is now 46%.
Since the popularity is not more than 50% Adi is not the president :(

Make sure each step prints out a sentence explaining what is happening and shows the final results.'''

import random
#creating  main to run the program 
def main():
#creating variables 
    popularity = 0
    total = 0
    x =  random.randint(1,10)

#for loop iterates 5 times
    for i in range(0 , 5):
        
#generating the popularity value  and sum to the overall total
        if(x > 0):
            total = total + x
            
                 
            print("\nGoodnews gives a speech and earns "+str(x)+"% popularity! The popularity is now "+str(total)+" %")    
        else:
            total = total + x

            if(total < 0):
                total = 0
                
            print("\nGoodnews gives a speech and loses "+str(x)+"% popularity! The popularity is now "+str(total)+" %")    
            
        x =  random.randint(-8,20)

#if the popularity exceeded 50 then Ade wins else loses  
    if( total < 50 ):
        print("Since the popularity is not more than 50% Goodnews is not the president :(")
    else:
        print("Since the popularity is more than 50% Goodnews is the president :)")
main()