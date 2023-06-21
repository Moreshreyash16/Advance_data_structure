'''
@Author: Shreyash More

@Date: 2023-06-20 21:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-20 21:34:30

@Title : Write a program to do a a infix to postfix operation

'''
def infix_to_postfix(expression):
    """
    Description:
        It converts infix to postfix
    Parameter:
        expression: It takes expression as input
    Return:
        None
    """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    postfix = []
    stack = []

    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence[char] <=precedence.get(stack[-1], 0):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)


def main():
    infix_expression = input("Enter an infix expression: ")
    postfix_expression = infix_to_postfix(infix_expression)
    print("Postfix expression:", postfix_expression)


if __name__ == "__main__":
    main()
