class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(start, path, remain):
            if remain == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                if remain - candidates[i] >= 0:
                    dfs(i, path + [candidates[i]], remain - candidates[i])

        result = []
        dfs(0, [], target)
        return result