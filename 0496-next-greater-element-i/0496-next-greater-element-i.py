class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        for num in nums2:
            dic[num] = -1
            
        for num in nums2:
            while stack and stack[-1] < num:
                dic[stack[-1]] = num
                stack.pop()
                
            stack.append(num)
            
            
        ans = []
        for num in nums1:
            ans.append(dic[num])
            
        return ans