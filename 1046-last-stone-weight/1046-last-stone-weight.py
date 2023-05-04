class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        def swap(heap,i, j):
            heap[i], heap[j] = heap[j], heap[i]
                
        def heappop(heap):
            if not heap:
                return None
            heap[0] = heap[-1]
            heap.pop()
            current = 0
            heapify_down(heap,current)
        
        def heapify_down(heap, current):
            n = len(heap)
            curChild = current
            left = 2 * current + 1
            right = 2 * current + 2

            if left < n and heap[left] > heap[curChild]:
                curChild = left

            if right < n and heap[right] > heap[curChild]:
                curChild = right

            if curChild != current:
                swap(heap,current, curChild)
                heapify_down(heap,curChild)

        
        def heapify(arr):
            for i in range(len(arr)//2, -1, -1):
                heapify_down(arr, i)
                
            return arr
        
        scores = heapify(stones)
        while len(scores) >= 2:
            x = scores[0]
            heappop(scores)
            y = scores[0]
            heappop(scores)
            
            diff = abs(x-y)
            
            if diff != 0:
                scores.append(diff)
                heapify_down(scores,0)
                
        if len(scores) != 0:
            return scores[0]
        return 0
            
                
            