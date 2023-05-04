#User function Template for python3

class Solution:
    
    #Heapify function to maintain heap property.
    def heapify(self,heap, n, current):
        curChild = current
        left = 2*current + 1
        right = 2*current + 2
        
        if left < n and heap[left] > heap[curChild]:
            curChild = left
            
        if right < n and heap[right] > heap[curChild]:
            curChild = right
            
        if curChild != current:
            heap[current], heap[curChild] = heap[curChild], heap[current]
            self.heapify(heap,n, curChild)
        
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range((n//2)-1,-1,-1):
            self.heapify(arr, n, i)
        
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        
        while n != 0:
            arr[0], arr[n-1] = arr[n-1], arr[0]
            n -= 1
            self.heapify(arr, n, 0)
        
         


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends