class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = defaultdict(int)
        left = 0
        
        if len(fruits) <= 2:
            return len(fruits)
        
        maxFruits = 0
        fruitsSum = 0
        for right in range(len(fruits)):
            dic[fruits[right]] += 1
            fruitsSum += 1
            
            while len(dic) > 2:
                dic[fruits[left]] -= 1
                fruitsSum -= 1
                if dic[fruits[left]] == 0:
                    del dic[fruits[left]]
                    
                left += 1
                
            maxFruits = max(maxFruits, fruitsSum)
            
        return maxFruits