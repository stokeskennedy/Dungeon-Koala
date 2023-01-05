from main import *

class Button:
    def __init__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.draw()

    def draw(self):
        button_text = font.render(self.text, True, black)
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (290, 30))
        
        if self.enabled:
            if self.check_click():
                pygame.draw.rect(screen, green, button_rect, 0, 5)
            else:
                pygame.draw.rect(screen, blue, button_rect, 0, 5)
        else:
            pygame.draw.rect(screen, grey, button_rect, 0, 5)
    
        pygame.draw.rect(screen, black, button_rect, 2, 5)
        screen.blit(button_text, (self.x_pos + 5, self.y_pos + 5))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (280, 30))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False