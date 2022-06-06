def check_palindromo(palabra_frase):
    palabra_frase = palabra_frase.lower().replace(" ", '')
    palabra_invertida = palabra_frase[::-1]
    if palabra_frase == palabra_invertida:
        return True
    else:
        return False


def main():
    print("""
    
Veamos si vuestra palabra o frase es o no es palindromo!    
    
    """)
    palabra_frase = input("Ingresa la palabra o frase :3\n")
    is_palindromo = check_palindromo(palabra_frase)
    if is_palindromo == True:
        print("Si es palindromo! :3")
    else:
        print("No es palindromo :c")     


if __name__ == '__main__':
    main()
