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
            
