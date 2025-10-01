
import pygame
import pygame.freetype

from constants import SCORE_FONT_SIZE

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self,x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()


        self.x = x
        self.y = y
        self.str_num_score = "0"
        self.cur_score = 0

    def draw(self, screen):
        score = pygame.freetype.Font(None, SCORE_FONT_SIZE)
        score.render_to(screen, (self.x, self.y), self.str_num_score, "white")

    def score_increase(self):
        self.cur_score += 1
        self.str_num_score = str(self.cur_score)
        