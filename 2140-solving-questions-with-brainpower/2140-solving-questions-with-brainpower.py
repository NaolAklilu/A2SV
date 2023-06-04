class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = defaultdict(int)
        memo[n-1] = questions[n-1][0]
        
        for index in range(n-2, -1, -1):
            memo[index] = questions[index][0]
            memo[index] += memo[index + questions[index][1] + 1]
            memo[index] = max(memo[index], memo[index+1])
            
        return memo[0]