def is_palindromo():
    palabra_o_frase = input("\nIngresa tu palabra o tu frase\n")
    palabra_o_frase = palabra_o_frase.lower()
    palabra_o_frase = palabra_o_frase.replace(" ", "")
    temp = palabra_o_frase

    palabra_o_frase = palabra_o_frase[::-1]

    print("\nResultado de tu palabra o frase al reves sin espacios y en minusculas: " + palabra_o_frase)

    if(temp == palabra_o_frase):
        print("\nSi es! :3")
    else:
        print("\nNo es :c")    

#This will be our main

is_palindromo()
