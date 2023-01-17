class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        moveUp = False
        moveDown = False
        
        for i in range(len(arr)-1):
            if moveDown == False: 
                if moveUp == False:
                    if arr[i] < arr[i+1]:
                        moveUp = True
                    else:
                        return False
            
                else:
                    if arr[i] > arr[i+1]:
                        moveDown = True
                        
                    elif arr[i] == arr[i+1]:
                        return False
                    
            else:
                if arr[i] <= arr[i+1]:
                    return False
        if moveUp == True and moveDown == True:
            return True
        return False

            