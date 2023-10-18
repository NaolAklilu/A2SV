class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:        
        if len(nums) <= 1:
            return len(nums)
        
        nums_set = set(nums)
        parent = {num:num for num in nums_set}
        rank = {num:1 for num in nums_set}
        
        def find(num):
            if num != parent[num]:
                parent[num] = find(parent[num])
            
            return parent[num]
        
        def combine(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 != p2:
                if rank[p1] >= rank[p2]:
                    parent[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    parent[p1] = p2
                    rank[p2] += rank[p1]
            
        for num in nums_set:
            if num+1 in nums_set:
                combine(num+1, num)
            if num-1 in nums_set:
                combine(num-1, num)
        
        results = defaultdict(list)
        for num in nums_set:
            results[find(num)].append(num)
            
        maxSet = 0
        for st in results.values():
            maxSet = max(maxSet, len(st))
            
        return maxSet 
        
                
            