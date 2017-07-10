# adding for testing
class Linked_List:
    """provides basis for doubly linked list representation"""
    
    class _Node:
        """nonpublic class used for storing a doubly linked node"""
        __slots__ = '_element', '_prev', '_next'
            
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
            

            
    def __init__(self):
        """create an empty list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
        
    def __len__(self):
        """return number of elements in list"""
        return self._size
         
    def __iter__(self):
        """Iterates through the list when encountering a for loop"""
        
        self._position = self._header._next
        return self
    
    def __next__(self):
        """Goes on to the next element in the linked list until reaching the
        last one"""
        if self._position._next == None:
            raise StopIteration  
        
        to_return = self._position._element
        self._position = self._position._next
       
        return to_return
        
        
    def append_element(self, val):
        """add element to end of list"""
        
        newest = self._Node(val, None, None)
        newest._prev = self._trailer._prev
        newest._next = self._trailer
        self._trailer._prev._next = newest
        self._trailer._prev = newest
        self._size += 1
        
        
            
        
    def insert_element_at(self, val, index):
        new = self._Node(val, None, None)
        
        
        if index < 0 or index >= self._size:
            raise IndexError
        elif index == 0:
            new._next = self._header._next
            new._prev = self._header
            self._header._next = new
            self._header._next._next._prev = new
            self._size += 1
            current = self._header._next
            
        else:
            count = 0
            current = self._header._next
            while count < index - 1:
                current = current._next
                count += 1
            new._next = current._next
            new._prev = current
            current._next = new
            current._next._next._prev = new
            self._size += 1
            
            
                
        
        
    def remove_element_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError
        elif index == 0:
            to_return = self._header._next._element
            self._header._next = self._header._next._next
            self._header._next._prev = self._header
            self._size -= 1
            return to_return
            
        else:
            current = self._header._next
            count = 0
            while count < index - 1:
                scurrent = current._next
                count += 1
            to_return = current._next._element
            current._next = current._next._next
            current._next._prev = current
            self._size -= 1
            return to_return
     
        
    def get_element_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError
        else:
            current = self._header._next
            count = 0
            while count < index:
                current = current._next
                count += 1
            return current._element
        
        
    def __str__(self):
        if self._size == 0:
            return '[ ]'
       
        else:
            result = '[ '
            current = self._header._next
            result += str(current._element)
            current = current._next
            for i in range(1, self._size):
                result += ', ' + str(current._element)
                current = current._next
            result += ' ]'
            return result
            
            
            
if __name__ == '__main__':
    
    a = Linked_List()
    print(a)
    print("linked list has " + str(len(a)) + " elements")
    try:
        a.append_element(7)
        a.append_element(10)
        a.append_element(13)
        a.append_element(5)
        a.append_element(21)
    except MemoryError:
        print("Error: unexpected out of cells")
    print(a)
    print("linked list has " + str(len(a)) + " elements")
    
    # Test out the iterator and next methods
    for val in a:
        print(val)
        
    # Test out the get element at method
    # this should work
    try:
        print()
        a.get_element_at(2)
        a.get_element_at(4)
    except IndexError:
        print("Please enter a valid index")
    # this should fail
    try:
        print(a.get_element_at(7))
    except IndexError:
        print("Please enter a valid index")
        
    # try to remove an element at a given index
    # this should work
    try:
        print()
        print(a)
        print(a.remove_element_at(2))
        print(a.remove_element_at(0))
        print(a)
        print("linked list has " + str(len(a)) + " elements")
    except IndexError:
        print("Please enter a valid index")
    #this should fail
    try:
        print(a.remove_element_at(8))
    except IndexError:
        print("Please enter a valid index")
        
    
    # test the insert element at method
    # this should work
    try:
        a.insert_element_at(13, 0)
        a.insert_element_at(23, 3)
        print()
        print(a)
        print("linked list has " + str(len(a)) + " elements")        
    except IndexError:
        print("Please enter a valid index")
    # this should fail
    try:
        a.insert_element_at(15, 7)
    except IndexError:
        print("Please enter a valid index")
        
    # try inserting an empty list
    # this should work
    b = Linked_List()
    try:
        b.insert_element_at(5, 0)
        print()
        print(b)
        print("linked list has " + str(len(b)) + " elements")
    except IndexError:
        print("Please enter a valid index")   
        
    c = Linked_List()
    print()
    try:
        c.remove_element_at(0)
        print(c)
        print("linked list has " + str(len(c)) + " elements")        
    except IndexError:
        print("You can't remove from an empty list")
        
    d = Linked_List()
    print()
    try:
        d.insert_element_at(5, 0)
        print(d)
        print("linked list has " + str(len(d)) + " elements")
    except IndexError:
        print("You can't insert in an empty list")
        
    d.append_element("Hello")
    d.append_element(1)
    d.append_element("Goodbye")
    print()
    print(d)
    try:
        d.get_element_at(1)
    except IndexError:
        print("Please enter a valid index")
        
    d.remove_element_at(1)
    print()
    print(d)
    try:
        d.get_element_at(1)
    except IndexError:
        print("Please enter a valid index")
        
    e = Linked_List()
    e.append_element("Hello")
    print()
    print(e)
    try:
        e.get_element_at(0)
    except IndexError:
        print("Please eneter a valid index")
        
    
        
    
