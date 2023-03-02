class StockSpanner:

    def __init__(self):
        self.prices = []
        self.stack = []
        self.dic = {}

    def next(self, price: int) -> int:
        self.prices.append(price)
        
        count = 1
        while len(self.stack) > 0 and self.prices[self.stack[-1]] <= price:
            count += self.dic[self.stack[-1]]
            self.stack.pop()
        
        self.stack.append(len(self.prices)-1)
        self.dic[len(self.prices)-1] = count
                   
        return count
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)