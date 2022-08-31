import pygame


class Button():
    def __init__(self, x, y, width, height, screen, onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.buttonColor = '#ffffff'
        textSize = 75
        buttonText = "Next Level"

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        font = pygame.font.Font('Quicksand-SemiBold.ttf', textSize)
        self.buttonSurf = font.render(" " + buttonText, True, (20, 20, 20))


    def process(self, nextOrAgain):
        textSize = 72 if nextOrAgain==0 else 75
        buttonText = "Next Level" if nextOrAgain==0 else "Try Again"

        font = pygame.font.Font('Quicksand-SemiBold.ttf', textSize)
        self.buttonSurf = font.render(" " + buttonText, True, (20, 20, 20))

        mousePos = pygame.mouse.get_pos()
        self.buttonColor = self.fillColors['normal']
        if self.buttonRect.collidepoint(mousePos):
            self.buttonColor = self.fillColors['hover']
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonColor = self.fillColors['pressed']
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        # self.screen.blit(self.buttonSurface, self.buttonRect)
        pygame.draw.rect(self.screen, self.buttonColor, self.buttonRect, 0, 10)
        self.screen.blit(self.buttonSurf, self.buttonRect)