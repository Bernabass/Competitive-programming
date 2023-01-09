class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = []
        self.value = value
        self.parse = k
        self.count = 0
        

    def consec(self, num: int) -> bool:
        self.stream.append(num)
        if num == self.value:
            self.count += 1
        else:
            self.count = 0
        if len(self.stream) >= self.parse:
            if self.count >= self.parse:
                return True
            else:
                return False
        else:
            return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)