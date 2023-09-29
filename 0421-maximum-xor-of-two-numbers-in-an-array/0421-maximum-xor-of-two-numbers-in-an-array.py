class Solution:
    def __init__(self):
        self.root = {}
    
    def insert(self, num):
        cur = self.root
        curNum = "{:032b}".format(num)
        
        for char in curNum:
            if char not in cur:
                newNode = {}
                cur[char] = newNode
            
            cur = cur[char]
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        for num in nums:
            self.insert(num)

        maxNum = 0
        for num in nums:
            cur = self.root
            curNum = "{:032b}".format(num)
            
            curBit = []
            for bit in curNum:
                if bit == "0":
                    if "1" in cur:
                        cur = cur["1"]
                        curBit.append("1")
                    else:
                        cur = cur[bit]
                        curBit.append(bit)
                else:
                    if "0" in cur:
                        cur = cur["0"]
                        curBit.append("0")
                    else:
                        cur = cur[bit]
                        curBit.append(bit)
            
            pairNum = 0
            for i in range(32):
                if curBit[i] == '1':
                    pairNum += 2**(32-i-1)
            
            maxNum = max(maxNum, num^pairNum)
        
        return maxNum
    
    
        
