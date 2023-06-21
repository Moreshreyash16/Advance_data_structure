'''
@Author: Shreyash More

@Date: 2023-06-20 21:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-20 21:34:30

@Title : Write a program to implement a binary search tree (BST)

'''
class Bst():
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None
    
    def insert(self, data):
        """
        Description:
            Inserts data into the tree
        Parameter:
            data: The data to be inserted
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
    
    def search_tree(self, value):
        """
        Description:
            Searches for a value in the tree
        Parameter:
            value: The value to search for
        Return:
            Boolean value indicating whether the value was found or not
        """
        if self.key == value:
            print("Node was found")
            return True
        elif value < self.key:
            if self.left_child:
                self.left_child.search_tree(value)
        
        elif value > self.key:
            if self.right_child:
                self.right_child.search_tree(value)
        
        else:
            print("Value not found")
            return False
    
    def delete_node(self, value):
        """
        Description:
            Deletes a node from the tree
        Parameter:
            value: The value of the node to be deleted
        Return:
            None
        """
        if self.key is None:
            print("Tree is empty")
            return
        
        # Node to be deleted is in the left subtree
        if value < self.key:
            if self.left_child:
                self.left_child = self.left_child.delete_node(value)
            else:
                print("Value not found in the tree")
        
        # Node to be deleted is in the right subtree
        elif value > self.key:
            if self.right_child:
                self.right_child = self.right_child.delete_node(value)
            else:
                print("Value not found in the tree")
        
        # Node to be deleted is the current node
        else:
            # Case 1: Node has no child or only one child
            if self.left_child is None:
                temp = self.right_child
                self = None
                return temp
            elif self.right_child is None:
                temp = self.left_child
                self = None
                return temp
            
            # Case 2: Node has two children
            successor = self.right_child.get_min_value()
            self.key = successor
            self.right_child = self.right_child.delete_node(successor)
        
        return self
    
    def get_min_value(self):
        """
        Description:
            Finds the minimum value in the subtree rooted at the current node
        Parameter:
            None
        Return:
            The minimum value in the subtree
        """
        if self.left_child is None:
            return self.key
        else:
            return self.left_child.get_min_value()


def main():
    binary = Bst(None)
    list1 = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    for i in list1:
        binary.insert(i)
    
    binary.search_tree(15)
    
    # Delete a node from the tree
    value_to_delete = 10
    binary = binary.delete_node(value_to_delete)
    print("Tree after deleting node with value", value_to_delete)
    binary.search_tree(value_to_delete)


if __name__ == "__main__":
    main()
