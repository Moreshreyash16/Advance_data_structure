'''
@Author: Shreyash More

@Date: 2023-06-20 15:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-20 15:34:30

@Title : Write a program to Bubble sort

'''
def bubble_sort(arr):
    """
    Description:
        It takes an array and sorts it
    Parameter:
        arr: Takes array as input
    Return:
        Returns the sorted list
    """
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def main():
    arr = list(map(int,input("Enter elemnts to sort ").split()))
    print(f"The original array is {arr} and the sorted array is {bubble_sort(arr)}")

if __name__=="__main__":
    main()
