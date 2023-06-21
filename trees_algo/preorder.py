'''
@Author: Shreyash More

@Date: 2023-06-20 21:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-20 21:34:30

@Title : Write a program to do a implement bst

'''
class Bst():
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
                self.left_child=Bst(data)
        
        elif data>self.key:
            if self.right_child:
                self.right_child.insert(data)
            else:
                self.right_child=Bst(data)

    def pre_order(self):
        """
        Description:
            It prints value in post order
        Parameter:
            None
        Return:
            None
        """
        print(self.key,end="")
        if self.left_child:
            self.left_child.post_order()
        
        if self.right_child:
            self.right_child.post_order()
        




def main():
    binary=Bst(None)
    list1=[8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    for i in list1:
        binary.insert(i)
    binary.pre_order()

if __name__=="__main__":
    main()