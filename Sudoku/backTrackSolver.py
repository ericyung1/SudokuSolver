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

def solveSudoku(grid):
    board = isEmpty(grid)
    if not board:
        return True
    else:
        row, col = board

    for i in range(1, 10):
        if isValid(grid, i, (row, col)):
            grid[row][col] = i

            if solveSudoku(grid):
                return True

            grid[row][col] = 0

    return False


def isValid(grid, num, pos):
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if grid[i][j] == num and (i,j) != pos:
                return False

    return True

def isEmpty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)

    return None

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
                solveSudoku(grid)
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