'''
@Author: Shreyash More

@Date: 2023-06-21 14:22:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-21 14:22:30

@Title : Write a program to implement depth first search

'''
class BinaryTree():
    def __init__(self,key):
        self.key=key
        self.left_child=None
        self.right_child=None
    
    def insert(self,data):
        """
        Description:
            It inserts data in tree
        Parameter:
            data: Takes data as input
        Return:
            None
        """
        if self.key==None:
            self.key=data
            return
        elif data<self.key:
            if self.left_child:
                self.left_child.insert(data)
            else:
                self.left_child=BinaryTree(data)
        
        elif data>self.key:
            if self.right_child:
                self.right_child.insert(data)
            else:
                self.right_child=BinaryTree(data)

    def depth_first_search(self):
        """
        Description:
            It does depth first search 
        Parameter:
            None
        Return:
            prints the data 
        """
        print(self.key,end="")
        if self.left_child:
            self.left_child.depth_first_search()
        
        if self.right_child:
            self.right_child.depth_first_search()
        

def main():
    binary_tree=BinaryTree(None)
    list1=[8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    for i in list1:
        binary_tree.insert(i)
    binary_tree.depth_first_search()

if __name__=="__main__":
    main()