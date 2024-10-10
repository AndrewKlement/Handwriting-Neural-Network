from .settings import *

class Button:
    def __init__(self, x, y, width, height, color, text=None, text_color=black):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw_button(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 2)
        if self.text:
            text = font_size.render(self.text, 1, self.text_color)
            window.blit(text, (
            self.x + self.width / 2 - text.get_width() / 2, self.y + self.height / 2 - text.get_height() / 2))

    def draw_result(self, window):
        text = font_size.render(self.text, 1, self.text_color)
        window.blit(text, (
        self.x + self.width / 2 - text.get_width() / 2, self.y + self.height / 2 - text.get_height() / 2))

    def clicked(self, position):
        x, y = position
        if not (self.x <= x <= self.x + self.width):
            return False
        if not (self.y <= y <= self.y + self.height):
            return False

        return True
