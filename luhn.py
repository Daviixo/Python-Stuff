def checkLuhn(credit_card_no):
     
    nDigits = len(credit_card_no)
    nSum = 0
    isSecond = False
     
    for i in range(nDigits - 1, -1, -1):
        d = ord(credit_card_no[i]) - ord('0')

        print("Our D current value is: " +  str(d))

        print("Now, we convert the character into unicode:")
        print(str(d) + "\n")

        if (isSecond == True):
            d = d * 2
            print("Our D(2) current value is: " +  str(d))

  
        nSum += d // 10
        print("nSum1: " + str(nSum))
        nSum += d % 10
        print("nSum2: " + str(nSum))
  
        isSecond = not isSecond
     
    if (nSum % 10 == 0):
        return True
    else:
        return False
 
#This will be our main.
if __name__=="__main__":
     
    #Valid card: "79927398713"

    credit_card_no = input("Please type in your CC\n")

    if (checkLuhn(credit_card_no)):
        print("This is a valid card #")
    else:
        print("This is not a valid card #")