class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        diff_pro_pair = []
        for i in range(len(difficulty)):
            diff_pro_pair.append([difficulty[i], profit[i]])
        
        diff_pro_pair.sort()
        worker.sort()
        
        dif_ptr = 0
        total = 0
        max_profit = 0
        for ptr in range(len(worker)):
            while diff_pro_pair[dif_ptr][0] <= worker[ptr]:
                if dif_ptr+1 != len(difficulty):
                    if max_profit < diff_pro_pair[dif_ptr][1]:
                        max_profit = diff_pro_pair[dif_ptr][1]
                    dif_ptr += 1
                    
                else:
                    break
            
            if dif_ptr > 0:
                if diff_pro_pair[dif_ptr][0] > worker[ptr]:
                    total += max_profit
                else:
                    if max_profit < diff_pro_pair[dif_ptr][1]:
                        max_profit = diff_pro_pair[dif_ptr][1]
                    total += max_profit
                    
            else:
                if diff_pro_pair[dif_ptr][0] <= worker[ptr]:
                    total += diff_pro_pair[dif_ptr][1]
            
        return total
                    
                    
        