class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        binary_dic = defaultdict(list)
        min_operations = []
        
        
        for i in range(len(boxes)):
            if boxes[i] == '1':
                binary_dic['1'].append(i)
            else:
                binary_dic['0'].append(i)
        
        for i in range(len(boxes)):
            curSum = 0
            for num in binary_dic['1']:
                curSum += abs(num - i)
            min_operations.append(curSum)
        
        return min_operations