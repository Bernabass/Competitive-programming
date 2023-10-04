class MyHashMap:

    def __init__(self):
        self.HashMap = [-1] * (10**6 + 1)
        self.seen = set()
        
    def put(self, key: int, value: int) -> None:
        self.HashMap[key] = value
        self.seen.add(key)

    def get(self, key: int) -> int:
        return self.HashMap[key]

    def remove(self, key: int) -> None:
        if key in self.seen:
            self.seen.remove(key)
            self.HashMap[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)