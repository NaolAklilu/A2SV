class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        visited = set()
        notUnique = set()
        total = 0
        
        for num in nums:
            if num in visited:
                notUnique.add(num)
            visited.add(num)
            
        for num in visited:
            if num not in notUnique:
                total += num
        
        return total