class DataStream:

    def __init__(self, value: int, k: int):
        self.dataStream = []
        self.value = value
        self.k = k
        self.valueCount = 0

    def consec(self, num: int) -> bool:
        self.dataStream.append(num)
        if num == self.value:
            self.valueCount += 1
        else:
            self.valueCount = 0
        
        if self.valueCount >= self.k:
            return True
        else:
            return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)