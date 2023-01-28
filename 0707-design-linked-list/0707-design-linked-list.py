class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0
        
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        
        position = self.head
        for _ in range(index):
            position = position.next
            
        return position.val

    def addAtHead(self, val: int) -> None:
        inserted = Node(val)
        inserted.next = self.head
        self.head = inserted
        self.length += 1
        

        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return - 1
        if not index or not self.head:
            self.addAtHead(val)
            
        else:
            position = self.head
            inserted = Node(val)
            print(index)
            for _ in range(index-1):
                position = position.next
            
            inserted.next = position.next
            position.next = inserted
            
            self.length += 1
    
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)
        
        
    def deleteAtIndex(self, index: int) -> None:
        if not self.head or index >= self.length:
            return -1

        if not index:
            self.head = self.head.next
        else:    
            previous = self.head
            for _ in range(index-1):
                previous = previous.next

            previous.next = previous.next.next
        
        self.length -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)