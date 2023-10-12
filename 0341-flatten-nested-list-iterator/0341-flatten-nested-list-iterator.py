# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattend = []
        self.idx = 0
        
        def go(arr):
            for element in arr:
                if element.isInteger():
                    self.flattend.append(element.getInteger())
                    
                else:
                    go(element.getList())
                    
        go(nestedList)
        self.length = len(self.flattend)

    
    def next(self) -> int:
        return self.flattend[self.idx - 1]

        
    def hasNext(self) -> bool:
        self.idx += 1
        return self.idx <= self.length


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())