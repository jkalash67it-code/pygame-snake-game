import pygame
from pygame.math import Vector2

cell_size = 15
number_of_cells = 25
OFFSET = 75

class Snake:
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)
        self.add_segment = False
        self.eat_sound = pygame.mixer.Sound("sounds/food_eat.mp3")
        self.wall_hit_sound = pygame.mixer.Sound("sounds/wall_hit.mp3")

    def draw(self, screen, color, cell_size):
        for segment in self.body:
            segment_rect = (OFFSET + segment.x * cell_size,
                            OFFSET + segment.y * cell_size,
                            cell_size, cell_size)
            pygame.draw.rect(screen, color, segment_rect, 0, 7)

    def update(self):
        self.body.insert(0, self.body[0] + self.direction)
        if self.add_segment:
            self.add_segment = False
        else:
            self.body = self.body[:-1]

    def reset(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)
