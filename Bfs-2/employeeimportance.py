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
        totalimportance=0
        #creating a djency matrix
        adj={}
        #creating a queue
        q=deque()
        #adding the id tothe root
        q.append(id)
        
        #iterate through the employess
        for emp in employees:
            #empid is the key of the adj matrix
            adj[emp.id] = [emp.importance,emp.subordinates]
        
        #until the queue is end
        while q:
            node=q.popleft()
            #adding total imporatnce to the key
            totalimportance+=adj[node][0]
            #iterate through the value of the adj matrix
            for i in adj[node][1]:
                q.append(i)
                
        #return teh total importance
        
        return totalimportance