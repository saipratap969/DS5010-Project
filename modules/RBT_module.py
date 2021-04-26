import sys

from enum import Enum
class Color(Enum):
    RED = 1
    BLACK = 0
    
class Node():
    
    def __init__(self,key,value=1,parent =None,left=None,right=None,color=Color.RED):
        self.key = key
        self.value = value
        self.pnt = parent
        self.left = left
        self.right = right
        self.color = color
                
class RBT:
    
    
    
    def __init__(self):
        self.sentinel = Node(0)
        self.sentinel.color = Color.BLACK
        self.sentinel.left = None
        self.sentinel.right = None
        self.root = self.sentinel 
        self.arr = []
       
        
    def search_helper(self, node, key):
        """Recursively searches tree for node whose key is equal to given key"""
        
        if node == self.sentinel or key == node.key:
            return node
        if key < node.key:
            return self.search_helper(node.left, key)
        return self.search_helper(node.right, key)
    
    def in_order(self, node):
        """prints the inorder sequence while traversing"""
        
        if node != self.sentinel:
            self.in_order(node.left)
            self.arr.append(str(node.key)+':'+str(node.value))
            sys.stdout.write(str(node.key)+':'+str(node.value) + "\n")
            self.in_order(node.right)
            

    def rb_insert_fixup(self, node):
        """function maintains the property of RBTree after insertion """
        
        while node.pnt.color == Color.RED:
            if node.pnt == node.pnt.pnt.left:
                y = node.pnt.pnt.right
                if y.color == Color.RED:
                    y.color = Color.BLACK
                    node.pnt.color = Color.BLACK
                    node.pnt.pnt.color = Color.RED
                    node = node.pnt.pnt
                else:
                    if node == node.pnt.right:
                        node = node.pnt
                        self.left_rotate(node)
                    node.pnt.color = Color.BLACK
                    node.pnt.pnt.color = Color.RED
                    self.right_rotate(node.pnt.pnt)
            else:
                y = node.pnt.pnt.left
                
                if y.color == Color.RED:
                    y.color = Color.BLACK
                    node.pnt.color = Color.BLACK
                    node.pnt.pnt.color = Color.RED
                    node = node.pnt.pnt
                else:
                    if node == node.pnt.left:
                        node = node.pnt
                        self.right_rotate(node)
                    node.pnt.color = Color.BLACK
                    node.pnt.pnt.color = Color.RED
                    self.left_rotate(node.pnt.pnt)
            if node == self.root:
                break
        self.root.color = Color.BLACK

    def rb_delete_fixup(self, x):
        """maintains the property of RBTree after deletion"""
        
        while x != self.root and x.color == 0:
            if x == x.pnt.left:
                s = x.pnt.right
                if s.color == 1:
                    s.color = 0
                    x.pnt.color = 1
                    self.left_rotate(x.pnt)
                    s = x.pnt.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.pnt
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.pnt.right

                    s.color = x.pnt.color
                    x.pnt.color = 0
                    s.right.color = 0
                    self.left_rotate(x.pnt)
                    x = self.root
            else:
                s = x.pnt.left
                if s.color == 1:
                    s.color = 0
                    x.pnt.color = 1
                    self.right_rotate(x.pnt)
                    s = x.pnt.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.pnt
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.pnt.left

                    s.color = x.pnt.color
                    x.pnt.color = 0
                    s.left.color = 0
                    self.right_rotate(x.pnt)
                    x = self.root
        x.color = 0



    def rb_transplant(self, u, v):
        """Replaces subtree rooted at node u with subtree rooted at node v"""
        if u.pnt == None:
            self.root = v
        elif u == u.pnt.left:
            u.pnt.left = v
        else:
            u.pnt.right = v
        v.pnt = u.pnt




    def delete_key(self, node, key):
        """ deletes the key from RBTree"""
        z = self.sentinel
        while node != self.sentinel:
            if node.key == key:
                z = node

            if node.key <= key:
                node = node.right
            else:
                node = node.left

        if z == self.sentinel:
            print("Cannot find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.sentinel:
            x = z.right
            self.rb_transplant(z, z.right)
        elif (z.right == self.sentinel):
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.min(z.right)
            y_original_color = y.color
            x = y.right
            if y.pnt == z:
                x.pnt = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.pnt = y

            self.rb_transplant(z, y)
            y.left = z.left
            y.left.pnt = y
            y.color = z.color
        if y_original_color == 0:
            self.rb_delete_fixup(x)
         
    def sort(self):
        """prints all the keys with the values in sorted order"""
        self.arr = []
        self.in_order(self.root)

        return self.arr
        
    def min(self, node):
        """Returns the node with the minimum key"""
        while node.left != self.sentinel :
            node = node.left
        return node
    
    def max(self, node):
        """Returns the node with the minimum key"""
        while node.right != self.sentinel:
            node = node.right
        return node
    
    def search_key(self, key):
        """searches and returns the key using search_helper"""
        return self.search_helper(self.root, key)

    def predecessor_key(self, x):
        """The predecessor of a node x is the node with largest key less than x.key"""
        if (x.left != self.sentinel):
            return self.max(x.left)
        
        pnt = x.pnt
        while pnt != self.sentinel and pnt.left == x:
            x = pnt
            pnt = pnt.pnt
        return pnt
        

    def successor_key(self, x):
        """The successor of a node x is the node with smallest key greater than x.key"""
                
        if x.right != self.sentinel:
            return self.min(x.right)
        
        pnt = x.pnt
        while pnt != self.sentinel:
            if x != pnt.right:
                break
            x = pnt            
            pnt = pnt.pnt
        return pnt
        

    def left_rotate(self, x):
        """positions of nodes of subtree are interchanged"""
        y = x.right
        x.right = y.left
        if y.left != self.sentinel:
            y.left.pnt = x
            
        y.pnt = x.pnt
        if x.pnt == None:
            self.root = y
        elif x == x.pnt.left:
            x.pnt.left = y
        else:
            x.pnt.right = y
            
        y.left = x
        x.pnt = y
 
        
    def right_rotate(self, x):
        """positions of nodes of subtree are interchanged"""
        y = x.left
        x.left = y.right
        if y.right != self.sentinel:
            y.right.pnt = x
            
        y.pnt = x.pnt
        if x.pnt == None:
            self.root = y
        elif x == x.pnt.right:
            x.pnt.right = y
        else:
            x.pnt.left = y
            
        y.right = x
        x.pnt = y
  
        
    def insert_key(self, key):
        """inserts a key into RBTree"""
        
        if key == self.search_key(key).key:
             (self.search_key(key)).value += 1
             return
        else: 
             node = Node(key,1,None,self.sentinel,self.sentinel,Color.RED)
             y = None
             x = self.root

             while x != self.sentinel:
                y = x
                if node.key < x.key:
                    x = x.left
                else:
                    x = x.right
            
             node.pnt = y
             if y == None:
                self.root = node
             elif node.key < y.key:
                y.left = node
             else:
                 y.right = node
            
             if node.pnt == None:
                node.color = Color.RED
                return
        
             if node.pnt.pnt == None:
                 return
        
             self.rb_insert_fixup(node)

        



