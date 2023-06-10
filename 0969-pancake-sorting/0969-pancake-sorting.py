def find_max(arr, m):
    max_num_index = 0
    for i in range(m):
        if(arr[i] > arr[max_num_index]):
            max_num_index = i

    return max_num_index

class Solution:
    def pancakeSort(self,arr: List[int]) -> List[int]:
        
        def flip(end):
            start = 0
            while(start < end):
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        current_size = len(arr)

        flip_index = []
        while current_size > 1:
            max_index = find_max(arr, current_size)        
            if max_index != current_size - 1:
                flip(max_index)
                flip(current_size - 1)
                flip_index.append(max_index + 1)
                flip_index.append(current_size)
                
            current_size -= 1

        print(arr)
        return flip_index