class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        longestmountain, index = 0, 1
                
        while index <= len(arr) - 1:
            move_up, move_down = 0, 0
            while (index <= len(arr) - 1 and arr[index] == arr[index - 1]):
                index += 1
            
            while (index <= len(arr) - 1 and arr[index] > arr[index - 1]):
                index += 1
                move_up += 1
                
            while (index <= len(arr) - 1 and arr[index] < arr[index - 1]):
                index += 1
                move_down += 1
                
            if move_up and move_down:
                if (move_up + move_down + 1) > longestmountain:
                    longestmountain = move_up + move_down + 1

        return longestmountain