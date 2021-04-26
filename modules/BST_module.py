import sys

class Node:

    def __init__(self, key = None,value=None, left = None, right = None, parent = None):
        self.key = key
        self.value=value
        self.left = left
        self.right = right
        self.parent = parent

class BST:

    def __init__(self, root = None):
        self.root = root
        
    def search_key(self, key):
        """searches for the key through out the tree"""
        
        current_node = self.root
        while current_node is not None and key != current_node.key:
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return current_node
    
    def getmin(self):
        """Returns the node with the minimum key"""
        current_node = self.root
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def getmax(self):
        """Returns the node with the maximum key"""
        current_node = self.root
        while current_node.right is not None:
            current_node = current_node.right
        return current_node
    
    def successor_key(self,key):
        """The successor of a current node is the node with smallest key greater than current key"""
        current_node=self.search_key(key)
        if current_node.right is not None:
            return BST(current_node.right).getmin().key
        
        parent_node=current_node.parent
        while parent_node is not None:
            if current_node != parent_node.right:
                break
            current_node=parent_node
            parent_node=parent_node.parent
        return parent_node.key
    
    def predecessor_key(self,key):
        """The predecessor of a current node is the node with largest key less than current key"""
        current_node = self.search_key(key)
        if current_node.left is not None:
            return BST(current_node.left).getmax().key
        parent_node = current_node.parent
        while parent_node is not None:
            if current_node != parent_node.left:
                break
            current_node = parent_node
            parent_node = parent_node.parent
        return parent_node.key

    def insert_key(self, key,val):
        """ inserts the key to BSTree"""
       
        node = Node(key,val)
        parent_node = None
        current_node = self.root
        while current_node is not None:
            parent_node = current_node
            if node.key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        if parent_node is None:
            self.root=node
        elif node.key < parent_node.key:
            parent_node.left=node
        else:
            parent_node.right=node
        node.parent=parent_node

    def delete_key(self, key):
        """ deletes the key from BSTree"""
        
        node = self.search_key(key)
        if node is None:
            return
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            successor = BST(node.right).getmin()
            if successor.parent is not node:
                self.transplant(successor, successor.right)
                successor.right=node.right
            self.transplant(node, successor)
            successor.left=node.left

    def transplant(self, x, y):
        """Replaces subtree rooted at node x with subtree rooted at node y"""
        if x.parent is None:
            self.root=y
        elif x is x.parent.left:
            x.parent.left=y
        else:
            x.parent.right=y
    
    
    
    def print_tree_inorder(self):
        """prints the inorder sequence while traversing"""
        stack = []
        #keys = []
        current = self.root
        while len(stack) > 0 or current is not None:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop(-1)
                #keys.append(current.key)
                sys.stdout.write("{"+current.key+" : "+str(current.value)+"}\n")
                current = current.right
        
    
    def increase_value(self,key):
        """Increases the value of the key by 1"""
        
        required_node=self.search_key(key)
        required_node.value=required_node.value+1
    



