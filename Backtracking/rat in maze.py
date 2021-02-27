# https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/

# def display(maze):
#     for row in maze:
#         print(row)
#     print("\n")

def findPathUtil(maze, psf, row, col, visited):    # onlu can move in 2 directions: right and down
    if row >= len(maze) or col >= len(maze[0]) or maze[row][col] == 0 or visited == True:
        return
    if row == len(maze)-1 and col == len(maze[0])-1:
        print(psf)
        return

    visited[row][col] = True
    findPathUtil(maze, psf+str(row+1)+'-'+str(col)+', ', row+1, col, visited)  # down
    findPathUtil(maze, psf+str(row)+'-'+str(col+1)+', ', row, col+1, visited)  # right
    visited[row][col] = False

def findPath(maze):
    visited = [[False for j in range(len(maze[0]))] for i in range(len(maze))] 
    # print(visited)
    findPathUtil(maze, '0-0, ', 0, 0, visited)

if __name__ == "__main__":
    maze = [ [1, 0, 0, 0],
             [1, 1, 1, 1],
             [0, 1, 0, 1],
             [1, 1, 1, 1] ]
    findPath(maze)
