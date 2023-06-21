'''
@Author: Shreyash More

@Date: 2023-06-20 15:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-20 15:34:30

@Title : Write a program to merge sort

'''
def merge(arr):
    """
    Description:
        It takes an array and splits the array in two part and recursiveky sort the left part and right part
    Parameter:
        arr: Takes array as input
    Return:
        Returns the array
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge(left)
    right = merge(right)
    return merge_list(left, right)


def merge_list(a, b):
    """
    Description:
        It takes an array and splits the array in two part and recursiveky sort the left part and right part
    Parameter:
        a: Takes left part of array as input
        b: Takes right part of array as input
    Return:
        Returns the sorted list
    """
    left_list1 = len(a)
    right_list2 = len(b)
    i = 0
    j = 0
    sorted_list = []
    while i < left_list1 and j < right_list2:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    while i < left_list1:
        sorted_list.append(a[i])
        i += 1
    while j < right_list2:
        sorted_list.append(b[j])
        j += 1
    return sorted_list


def main():
    arr = list(map(int,input("Enter elemnts to sort ").split())) 
    print(f"The original array is {arr} and the sorted array is {merge(arr)}")

if __name__=="__main__":
    main()

