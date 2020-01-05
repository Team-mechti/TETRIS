from pg_board import Board
import pygame
import random

cell_size = 30
size = widht, height = 500, 1200 # размеры окошка
b_width = 300  # размеры клеточного поля
b_height = 600
top = 15
left = 45

# короче мы создаём поле в виде списка его строк, забитых нулями. Ноль - пустая клетка, единица - закрашенная клетка. Ниже
# описаны разные варианты фигур, которые получаются при повороте (если непонятно, попробуй нарисовать на бумажке).
# Поворот происходит всегда против часовой стрелки

TURN = 0  # количество поворотов
S = [[[0, 1, 1],
     [1, 1, 0]],

    [[1, 0],
     [1, 1],
     [0, 1]]]

Z = [[[1, 1, 0],
      [0, 1, 1]],

      [[0, 1],
      [1, 1],
      [1, 0]]]

I = [[[1, 1, 1, 1]],
     [[1],
     [1],
     [1],
     [1]]]

O = [[1, 1],
      [1, 1]]

J = [[[0, 1],
      [0, 1],
      [1, 1]],

    [[1, 1, 1],
     [0, 0, 1]],

   [[1, 1],
    [1, 0],
    [1, 0]]]

L = [[[1, 0],
      [1, 0],
      [1, 1]],

     [[0, 0, 1],
      [1, 1, 1]],

     [[1, 1],
      [0, 1],
      [0, 1]]]

T = [[[1, 1, 1],
      [0, 1, 0]],

     [[1, 0],
      [1, 1],
      [1, 0]],

     [[0, 1, 0],
      [1, 1, 1]],

     [[0, 1],
      [1, 1],
      [0, 1]]]


class Figures(Board):
    def __init__(self, width, height):
        self.figures = ['S', 'Z', 'I', 'O', 'J', 'L', 'T']  # для удобства фигурки буквами назовём
        super().__init__(width, height)
        self.colors = ['blue', 'red', 'green', 'yellow']  # цвета фигурок
        self.left = 45  # у верхнего левого угла поля
        self.top = 15  # х верхнего левого угла поля
        self.cell_size = 30

    def get_figure(self):  # здесь мы выбираем рандомную фигурку и цвет, в который она будет покрашена
        return random.choice(self.figures), random.choice(self.colors)

    def draw_figure(self, shape, x, y, f_color): #отрисовка фигуры сверху
        h = 0 # высота, на которую опускается фигурка
        for i in shape[0]:
            for n in i:
                if n == 1:
                    rect = (x, y + cell_size * h, 30, 30)
                    pygame.draw.rect(screen, pygame.Color(f_color), rect)
                    h += 1

    def grid(self, locked={}): # функция создаёт поле
        grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(10) for _ in range(20)]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (j, i) in locked:
                    l = locked[(j, i)]
                    grid[i][j] = l

        print(grid)
        return grid

    def turn(self, TURN):  # поворот фигуры
        pass

    def move(self):  # обычное передвижение фигуры
        pass

    def fast_move(self):  # быстрое передвижение
        pass

    def move_right(self):  # сдвиг вправо
        pass

    def move_left(self):  # сдвиг влево
        pass


pygame.init()
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
board = Board(10, 25)
board.set_view(15, 45)
back_color = pygame.Color('black')
running = True

while running:
    figures = Figures(500, 1200)
    shape = figures.get_figure()[0]
    f_color = figures.get_figure()[1]
    figures.draw_figure(shape, 5 * cell_size + top, 1 * cell_size + left, f_color)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_UP:
                TURN += 1
                figures.turn(TURN)
            elif event.type == pygame.K_DOWN:
                figures.fast_move()
            elif event.type == pygame.K_RIGHT:
                figures.move_right()
            elif event.type == pygame.K_LEFT:
                figures.move_left()
    screen.fill(back_color)
    board.render(screen)

pygame.quit()


