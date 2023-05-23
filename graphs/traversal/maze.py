from collections import deque

class Maze:

    def __init__(self,matrix):
        self.matrix=matrix
        # define the moves L,D,U,R 
        self.moveX=[1,0,0,-1]
        self.moveY=[0,-1,1,0]
        # since it is 4*4 matrix make all 16 vertices at first cannot be visited
        self.visited=[ [False for _ in range (len(self.matrix))] for _ in range(len(self.matrix)) ]
        self.min_distance=float('inf')
    
    def is_valid(self,row,col):
        # make sure it doesn;t excedd the right hand side boundary of the list
        if row<0 and row>=len(self.matrix):
            return False
        # make sure it doesn;t excedd the left hand side boundary of the list
        if col<0 and col>=len(self.matrix):
            return False
        # check if neiggbor is an obstacle or not
        if self.matrix[row][col]==0:
            return False
        # check if neighbor already visited
        if self.visited[row][col]:
            return False
        return True
    
    # i,j are x and y cordinates repectively
    def search(self,i,j,destX,destY):
        self.visited[i][j]=True
        # it is a linked list giving access to first and last nodes
        queue=deque()
        queue.append((i,j,0))

        while queue:
            (i,j,dist)=queue.popleft()
            #check whether maze end reached or not
            if i==destX and j==destY:
                self.min_distance=dist
                break
            # make a move in direction L,U,D,R
            for move in range(len(self.moveX)):
                nextX=i+self.moveX[move]
                nextY=j+self.moveY[move]
                # check if move is valid and can be made
                if self.is_valid(nextX,nextY):
                    # make the move and set visited vertex as true
                    self.visited[nextX][nextY]=True
                    queue.append((nextX,nextY,dist+1))
    
    def maze_result(self):
        if self.min_distance!=float('inf'):
            print("The shortest path to solve maze takes {self.min_distance} steps")
        else:
            print("There is no possible solution, try changing the matrix values")

if __name__=="__main__":

    mtx=[
        [1,1,1,1],
        [0,0,0,1],
        [0,0,0,1],
        [0,0,0,1]
    ]

    maze_path=Maze(mtx)
    maze_path.search(0,0,4,4)
    maze_path.maze_result()