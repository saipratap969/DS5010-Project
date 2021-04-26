from BST_module import BST

import unittest

def test_cleaning(text):
    
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for ele in text: 
        if ele in punc: 
            text = text.replace(ele, "")
            
    text = text.lower()
    text = text.split(' ')
    return text

def test_BST_instance():
    bst = BST()
    
    text = """Alice was beginning to get very tired, literally very very tired"""
    
    text = test_cleaning(text)
    
    for word in text:
        bst.insert_key(word,1)
    
    return bst
        
class test_BST(unittest.TestCase):
    
    
    def test_getmin(self):
        x = test_BST_instance()
        y = 'alice'
        self.assertEqual(x.getmin().key,y)
    
    def test_getmax(self):
        x = test_BST_instance()
        y = 'was'
        self.assertEqual(x.getmax().key,y)        
    
    def test_search_key(self):
        x = test_BST_instance()
        self.assertTrue('alice' in (x.search_key('alice').key))
        self.assertFalse('Alice' in (x.search_key('alice').key))
        
    def test_predecessor_key(self):
        x = test_BST_instance()
        y = 'beginning'
        self.assertEqual(x.predecessor_key('get'),y)
        
    def test_successor_key(self):
        x = test_BST_instance()
        y = 'literally'
        self.assertEqual(x.successor_key('get'),y)
    
    def test_insert_key(self):
        x = test_BST_instance()
        x.insert_key('team',1)
        self.assertIs(x.search_key('team').key, 'team')
    
    def test_delete_key(self):
        x = test_BST_instance()
        x.delete_key('alice')
        self.assertIs(x.search_key('alice'),None)
    
test = test_BST()
test = test.test_delete_key()