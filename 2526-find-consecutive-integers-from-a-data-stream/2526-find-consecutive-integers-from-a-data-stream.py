class DataStream:

    def __init__(self, value: int, k: int):
        self.dataStream = deque()
        self.value = value
        self.k = k
        self.count = 0

    def consec(self, num: int) -> bool:
        self.dataStream.append(num)
        if num == self.value:
            self.count += 1
            
        if len(self.dataStream) < self.k:
            return False
        elif len(self.dataStream) == self.k:
            if self.count == self.k:
                if self.dataStream[0] == self.value:
                    self.count -= 1
                self.dataStream.popleft()
                return True
            
            if self.dataStream[0] == self.value:
                self.count -= 1
            self.dataStream.popleft()
            return False
        
        
        



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)