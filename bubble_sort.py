import random as rd

def bubbleSort(arr):

    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
 

if __name__ == "__main__":

    numbers_list = (range(1,100))

    arr = []

    final_range = input("Array's range?\n")

    print(f"\nAdding {final_range} numbers\n")

    for i in range(int(final_range)):
        random_number = rd.choice(numbers_list)
        print(f"Number added to the array: {random_number}\n")
        arr.append(random_number)

    bubbleSort(arr)
 
    print("Sorted array is:\n")
    for i in range(len(arr)):
        print("%d" % arr[i], end="\n")