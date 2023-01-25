class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        left, right = 0, len(skill)-1
        
        pairSum = skill[-1] + skill[0]
        
        sumTeam = 0
        while left < right:
            if skill[left]+skill[right] != pairSum:
                return -1
            
            sumTeam += (skill[left]*skill[right])
            left += 1
            right -= 1
            
        return sumTeam