#Time_Complexity: O(mn)
#Space_Complexity: O(n)


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
         #Initialize q using deque  
        q = deque() 
        #Initialize freshCount as zero
        freshCount = 0
        #Initialize time as zero
        time = 0 
        #direction array to move four directionally
        dirs_ = [[0,1],[0,-1],[1,0],[-1,0]] 
        #the row of the grid
        m = len(grid)   
        #the column of the grid
        n = len(grid[0]) 
        
        #iterate through the row and column
        for i in range(m):  
            for j in range(n):
                #if the grid value is 2 then append it to queue
                if grid[i][j] == 2: 
                    q.append((i,j))
                    #if the grid value is 1 add freshcount value
                elif grid[i][j] == 1: 
                    freshCount += 1
                    
        #until the queue is empty
        while q and freshCount != 0:
            #increment  time by one
            time+=1 
            #size parameter for traversing each level by level
            size = len(q)   
            for _ in range(size):
                 #Pop the element in the q and store it in curr
                curr = q.popleft() 

                
                 # r,c in the direction array traverse the neighboring elements
                for r,c in dirs_:
                    nr = r+curr[0]
                    nc = c+curr[1]
                     #Boundary check
                    if nr >= 0 and nr < m and nc >= 0 and nc < n:   
                        #if the grid value is one change it to rotten (two)
                        if grid[nr][nc] == 1:   
                            grid[nr][nc] = 2
                            #decrease the freshcount value byb one 
                            freshCount -= 1
                            #append it at each stages of queue
                            q.append((nr,nc))  
            
        #if the freshcount is zero return time     
        if freshCount == 0:
            return time
        else:   
            #Else return -1
            return -1

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            