# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
            self.nodes_array = self.make_array(head)
            self.n = len(self.nodes_array)
        
    def make_array(self, head):
            nodes_array = list()
        
            ptr = head
            while ptr is not None:
                    nodes_array.append(ptr)
                    ptr = ptr.next
           
            return nodes_array
            
        
    def getRandom(self) -> int:
            i = random.randint(0, (self.n)-1)
            return self.nodes_array[i].val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()