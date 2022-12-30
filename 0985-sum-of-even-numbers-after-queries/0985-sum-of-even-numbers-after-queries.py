class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        answer = []
        
        # Calculate the initial even numbers sum
        for num in nums:
            if num % 2 == 0:
                even_sum += num
         
        # find even sum for every query
        for query in queries:
            val = query[0]
            index = query[1]
            
            if nums[index] % 2 == 0:
                if (nums[index] + val) % 2 == 0:
                    even_sum += val
                    
                else:
                    even_sum -= nums[index]
                    
            else:
                if (nums[index] + val) % 2 == 0:
                    even_sum += (nums[index] + val)
                    
            nums[index] = nums[index] + val
            answer.append(even_sum)
            
        return answer 
                
                