'''
@Author: Shreyash More

@Date: 2023-06-20 15:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-20 15:34:30

@Title : Write a program to do a reverse a string using stack 

'''

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
    length=len(stack)
    string=""
    if stack:
        for i in range(length):
            string+=stack.pop()
        return string
    else:
        print("stack is empty")
        

def stack_push(value):
    """
    Description:
        It adds value to stack
    Parameter:
        stack: Takes stack as input
        value: Takes value as input
    Return:
        None
    """
    stack=[]
    if value:
        for i in value:
            stack.append(i)
        return stack
    else:
        return 0


def main():
    word=input("Enter a string ")
    stack=stack_push(word)
    for i in range(len(stack)):
        print(stack.pop())
    
    

if __name__=="__main__":
    main()
