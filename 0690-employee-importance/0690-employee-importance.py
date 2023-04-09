"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        dic = {}
        for employee in employees:
            dic[employee.id] = [employee.importance, employee.subordinates]
            
        self.totalImportance = 0
        def dfs(employeeId):
            self.totalImportance += dic[employeeId][0]
            
            for employee in dic[employeeId][1]:
                dfs(employee)
                
            return
        
        dfs(id)
        
        return self.totalImportance
        
            