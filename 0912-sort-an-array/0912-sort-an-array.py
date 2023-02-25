class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:        
        negatives = []
        positives = []
        for num in nums:
            if num < 0:
                negatives.append(abs(num))
            else:
                positives.append(num)
        
        if len(positives) > 0:
            digits = len(str(max(positives)))
            for digit in range(digits):
                freq = [0]*10
                # find the frequency of each digit
                for num in positives:
                    mod = num // (10**digit)
                    mod %= 10
                    freq[mod] += 1

                # frequency list prefix sum
                for i in range(1,10):
                    freq[i] += freq[i-1]

                tempNums = [0]*len(positives)
                for i in range(len(positives)-1, -1, -1):
                    num = positives[i]
                    div = num // (10**digit)
                    div %= 10
                    freq[div] -= 1
                    tempNums[freq[div]] = num

                positives = [val for val in tempNums]
            
            if len(negatives) > 0:
                digits = len(str(max(negatives)))
                for digit in range(digits):
                    freq = [0]*10
                    # find the frequency of each digit
                    for num in negatives:
                        mod = num // (10**digit)
                        mod %= 10
                        freq[mod] += 1

                    # frequency list prefix sum
                    for i in range(1,10):
                        freq[i] += freq[i-1]

                    tempNums = [0]*len(negatives)
                    for i in range(len(negatives)-1, -1, -1):
                        num = negatives[i]
                        div = num // (10**digit)
                        div %= 10
                        freq[div] -= 1
                        tempNums[freq[div]] = num

                    negatives = [val for val in tempNums]
                
                negatives.reverse()
                nums = [(-val) for val in negatives]
            
            if len(negatives) > 0:
                nums.extend(positives)
            else:
                nums = [val for val in positives]
            
        return nums
                
                
            