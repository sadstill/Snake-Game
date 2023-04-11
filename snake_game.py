import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class Cube:
    rows = 0  # Ряды
    w = 0

    def __init__(self, start, dirX=1, dirY=0, color=(255, 0, 0)):
        pass

    def move(self, dirX, dirY):
        pass

    def draw(self, surface, eyes=False):
        pass


class Snake:
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirX = 0
        self.dirY = 1

    def move(self):
        for event in pygame.event.get():  # Все события, произошедшие в течение одного цикла игры / Обработка одного кадра.
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirX = -1
                    self.dirY = 0
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

                if keys[pygame.K_RIGHT]:
                    self.dirX = 1
                    self.dirY = 0
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

                if keys[pygame.K_UP]:
                    self.dirX = 0
                    self.dirY = 1
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

                if keys[pygame.K_DOWN]:
                    self.dirX = 0
                    self.dirY = -1
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

    def reset(self, pos):
        pass

    def cube_add(self):
        pass

    def draw(self, surface):
        pass


def grid_draw(grid_width, grid_rows, grid_surface):  # Отрисовка сетки.
    size_between = grid_width // grid_rows

    x = 0
    y = 0
    for i in range(rows):
        x = x + size_between
        y = y + size_between

        pygame.draw.line(grid_surface, (255, 255, 255), (x, 30), (x, grid_width - 30))
        pygame.draw.line(grid_surface, (255, 255, 255), (30, y), (grid_width - 30, y))


def window_redraw(window_surface):
    global rows, width
    window_surface.fill((0, 0, 0))
    grid_draw(width, rows, window_surface)
    pygame.display.update()


def spawn_random_snack(rows, items):
    pass


def message_box(subject, content):
    pass


def main():
    global width, rows
    width = 600
    rows = 20
    window = pygame.display.set_mode((width, width))
    snake = Snake((255, 0, 0), (10, 10))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)  # Задержка между операциями.
        clock.tick(10)  # Этот метод объекта Clock, позволяет выставить частоту кадров в игре.
        window_redraw(window)


rows = 0
width = 0

main()
