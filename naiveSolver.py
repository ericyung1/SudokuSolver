import pygame

width = 550
background_color = (255, 255, 255)
element_color = (0, 255, 255)

grid = [[4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 8, 5],
        [0, 0, 7, 0, 4, 8, 0, 5, 0],
        [0, 0, 1, 3, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 7, 0, 0, 0, 0],
        [8, 6, 0, 0, 0, 0, 9, 0, 3],
        [7, 0, 0, 0, 0, 5, 0, 6, 2],
        [0, 0, 3, 7, 0, 0, 0, 0, 0]]

def isSafe(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def solveSudoku(grid, row, col):
    if (row == 8 and col == 9):
        return True
    
    if col == 9:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)

    for num in range(9):
        if isSafe(grid, row, col, num):
            grid[row][col] = num
            pygame.display.update()
            if solveSudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

def main():
    pygame.init()
    screen = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Sudoku Solver")
    screen.fill(background_color)
    myfont = pygame.font.SysFont('calibri', 35)

    for i in range(0, 10):
        if (i % 3 == 0):
            pygame.draw.line(screen, (0,0,0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(screen, (0,0,0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
        pygame.draw.line(screen, (0,0,0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(screen, (0,0,0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()

    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if (0 < grid[i][j] < 10):
                value = myfont.render(str(grid[i][j]), True, element_color)
                screen.blit(value, ((j + 1) * 50 + 18, (i + 1) * 50 + 9))
    pygame.display.update()


    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                solveSudoku(grid, 0, 0)
                for i in range(0, len(grid[0])):
                    for j in range(0, len(grid[0])):
                        if (0 < grid[i][j] < 10):
                            value = myfont.render(str(grid[i][j]), True, element_color)
                            screen.blit(value, ((j + 1) * 50 + 18, (i + 1) * 50 + 9))
                pygame.display.update()
        if event.type == pygame.QUIT:
                pygame.quit()
                return

main()