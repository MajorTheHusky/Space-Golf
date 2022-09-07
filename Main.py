from turtle import pos
import pygame
import mat
from math import *
import Planet
import Level
import Button

pygame.init()



asteroidColor = (35, 35, 35)

WIDTH, HEIGHT = 800, 600

asteroidPos = (100, 100)
asteroidRad = 10
mousePos = (0, 0)

posDif = (0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Golf")

# earth = Planet.Planet((0, 0, 255), (500, 500), 25)
# mars = Planet.Planet((255, 0, 0), (350, 350), 35)

level1 = Level.Level(0, 3, (100, 100), [(0, 0, 255), (255, 0, 0)], [(500, 500), (350, 350)], [25, 35])
level2 = Level.Level(0, 4, (500, 100), [(0, 0, 255), (255, 0, 0), (0, 255, 0)], [(450, 500), (250, 300), [500, 350]], [15, 50, 55])
level3 = Level.Level(0, 1, (400, 100), [(0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 255, 0), (255, 0, 0), (0, 255, 0), (255, 0, 0), (0, 255, 0), (255, 0, 0)], [(400, 600), (300, 300), (500, 300), (300, 400), (500, 400), (300, 500), (500, 500), (300, 600), (500, 600)], [50, 50, 50, 50, 50, 50, 50, 50, 50])

levels = [level1, level2, level3]

currentLevel = level1
currentLevelNum = 0

planets = currentLevel.get_planets()

target = planets[currentLevel.get_target_number()]

attempts = currentLevel.get_attempt_amount()

canShoot = True

changingOrResseting = 3

def ChangeOrReset():
    global changingOrResseting

    if changingOrResseting == 0:
        NextLevel()
    if changingOrResseting == 1:
        RestartLevel()

    changingOrResseting = 3

changeOrRestartButton = Button.Button(200, 250, 400, 100, screen, ChangeOrReset)


def RestartLevel():
    global attempts, asteroidColor, asteroidPos, asteroidRad, mousePos, posDif, target, planets, canShoot

    attempts -= 1

    if attempts == 0:
        pygame.quit()

    canShoot = True

    asteroidColor = (35, 35, 35)
    asteroidPos = currentLevel.get_asteroid_pos()
    asteroidRad = 10
    mousePos = (0, 0)

    posDif = (0, 0)

    planets = currentLevel.get_planets()

    target = planets[currentLevel.get_target_number()]

def NextLevel():
    global attempts, asteroidColor, asteroidPos, asteroidRad, mousePos, posDif, target, planets, currentLevel, currentLevelNum, canShoot

    canShoot = True

    currentLevelNum += 1
    currentLevel = levels[currentLevelNum]

    asteroidColor = (35, 35, 35)
    asteroidPos = currentLevel.get_asteroid_pos()
    asteroidRad = 10
    mousePos = (0, 0)

    posDif = (0, 0)

    planets = currentLevel.get_planets()

    target = planets[currentLevel.get_target_number()]

    attempts = currentLevel.get_attempt_amount()


while True:
    screen.fill((0, 0, 0))

    font = pygame.font.Font('Quicksand-SemiBold.ttf', 48)
    attemptsText = font.render('Attempts Left: ' + str(attempts), True, (255, 255, 255))
    attemptsRect = attemptsText.get_rect()
    attemptsRect.center = (400, 50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if changingOrResseting == 3:
            if pygame.mouse.get_pressed()[0] == True and canShoot:
                canShoot = False

                mousePos = pygame.mouse.get_pos()
                posDif = (mousePos[0] - asteroidPos[0], mousePos[1] - asteroidPos[1])
                posDif = (posDif[0] / math.sqrt(math.pow(posDif[0], 2) + math.pow(posDif[1], 2)), posDif[1] / math.sqrt(math.pow(posDif[0], 2) + math.pow(posDif[1], 2)))
    
    if changingOrResseting == 3:
        for planet in planets:
            distance = sqrt(pow((asteroidPos[0] - planet.get_pos()[0]), 2) + pow((asteroidPos[1] - planet.get_pos()[1]), 2))
            if distance - asteroidRad < planet.get_rad() * 3:
                posDif = (posDif[0] + ((planet.get_pos()[0] - asteroidPos[0])/50000), posDif[1] + ((planet.get_pos()[1] - asteroidPos[1])/50000))

            if distance - asteroidRad <= planet.get_rad():
                if planet == target:
                    changingOrResseting = 0
                else:
                    if changingOrResseting == 3:
                        changingOrResseting = 1
    

    asteroidPos = (asteroidPos[0] + posDif[0] * .225, asteroidPos[1] + posDif[1] * .225)

    if asteroidPos[0] < asteroidRad or asteroidPos[0] > WIDTH - asteroidRad or asteroidPos[1] < asteroidRad or asteroidPos[1] > HEIGHT - asteroidRad:
        if changingOrResseting == 3:
            changingOrResseting = 1

    if changingOrResseting == 3:
        pygame.draw.circle(screen, asteroidColor, asteroidPos, asteroidRad)
        
        for planet in planets:
            planet.draw(screen)

        screen.blit(attemptsText, attemptsRect)
    else:
        if currentLevelNum + 1 < len(levels):
            changeOrRestartButton.process(changingOrResseting)
        else:
            font = pygame.font.Font('Quicksand-SemiBold.ttf', 96)
            winText = font.render('You Win!', True, (255, 255, 255))
            winRect = attemptsText.get_rect()
            winRect.center = (400, 250)
            screen.blit(winText, winRect)

    pygame.display.update()
