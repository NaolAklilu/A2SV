class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        
        coordinates.sort()
        
        y_diff = coordinates[0][1] - coordinates[1][1]
        x_diff = coordinates[0][0] - coordinates[1][0]
        
        for index in range(1, len(coordinates)):
            cur_y_diff = coordinates[0][1] - coordinates[index][1]
            cur_x_diff = coordinates[0][0] - coordinates[index][0]
            
            if y_diff == 0:
                if cur_y_diff != 0:
                    return False
            
            if x_diff == 0:
                if cur_x_diff != 0:
                    return False
                
            if y_diff and x_diff:
                if cur_y_diff == 0 or cur_x_diff == 0:
                    return False
            
                if (y_diff / x_diff) != (cur_y_diff / cur_x_diff):
                    return False
            
        return True