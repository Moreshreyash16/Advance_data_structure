'''
@Author: Shreyash More

@Date: 2023-06-21 14:22:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-21 14:22:30

@Title : Write a program to implement breadth first search

'''
from collections import deque
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        """
        Description:
            It inserts data in tree
        Parameter:
            val: Takes data as input
        Return:
            None
        """
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def breadth_first_search(root):
    """
        Description:
            It does depth first search 
        Parameter:
            root: Takes root node as input
        Return:
            prints the data 
    """
    que = []
    que.append(root)
    while que:
        temp = que.pop(0)
        print(temp.info, end = ' ')
        if temp.left != None:
            que.append(temp.left)
        if temp.right != None:
            que.append(temp.right)

        

def main():
    tree = BinarySearchTree()
    
    arr = list(map(int, input("Enter nodes value : ").split()))

    for i in arr:
        tree.create(i)

    breadth_first_search(tree.root)

if __name__=="__main__":
    main()