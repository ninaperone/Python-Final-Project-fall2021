# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pygame

pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('The Great Snake Game')
game_over = False
crashed = False

clock = pygame.time.Clock()

snakeHead = pygame.image.load('snake head.png')
snakeBody = pygame.image.load('snake body.png')
def snake(x,y):
    dis.blit(snakeHead, (x,y))

x = (400 * 0.45)
y = (300 * 0.8)
blue = (0,0,255)
black = (0, 0, 0)
x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
    x1 += x1_change
    y1 += y1_change
    dis.fill(black)
    #snake(x,y)
    pygame.draw.rect(dis, blue,[x1,y1,10,10])
    pygame.display.update()
    clock.tick(30)



#while not game_over:


pygame.quit()
quit()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
