'''
@Author: Shreyash More

@Date: 2023-06-20 15:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-20 15:34:30

@Title : Write a program to do queue operation

'''

# queue push operations
def enqueue(queue,value):
    """
    Description:
        It adds value to queue
    Parameter:
        queue: Takes queue as input
        value: Takes value as input
    Return:
        None
    """
    queue.append(value)

#queue pop operations
def dequeue(queue):
    """
    Description:
        It removes value from  queue
    Parameter:
        queue: Takes queue as input
    Return:
        A boolean value
    """
    if queue:
        queue.pop(0)
    else:
        print("queue is empty")
        return False
# checking if queue is empty or not
def queue_empty(queue):
    """
    Description:
        It check if queue is empty or not
    Parameter:
        queue: Takes queue as input
    Return:
        A boolean value
    """
    if queue:
        print("Not empty")
        return True
    else:
        print("empty")
        return False

def main():
    queue = []
    value=int(input("Enter value"))
    enqueue(queue,value)
    dequeue(queue)
    queue_empty(queue)
    

if __name__=="__main__":
    main()
