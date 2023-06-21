'''
@Author: Shreyash More

@Date: 2023-06-21 14:22:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-21 14:22:30

@Title : Write a program to reverse a element using another queue

'''

# Python3 implementation of the above approach
from collections import deque

# Function to return the reversed queue
def reverse(que):
	"""
    Description:
        It reverse a queue
    Parameter:
        queue: Takes queue as input
    Return:
        A queue
    """
	l = len(que)
	temp_queue = deque()
	
	for i in range(l):
		temp_queue.appendleft(que.popleft())
	return temp_queue


def main():
    original_queue= deque()
    queue = list(map(int, input("Enter elements in the queue: ").split()))
    for i in queue:
        original_queue.append(i)

    original_queue = reverse(original_queue)

    # Print the queue
    while (len(original_queue) > 0):
        print(original_queue.popleft(), end = " ")


if __name__ == '__main__':
    main()
