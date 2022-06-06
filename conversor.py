#Lets convert quetzales (Qs) into dolars ($) and viceversa

from typing import final

#If the user wants to exchange quetzales to dollars


def exchange_quetzales_to_dollars(quetzales):
    
    dollars_final = quetzales/value_dolars
    round(dollars_final, 2)

    return dollars_final

#If the user wants to exchange dollars to quetzales    

def exchange_dollars_to_quetzales(dollars):

    quetzales_final = value_dolars*dollars
    round(quetzales_final, 2)

    return quetzales_final

#This will be our MAIN

value_dolars = 7.5

print("Welcome to my conversor!\n")

user_input = 0

while (user_input != 1 or user_input !=2):

    user_input = int(input("Type 1 if you would like to exchange quetzales to dollars. Type 2 if you would like to exchange dollars to quetzales.\n"))

    if user_input == 1:

        quetzales = int(input("How many quetzales do you want to exchange?\n"))
        print("\nNice, we'll do the exchange for Q" + str(quetzales) + "!")

        final_result = exchange_quetzales_to_dollars(quetzales)

        final_result = round(final_result,2)

        print("If you exchange Q" + str(quetzales) + " you'll have $" + str(final_result) + "!")
        print("*-*-*Thanks for using my conversor!*-*-*")
        break

    elif user_input == 2:
        
        dollars = int(input("How many dollars do you want to exchange?\n"))
        print("\nNice, we'll do the exchange for $" + str(dollars) + "!")

        final_result = exchange_dollars_to_quetzales(dollars)

        final_result = round(final_result,2)

        print("If you exchange $" + str(dollars) + " you'll have Q" + str(final_result) + "!")
        print("*-*-*Thanks for using my conversor!*-*-*")
        break

    else:
        print("Please choose a valid option (1 or 2)\n")
        
        
