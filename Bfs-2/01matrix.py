#Time_Complexity: O(mn)
#Space_Complexity: O(n)


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # row and column is inneed incase of  matrix problem
        m=len(mat)
        n=len(mat[0])  
        #direction array for the four direction
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        q=deque()
        
        #iterate through the row and columns
        for i in range(m):
            for j in range(n):
                # if matrix value  is 0
                if mat[i][j]==0: 
                    #then append it to the queue as tuple
                    q.append((i,j)) 
                else:
                    #orelse decrement by one
                    mat[i][j]=-1 
                    
           #a dist variable to be zero         
        dist = 0 
        #until queue is empty
        #size parameter for each stage
        while q:
            size = len(q)
            #decrement the distance travelled at each state
            dist+=1 
            #traverse through the size parameter
            for _ in range(size):
                curr = q.popleft() 
                #pop it and store and traverse through the direction array
                for x,y in dir: 
                    #nearby row
                    nr = x+curr[0]
                    #nearby column
                    nc = y+curr[1]
                    #boundary check
                    if nr>=0 and nr<m and nc>=0 and nc<n and mat[nr][nc]==-1:
                        # assinging dist to matrix value
                        mat[nr][nc] = dist 
                        q.append((nr,nc)) 
                        #returning the matrix value
        return mat 
        
