import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Shooter Game")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("bg.png")
background = pygame.transform.scale(background, (800,600))

Spaceshipimg = pygame.image.load("shooter.png")
Alienimg = []
AlienX = []
AlienY = []
AlienspeedX = []
AlienspeedY = []

no_of_aliens = 6

for i in range(no_of_aliens):
    Alienimg.append(pygame.image.load("alien.png"))
    AlienX.append(random.randint(0,736))
    AlienY.append(random.randint(30,150))
    AlienspeedX.append(-0.2)
    AlienspeedY.append(40)

score = 0

SpaceshipX = 370
SpaceshipY = 480

ChangeX = 0

bulletimg = pygame.image.load("bullet.png")

check = False
bulletX = 386
bulletY = 480

running = True

font = pygame.font.SysFont("Arial", 20,)

font_gameover = pygame.font.SysFont("Arial", 64,'bold')

def gameover():
    img = font_gameover.render('GAME OVER',True,'white')
    screen.blit(img,(240,250))

def score_text():
    img_gameover = font.render(f'Score:{score}',True,'white')
    screen.blit(img_gameover,(10,10))


while running:

    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ChangeX = -1
            if event.key == pygame.K_RIGHT:
                ChangeX = 1
            if event.key == pygame.K_SPACE:
                if check is False:
                    check = True
                    bulletX = SpaceshipX + 16
        if event.type == pygame.KEYUP:
            ChangeX = 0

    SpaceshipX += ChangeX

    if SpaceshipX <= 0:
        SpaceshipX = 0
    elif SpaceshipX >= 736:
        SpaceshipX = 736

    for i in range(no_of_aliens):

        AlienX[i] += AlienspeedX[i]

        if AlienX[i] <= 0:
            AlienspeedX[i] = 0.5
            AlienY[i]+=AlienspeedY[i]
        elif AlienX[i] >= 736:
            AlienspeedX[i] = -0.5
            AlienY[i] +=AlienspeedY[i]

        if AlienY[i] > 410:
            for j in range(no_of_aliens):
                AlienY[j] = 2000
            AlienY[i] = 2000
            gameover()
            break

        distance = math.sqrt((bulletX - AlienX[i]) ** 2 + (bulletY - AlienY[i]) ** 2)
        if distance < 30:
            bulletY = 480
            check = False
            score += 1
            AlienX[i] = random.randint(0, 736)
            AlienY[i] = random.randint(30, 150)
        screen.blit(Alienimg[i], (AlienX[i], AlienY[i]))

    if bulletY <= 0:
        bulletY = 480
        check = False
    if check is True:
        screen.blit(bulletimg, (bulletX, bulletY))
        bulletY-=5

    screen.blit(Spaceshipimg,(SpaceshipX,SpaceshipY))
    score_text()
    pygame.display.update()

pygame.quit()
