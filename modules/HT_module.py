class Node:
    
    def __init__(self,key = '', value = -1) -> None:
        
        self.key = key
        self.value = value
        self.next = None
    

class HashMap:
    
    def __init__(self):
        
        self.buckets = 9973
        self.keys = []
        self.array = [Node() for i in range(self.buckets)]
 
    
    
    def hash_key(self,key: str) -> int:
        """calculates the hash key"""        
        
        total = 0
        prime = 3
                          
        for index, char in enumerate(key,start=1):
                
            total += ord(char)*(prime)**index
                
        return total % self.buckets
    
    def insert_key(self, key : str, value : int) -> None:
        """inserts the key to the hash table"""
        
        hash_key = self.hash_key(key)
        head = self.array[hash_key]
        
        while head.next:
            if head.next.key == key:
                head.next.value = value
                return
            head = head.next
        head.next = Node(key,value)
        self.keys.append(key)
        
    def delete_key(self, key: str) -> None:
        """deletes the key from the hash table"""
        
        hash_key = self.hash_key(key)
        head = self.array[hash_key]
        
        while head.next:
            if head.next.key == key:
                curr = head.next
                head.next = curr.next
                curr.next = None
                self.keys.remove(key)
                return
            head = head.next
        
            
    def search_key(self, key:str) -> bool:
        """searches the key in the hash table"""
        
        hash_key = self.hash_key(key)
        head = self.array[hash_key]
        
        while head.next:
            if head.next.key == key:
                return True
            head = head.next
        
        return False
    
    def get(self, key:str) -> int:
        """returns the value of given key""""
        hash_key = self.hash_key(key)
        head = self.array[hash_key]
        
        while head.next:
            if head.next.key == key:
                return head.next.value
            head = head.next
        
        return -1
            
    def increase(self, key:str) -> None:
        """increases the value count"""

        hash_key = self.hash_key(key)
        head = self.array[hash_key]  
        
        while head.next: 
            if head.next.key == key:
                head.next.value +=1
            head = head.next
            
    def list_all_keys(self):
        """returns all the keys and values"""
        
        return self.keys
    
        
                
                
        
    
        

            
    


