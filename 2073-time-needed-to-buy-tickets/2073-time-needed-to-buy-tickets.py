class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        seconds = 0
        while tickets[k] != 0:
            for i in range(len(tickets)):
                if tickets[i] == 0:
                    continue
                else:
                    seconds += 1
                    tickets[i] -= 1
                    if i == k:
                        if tickets[i] == 0:
                            break
                            
        return seconds
                    
            