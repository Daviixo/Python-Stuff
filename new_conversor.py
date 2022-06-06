#Let's create a conversor :3

from tkinter import Menu


def money_conversor(value_in_dollars, currency):
    money = input("How many " + currency + " have you got?\n")
    money = float(money)
    dollars = money / value_in_dollars
    dollars = round(dollars,2)

    print("You'll have $" + str(dollars) + " with the currency: " + currency)

b_continue = False

while(b_continue == False):

    menu = """

Welcome to your currency converter!

Select your currency:

1.- Quetzales
2.- Pesos mexicanos
3.- Euros

What will you choose?
"""    

    menu_option = int(input(menu))

    if menu_option == 1:
        money_conversor(7.5, "quetzales")

    elif menu_option == 2:
        money_conversor(19.98, "mexican pesos")

    elif menu_option == 3:
        money_conversor(0.90, "euros")

    else:
        print("Dude, choose the right option (1,2,3)")

    user_continue = ""

    while(user_continue != "Y" or user_continue !="N" and b_continue != True):
        user_continue = input("\nWould you like to do another conversion? (Y/N)\n")
        #print("user_continue = " + user_continue)
        #print("b_continue = " + str(b_continue))

        if(user_continue == "N"):
            b_continue = True
            print("\nThanks for choosing Daviixo's conversor! :3")
            break
        else:
            print("\nSure, let's do another one! :3")
            b_continue = False
            #print("user_continue = " + user_continue)
            #print("b_continue = " + str(b_continue))
            break
        