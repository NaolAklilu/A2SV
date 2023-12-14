class FrequencyTracker:

    def __init__(self):
        self.dictionary = defaultdict(int)
        self.counter = defaultdict(int)

    def add(self, number: int) -> None:
        self.counter[self.dictionary[number]] -= 1
        self.dictionary[number] += 1
        self.counter[self.dictionary[number]] += 1  

    def deleteOne(self, number: int) -> None:
        if self.dictionary[number] > 0:
            self.counter[self.dictionary[number]] -= 1
            self.dictionary[number] -= 1
           
        self.counter[self.dictionary[number]] += 1
            

    def hasFrequency(self, frequency: int) -> bool:
        if self.counter[frequency] > 0:
            return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)