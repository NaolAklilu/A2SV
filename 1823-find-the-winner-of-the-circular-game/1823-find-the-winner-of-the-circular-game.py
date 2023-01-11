class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ptr = 0
        friendsList = []
        
        # create list of friends from the given number of friends
        for i in range(n):
            friendsList.append(i+1)
            
        # Remove friends at the ptr index
        while len(friendsList) > 1:
            ptr = (ptr+k - 1) % len(friendsList)
            friendsList.pop(ptr)
        
        return friendsList[0]
        
            