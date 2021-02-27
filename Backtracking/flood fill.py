# https://www.youtube.com/watch?v=R1URUB6_y2k


def solveUtil(grid, psf, row, col, visited):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col]==1 or visited[row][col]==True:
        return

    if row == len(grid)-1 and col == len(grid[0])-1:
        print(psf)
        return

    visited[row][col] = True

    solveUtil(grid, psf+str(row-1)+'-'+str(col)+', ', row-1, col, visited)  # top
    solveUtil(grid, psf+str(row)+'-'+str(col-1)+', ', row, col-1, visited)  # left
    solveUtil(grid, psf+str(row+1)+'-'+str(col)+', ', row+1, col, visited)  # bottom
    solveUtil(grid, psf+str(row)+'-'+str(col+1)+', ', row, col+1, visited)  # right
    visited[row][col] = False

def solve(grid):
    visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
    solveUtil(grid, "0-0, ", 0, 0, visited)

if __name__ == "__main__":
    grid = [
            [0,1,0,0,0],
            [0,1,0,1,0],
            [0,0,0,0,0],
            [1,1,0,1,0],
            [1,0,0,0,0]
    ]

    solve(grid)