class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        position_speed_pair = []
        for i in range(len(position)):
            position_speed_pair.append([position[i], speed[i]])
            
        position_speed_pair.sort(reverse=True)
        remaining_time = []
        stack = []
        for pos_speed in position_speed_pair:
            remaining_time.append((target - pos_speed[0])/pos_speed[1])
    
        for i in range(len(position)):
            if not stack:
                stack.append(remaining_time[i])
            
            elif stack and stack[-1] < remaining_time[i]:
                stack.append(remaining_time[i])
                
        return len(stack)
    
        
        