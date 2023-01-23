class Solution: 
    def select(arr, i):
        return i

    def selectionSort(self, arr: list,n: int):
        for i in range(len(arr)):
            current_index = i
            for j in range(i, len(arr)):
                if arr[current_index] > arr[j]:
                    current_index = j
            arr[i], arr[current_index] = arr[current_index], arr[i]
    
        return arr
