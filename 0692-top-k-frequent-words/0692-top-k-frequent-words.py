class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = defaultdict(int)
        for word in words:
            dic[word] += 1      
        
        heap = []
        for word in dic.keys():
            heappush(heap, (-1 * dic[word], word))
         
        ans = []
        for _ in range(k):
            ans.append(heappop(heap)[1])
        
        return ans
            