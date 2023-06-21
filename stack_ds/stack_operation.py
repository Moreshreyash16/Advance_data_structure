'''
@Author: Shreyash More

@Date: 2023-06-20 15:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-20 15:34:30

@Title : Write a program to do stack operation

'''

# stack push operations
def stack_push(stack,value):
    """
    Description:
        It adds value to stack
    Parameter:
        stack: Takes stack as input
        value: Takes value as input
    Return:
        None
    """
    stack.append(value)

#stack pop operations
def stack_pop(stack):
    """
    Description:
        It removes value to stack
    Parameter:
        stack: Takes stack as input
    Return:
        A boolean value
    """
    if stack:
        stack.pop()
    else:
        print("stack is empty")
        return False
# checking if stack is empty or not
def stack_empty(stack):
    """
    Description:
        It check if stack is empty or not
    Parameter:
        stack: Takes stack as input
    Return:
        A boolean value
    """
    if stack:
        print("Not empty")
        return True
    else:
        print("empty")
        return False

def main():
    stack = []
    value=int(input("Enter value"))
    stack_push(stack,value)
    stack_pop(stack)
    stack_empty(stack)
    

if __name__=="__main__":
    main()
