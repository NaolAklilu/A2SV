class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        maxMeal = 0
        pairCount = 0
        twoPowers = []
        
        # store power of two numbers between zero and 2^20 including the 2^20.
        for i in range(0, 22):
            twoPowers.append(2 ** i)
            
        mealCountPair = {}
        # Count each meal in deliciousness and store in dictionary
        for meal in deliciousness:
            if meal > maxMeal:
                maxMeal = meal
            if meal in mealCountPair.keys():
                mealCountPair[meal] += 1
            else:
                mealCountPair[meal] = 1
                
        # find the good meals pair
        for meal in mealCountPair.keys():
            for power in twoPowers:
                mealDifference = power - meal
                if mealDifference > maxMeal:
                    break
                
                if mealDifference in mealCountPair.keys():
                    if mealDifference == meal:
                        pairCount += (mealCountPair[meal])*(mealCountPair[meal] - 1)
                    else:
                        pairCount += (mealCountPair[meal] * mealCountPair[mealDifference])

        # Remove the duplication and modulo 10^9 + 7
        pairCount = (pairCount//2) % (10**9 + 7)
        return pairCount