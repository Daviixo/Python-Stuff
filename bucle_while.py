def main():
    
    LIMIT = 1000
    icont = 0
    potencia_2 = 2**icont

    while potencia_2 < LIMIT:
        print("2 elevado a " + str(icont) + " es " + str(potencia_2))
        icont = icont + 1
        potencia_2 = 2**icont


if __name__ == "__main__":
    main()