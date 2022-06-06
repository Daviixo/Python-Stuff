import random

def dicegame(numero, random_number):

    #Esto es para hacer trampa en el juego. 
    print("Estoy en dicegame:\nEl valor de numero es: " 
    + str(numero) + " y el valor de random es: " + str(random_number))
    
    if random_number == numero:
        return True
    else:
        return False


def main():
    icont = 0

    print("""
    
Bienvenido al adivina adivinador! Debes ingresar un numero del 1 al 10 para jugar.   
    
    """)

    random_number = random.randint(1,10)

    is_numero = False

    while is_numero == False:
        print("-----")
        numero = int(input("Trata de adivinar el numero que da la maquina :3 (1 al 10)\n"))
        is_numero = dicegame(numero, random_number)
        print("is_numero: " + str(is_numero))

        if is_numero == True:
            break

        icont += 1
        print("Vas por el intento: " + str(icont))

        if(icont == 3):
            print("\nYou lost :c")
            break

        continue
    
    if is_numero == True:
        print("\nYOU WOOON!")
    else:
        print("\nGame over :c")


if __name__ == "__main__":
    main()