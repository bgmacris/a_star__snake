import pygame
import random
import copy
from map import draw_map
from route import algoritmo, ruta


def operador(pos1, pos2, posX, posY, operador):
    try:
        x1_change, y1_change = 0, 0
        if pos1 > posX:
            x1_change = operador
            y1_change = 0
        if pos2 > posY:
            y1_change = operador
            x1_change = 0
        if pos1 < posX:
            x1_change = -operador
            y1_change = 0
        if pos2 < posY:
            y1_change = -operador
            x1_change = 0

        return x1_change, y1_change
    except:
        print((pos1, pos2))
        print(posX, posY)


def calcular_snake_list(resultado, posX, posY, snake_list, parts_snake):
    # parts_snake += 1
    copy_snake = copy.copy(snake_list)
    for i in resultado:
        x1_change, y1_change = operador(i[0], i[1], posX, posY, 10)
        posX += x1_change
        posY += y1_change
        snake_head = (posX, posY)
        copy_snake.append(snake_head)
        if len(copy_snake) > parts_snake:
            del copy_snake[0]
    cabeza = copy_snake[0]
    x = 0
    for i in copy_snake:
        if i == cabeza:
            x += 1

    return copy_snake[::-1]


class snake_game():
    def __init__(self):
        pygame.init()

        self.white = (255, 255, 255)
        self.green = (122, 255, 51)
        self.blue = (3, 126, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)

        self.display_x = 200
        self.display_y = 200
        self.dis = pygame.display.set_mode((self.display_x, self.display_y))
        pygame.display.set_caption('Snake')

        self.game_over = False

        self.posX = 190
        self.posY = 190

        self.x1_change = 0
        self.y1_change = 0
        self.direccion_actual = 'right'

        self.snake_list = []
        self.parts_snake = 1

        self.clock = pygame.time.Clock()

        # foodx = round(random.randrange(10, display_x - 10) / 10.0) * 10.0
        # foody = round(random.randrange(10, display_y - 10) / 10.0) * 10.0
        self.foodx = 160
        self.foody = 10

        self.original_map = draw_map()
        self.game()


    def our_snake(self, snake_list):
        for x in snake_list:
            if snake_list.index(x) == 0:
                pygame.draw.rect(self.dis, self.blue, [x[0], x[1], 10, 10])
            else:
                pygame.draw.rect(self.dis, self.white, [x[0], x[1], 10, 10], 1)
      

    def game(self):
        while not self.game_over:
            resultado = algoritmo(self.original_map, self.snake_list,
                                  (self.posX, self.posY), (self.foodx, self.foody))
            if not resultado:
                print("Buscar cola")
                resultado = algoritmo(self.original_map, self.snake_list,
                                      (self.posX, self.posY), self.snake_list[0], pop=-1, ignore=self.snake_list[0])
            
            next_snake_pos = calcular_snake_list(resultado, self.posX, self.posY, self.snake_list, self.parts_snake)
            if self.parts_snake > 2:
                next_head = (next_snake_pos[0][0], next_snake_pos[0][1])
                next_tail = (next_snake_pos[-1][0], next_snake_pos[-1][1])
                comprov_go_tail = algoritmo(self.original_map, next_snake_pos, next_head, next_tail, ignore=next_tail)
                if not comprov_go_tail or next_tail in self.original_map[next_head]:
                    print("No tiene proximo movimiento")
                    resultado = algoritmo(self.original_map, self.snake_list,
                                          (self.posX, self.posY), self.snake_list[0], pop=-1, ignore=self.snake_list[0])
                    print(resultado)
            
                
            x1_change, y1_change = operador(
                resultado[0][0], resultado[0][1], self.posX, self.posY, 10)

            if self.posX >= self.display_x or self.posX < 0 or self.posY < 0 or self.posY >= self.display_y:
                self.game_over = True
            # x1_change, y1_change = 0, 0
            self.posX += x1_change
            self.posY += y1_change
            self.dis.fill(self.black)
            pygame.draw.rect(self.dis, self.red, [
                             self.foodx, self.foody, 10, 10])
            snake_head = (self.posX, self.posY)
            self.snake_list.append(snake_head)
            if len(self.snake_list) > self.parts_snake:
                del self.snake_list[0]

            for x in self.snake_list[:-1]:
                if x == snake_head:
                    self.game_over = True

            self.our_snake(self.snake_list)
            pygame.draw.rect(self.dis, self.green, [
                             self.posX, self.posY, 10, 10])

            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True

            if self.posX == self.foodx and self.posY == self.foody:
                while (self.foodx, self.foody) in self.snake_list:
                    self.foodx = int(round(random.randrange(
                        10, self.display_x - 10) / 10.0) * 10.0)
                    self.foody = int(round(random.randrange(
                        10, self.display_y - 10) / 10.0) * 10.0)
                self.parts_snake += 1
            self.clock.tick(70)
        

snake = snake_game()
