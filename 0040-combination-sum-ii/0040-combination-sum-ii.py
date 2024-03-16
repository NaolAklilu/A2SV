class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(start, path, remain):
            if remain == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if remain - candidates[i] < 0:
                    break
                backtrack(i + 1, path + [candidates[i]], remain - candidates[i])

        candidates.sort()
        res = []
        backtrack(0, [], target)
        return res