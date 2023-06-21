'''
@Author: Shreyash More

@Date: 2023-06-21 00:30:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-21 00:30:30

@Title : Write a program to selectio sort

'''
def selection_sort(arr):
    """
    Description:
        Sorts an array using the Selection Sort algorithm.
    Parameters:
        arr (list): The input list to be sorted.
    Returns:
        array.
    """
    n = len(arr)

    for i in range(n-1):
        # Find the minimum element in the remaining unsorted part
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

def main():
    arr = list(map(int,input("Enter elemnts to sort ").split()))
    print(f"The original array is {arr} and the sorted array is {selection_sort(arr)}")

if __name__=="__main__":
    main()
