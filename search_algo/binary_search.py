'''
@Author: Shreyash More

@Date: 2023-06-21 00:54:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-21 00:54:30

@Title : Write a program to do a binary search

'''

def binary_search(arr, value):
    """
    Description:
        It takes an array and sorts it
    Parameter:
        arr: Takes array as input
    Return:
        Returns the sorted list
    """
    lo = 0
    hi=len(arr)-1
    if value>max(arr):
        return 0
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = arr[mid]
        if mid_number == value:
            return mid
        elif mid_number < value:
            lo = mid + 1    
        elif mid_number > value:
            hi = mid - 1 
    if value not in arr:
        print(mid,mid_number)
        if value<mid_number:
            return mid-1
        else:
            return mid+1

def main():
    arr= list(map(int,input("Enter elemnts to in array ").split())) 
    arr=sorted(arr)
    value=int(input("Enter value to find : "))
    print(f"The {value} in {arr} is at {binary_search(arr,value)} poistion")
    

if __name__=="__main__":
    main()
    

