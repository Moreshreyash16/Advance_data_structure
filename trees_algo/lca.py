'''
@Author: Shreyash More

@Date: 2023-06-20 21:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-20 21:34:30

@Title : Write a program to find lowest common ancestor

'''
class Bst():
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None
    
    def insert(self, data):
        """
        Description:
            It inserts data in the tree
        Parameter:
            data: Takes data as input
        Return:
            None
        """
        if self.key is None:
            self.key = data
            return
        elif data < self.key:
            if self.left_child:
                self.left_child.insert(data)
            else:
                self.left_child = Bst(data)
        
        elif data > self.key:
            if self.right_child:
                self.right_child.insert(data)
            else:
                self.right_child = Bst(data)

    def post_order(self):
        """
        Description:
            It prints value in post order
        Parameter:
            None
        Return:
            None
        """
        if self.left_child:
            self.left_child.post_order()
        
        if self.right_child:
            self.right_child.post_order()
        
        print(self.key, end=" ")

    
    def lowest_common_ance(self, node1, node2):
        """
        Description:
            It finds lowest common ancestor
        Parameter:
            node1: Takes node as input
            node2: Takes node as input
        Return:
            root value
        """
        if self.key is None:
            return None
        
        if self.key == node1 or self.key == node2:
            return self.key

        if self.left_child is None and self.right_child is None:
            return None

        left_side = None
        right_side = None

        if self.left_child:
            left_side = self.left_child.lowest_common_ance(node1, node2) 

        if self.right_child:
            right_side = self.right_child.lowest_common_ance(node1, node2) 

        if left_side and right_side:
            return self.key

        if left_side:
            return left_side

        if right_side:
            return right_side

        return None


def main():
    binary = Bst(None)
    list1 = [3, 5, 1, 6, 2, 0, 8, 7, 4, 9]
    for i in list1:
        binary.insert(i)
    binary.post_order()
    ancestor = binary.lowest_common_ance(7, 9)
    print("Lowest Common Ancestor:", ancestor)

if __name__ == "__main__":
    main()
