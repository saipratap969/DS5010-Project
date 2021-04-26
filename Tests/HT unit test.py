from HT_module import HashMap

import unittest

def test_cleaning(text):
    
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for ele in text: 
        if ele in punc: 
            text = text.replace(ele, "")
            
    text = text.lower()
    text = text.split(' ')
    return text

def test_HashMap_instance():
    hmap = HashMap()
    
    text = """Alice was beginning to get very tired, literally very very tired"""
    
    text = test_cleaning(text)
    
    for word in text:
        if hmap.search_key(word):
            hmap.increase(word)
        else:
            hmap.insert_key(word,1)
            
    return hmap

class test_HashMap(unittest.TestCase):
    
    def test_insert_key(self):
        x = test_HashMap_instance()
        x.insert_key('team',1)
        self.assertIs(x.search_key('team'),True)
    
    def test_delete_key(self):
        x = test_HashMap_instance()
        x.delete_key('alice')
        self.assertIs(x.search_key('alice'),False)
    
    def test_search_key(self):
        x = test_HashMap_instance()
        
        self.assertEqual(x.search_key('alice'),True)
        self.assertEqual(x.search_key('Alice'),False)
               
    
    def test_increase(self):
        x = test_HashMap_instance()
        x.increase('alice')
        self.assertEqual(x.get('alice'),2)
        
        
    def test_get(self): 
        x = test_HashMap_instance()
        x.insert_key('team',5)
        self.assertEqual(x.get('team'),5)
    
    def test_list_all_keys(self):
        x = test_HashMap_instance()
        y = ['alice', 'was', 'beginning', 'to', 'get', 'very', 'tired', 'literally']
        self.assertEqual(x.list_all_keys(),y)