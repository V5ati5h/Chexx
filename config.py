import pygame
import os

from sound import Sound
from theme import Theme

class Config:

    def __init__(self):
        self.themes = []
        self._add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]
        self.font = pygame.font.SysFont('monospace', 18, bold=True)
        self.move_sound = Sound(
            os.path.join('assets/sounds/move.wav'))
        self.capture_sound = Sound(
            os.path.join('assets/sounds/capture.wav'))

    def change_theme(self):
        self.idx += 1
        self.idx %= len(self.themes)
        self.theme = self.themes[self.idx]

    def _add_themes(self):
        green = Theme((234, 235, 200), (119, 154, 88), (244, 247, 116), (172, 195, 51), '#C86464', '#C84646')
        brown = Theme((235, 209, 166), (165, 117, 80), (245, 234, 100), (209, 185, 59), '#C86464', '#C84646')
        blue = Theme((229, 228, 200), (60, 95, 135), (123, 187, 227), (43, 119, 191), '#C86464', '#C84646')
        gray = Theme((120, 119, 118), (86, 85, 84), (99, 126, 143), (82, 102, 128), '#C86464', '#C84646')
        wood = Theme((193, 154, 107), (101, 67, 33), (255, 248, 220), (238, 232, 170), '#C86464', '#C84646')
        royal_purple = Theme((192, 181, 205), (77, 57, 104), (255, 251, 223), (249, 231, 159), '#C86464', '#C84646')
        light_pastel = Theme((240, 240, 240), (200, 200, 200), (255, 255, 255), (100, 100, 100), '#C86464', '#C84646')
        sleek_gray = Theme((220, 220, 220), (150, 150, 150), (200, 200, 200), (100, 100, 100), '#333333', '#C84646')
        soft_blue = Theme((220, 240, 255), (150, 200, 255), (255, 250, 230), (240, 230, 200), '#C86464', '#C84646')
        warm_neutrals = Theme((240, 230, 210), (200, 180, 150), (230, 200, 180), (180, 150, 120), '#C86464', '#C84646')

        self.themes = [green, brown, blue, gray, wood, royal_purple, light_pastel, sleek_gray, soft_blue, warm_neutrals]
