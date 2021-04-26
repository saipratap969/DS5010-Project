from RBT_module import RBT

import unittest

def test_cleaning(text):
    
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for ele in text: 
        if ele in punc: 
            text = text.replace(ele, "")
            
    text = text.lower()
    text = text.split(' ')
    return text

def test_RBT_instance():
    rbt = RBT()
    
    text = """Alice was beginning to get very tired, literally very very tired"""
    
    text = test_cleaning(text)
    
    for word in text:
        rbt.insert_key(word)
    
    return rbt
        
class test_RBT(unittest.TestCase):
    
    def test_sort(self):
        x = test_RBT_instance()
        y = ['alice:1', 'beginning:1', 'get:1', 'literally:1', 'tired:2', 'to:1', 'very:3', 'was:1']
        
        self.assertEqual(x.sort(),y)
    
    def test_min(self):
        x = test_RBT_instance()
        y = 'alice'
        self.assertEqual(x.min(x.root).key,y)
    
    def test_max(self):
        x = test_RBT_instance()
        y = 'was'
        self.assertEqual(x.max(x.root).key,y)        
    
    def test_search_key(self):
        x = test_RBT_instance()
        
        self.assertTrue('alice' in (x.search_key('alice').key))
        self.assertFalse('Alice' in (x.search_key('alice').key))
        
    
    def test_predecessor_key(self):
        x = test_RBT_instance()
        y = 'beginning'
        self.assertEqual((x.predecessor_key(x.search_key('get'))).key,y)
        
    
    def test_successor_key(self):
        x = test_RBT_instance()
        y = 'literally'
        self.assertEqual((x.successor_key(x.search_key('get'))).key,y)
    
    def test_insert_key(self):
        x = test_RBT_instance()
        x.insert_key('team')
        self.assertIs(x.search_key('team').key, 'team')
    
    def test_delete_key(self):
        x = test_RBT_instance()
        x.delete_key(x.root,'alice')
        self.assertIs(x.search_key('alice').key,0)
    
