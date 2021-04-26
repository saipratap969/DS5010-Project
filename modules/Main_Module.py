import BST_module as BSTree
import HT_module as HTable
import RBT_module as RBTree


def cleaning(text):
    """
    function to clean the text
    param text: The text file or the manual input from the user 
    returns: returns the strings removing non alphanumeric characters
    """
    
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for ele in text: 
        if ele in punc: 
            text = text.replace(ele, "")
            
    text = text.lower()
    text = text.split(' ')
    return text



    
def word_count(ds_type):
    """
    count the frequency of strings 
    param ds_type: The input to select respective algorithm 
    returns: returns the count of strings
    """
    
    type_of_input=input("\nEnter 1 for text input or Enter 0 for file input ")

    if type_of_input=='1':
        text=input("\nPlease enter text here ")
        text=cleaning(text)
    else:
        filename=input("\nEnter file name with '.txt' extension. Note: File should be in the same directory as Python")
        file=open(filename)
        text=file.read()
        file.close()
        text=cleaning(text)
    
    if ds_type.lower()=='h':
        create_htable = HTable.HashMap()
        for word in text:
            if create_htable.search_key(word):
                create_htable.increase(word)
            else:
                create_htable.insert_key(word,1)
       
        print("\nThe created Hash Table is with the following key value pairs : ")
        list_of_keys=create_htable.list_all_keys()
        for key in list_of_keys:
            temp = key + ":" + str(create_htable.get(key))
            print(temp)

        print("\nTo delete any key please enter 1 else enter 0")
        
        del_input=input()
        
        if del_input == '1':
            string_deleted_items=input("/nEnter the valid keys separated by space")
            list_deleted_items=string_deleted_items.split(' ')
            for del_item in list_deleted_items:
                create_htable.delete_key(del_item)
        
        list_keys=create_htable.list_all_keys()
        for key in list_keys:
            temp = key + ":" + str(create_htable.get(key))
            print(temp)
    
    elif ds_type.lower()=='b':
        create_bst=BSTree.BST()
        for word in text:
            if create_bst.search_key(word):
                create_bst.increase_value(word)
            else:
                create_bst.insert_key(word,1)
        
        print("\nThe created Binary Search tree is with the following key value pairs : ")
        create_bst.print_tree_inorder()
        
        print("\n")
        ip1=input('Enter 1 for proceeding to get the maximum and and minimum keys else enter 0')
        if ip1=='0':
            pass
        else:
            print("\nThe word with maximum key is : "+create_bst.getmax().key)
            print("\nThe word with minimum key is : "+create_bst.getmin().key)
        
        
        
        ip2=input('\nTo delete any key please enter 1 else enter 0')
        
        if ip2=='1':
            string_deleted_items=input("Enter the valid keys separated by space")
            list_deleted_items=string_deleted_items.split(' ')
            for del_item in list_deleted_items:
                create_bst.delete_key(del_item)
                
        create_bst.print_tree_inorder()
        
        
        ip3=input('\nTo find the successor of any key please enter 1 else enter 0')
        
        if ip3=='1':
            string_keys=input("Enter the valid keys separated by space")
            list_keys=string_keys.split(' ')
            for key_item in list_keys:
                print("\nThe succesor of key '"+key_item+"' is "+create_bst.successor_key(key_item))
        
        print("\nTo find the predecessor of any key please enter 1 else enter 0")
        
        ip4=input()
        
        if ip4=='1':
            string_of_keys=input("Enter the valid keys separated by space")
            list_of_keys=string_of_keys.split(' ')
            for key_item in list_of_keys:
                print("\nThe predecessor of key '"+key_item+"' is "+create_bst.predecessor_key(key_item))
        

    elif ds_type.lower()=='r':
        create_rbt=RBTree.RBT()
        
        for word in text:
            create_rbt.insert_key(word)
        
        print("\nThe created RedBlack tree is with the following key value pairs : ")
        create_rbt.sort()
        
        
        print("\nTo delete any key please enter 1 else enter 0")
        
        ip2=input()
        
        if ip2=='1':
            string_deleted_items=input("\nEnter the valid keys separated by space")
            list_deleted_items=string_deleted_items.split(' ')
            for del_item in list_deleted_items:
                create_rbt.delete_key(del_item)
                
        print(create_rbt.in_order())
        print("/nTo find the successor of any key please enter 1 else enter 0")
        
        ip3=input()
        
        if ip3=='1':
            string_keys=input("\nEnter the valid keys separated by space")
            list_keys=string_keys.split(' ')
            for key_item in list_keys:
                print("\nThe succesor of key '"+key_item+"' is "+create_rbt.successor_key(key_item))
        
        print("\nTo find the predecessor of any key please enter 1 else enter 0")
        
        ip4=input()
        
        if ip4=='1':
            string_of_keys=input("\nEnter the valid keys separated by space")
            list_of_keys=string_of_keys.split(' ')
            for key_item in list_of_keys:
                print("\nThe predecessor of key '"+key_item+"' is "+create_rbt.predecessor_key(key_item))
    else:
        print("\nThe choosen data structure is unavailable")