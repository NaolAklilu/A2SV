class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
      
        result = []
        for i in range(numRows):
            row = [1]
            if result:
                last_row = result[-1]
                row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
                row.append(1)
            result.append(row)
        return result