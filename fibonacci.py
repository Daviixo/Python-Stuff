def main(a):

    x = 1
    y = 1
    z = 1
    print(0)
    print(1)
    for i in range(a):
        x = z
        z += y
        y = x
    print(y)

if __name__ == "__main__":
    a = int(input("How many fibonacci numbers do you want?\n"))
    main(a)
