# tutorial we followed - #https://www.edureka.co/blog/snake-game-with-pygame/#screen


import pygame
import random
pygame.init()

# display
title = pygame.image.load('Title Screen.png')
rules = pygame.image.load('rules.png')



dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('The Great Snake Game')
background = pygame.image.load('grid background.png')
#dis.blit(title, (0, 0))
ending = pygame.image.load('ending.png')
clock = pygame.time.Clock()


# snake
snakeHead = pygame.image.load('snake head.png')
snakeBody = pygame.image.load('snake body.png')

# variables
game_over = False
ruledis = False
x = (400 * 0.45)
y = (300 * 0.8)
blue = (255,95,31)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# score
score_font = pygame.font.SysFont("Times", 20)


# methods

dis.blit(title, (0,0))
pygame.display.update()
pygame.event.pump() #http://stackoverflow.com/questions/18839039/how-to-wait-some-time-in-pygame
pygame.time.delay(5000)
dis.blit(rules, (0,0))
pygame.display.update()
pygame.event.pump()
pygame.time.delay(5000)


def score(points):
    value = score_font.render("Your Score: " + str(points), True, red)
    dis.blit(value, [3, 7])

def snake(x,y):
    dis.blit(snakeHead, (x,y))

def txt_display(txt,color):
    txt = score_font.render(txt, True, color)
    dis.blit(txt, [10, 100])

def body(s_list):
    for x in s_list:
        pygame.draw.rect(dis, green, [x[0], x[1], 10, 10])




# game
def loop():
    game_over = False
    exit = False

    x1 = 150
    y1 = 150

    x1_change = 0
    y1_change = 0

    s_list = []
    s_length = 1

    food_x = round(random.randrange(0, 290) / 10.0) * 10.0
    food_y = round(random.randrange(30, 290) / 10.0) * 10.0

    power_rand = round(random.randrange(8, 11))
    print(power_rand)
    counter = 0

    powerup_onscreen = False
    snake_speed = 15

    runs = 0


    while not game_over:

        while exit == True:
            dis.blit(ending, (0,0))
            #txt_display("You died. Type 'Q' to Quit and 'P' to Play again.", red)
            score(s_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        exit = False
                    if event.key == pygame.K_p:
                        loop()


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

        if x1 >= 400 or x1 < 0 or y1 >= 300 or y1 < 30:
            exit = True

        # snake location
        x1 += x1_change
        y1 += y1_change
        dis.blit(background, (0, 0))


        if counter == power_rand:
            pygame.draw.rect(dis, black, [food_x, food_y, 10, 10])
            powerup_onscreen = True
        else:
            pygame.draw.rect(dis, blue, [food_x, food_y, 10, 10])

        s_head = []
        s_head.append(x1)
        s_head.append(y1)
        s_list.append(s_head)
        if len(s_list) > s_length:
            del s_list[0]

        for x in s_list[:-1]:
            if x == s_head:
                exit = True

        # power up



        body(s_list)
        score(s_length -1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            s_length += 1
            counter = counter + 1
            print("Counter: ", counter)
            food_x = round(random.randrange(0, 290) / 10.0) * 10.0
            food_y = round(random.randrange(30, 290) / 10.0) * 10.0
            if powerup_onscreen:
                snake_speed = 10
                print("slow", snake_speed)
                powerup_onscreen = False
                power_rand = round(random.randrange(8, 11))
                counter = 0
            if runs == 5:
                snake_speed = 15
                print("fast", snake_speed)
                runs = 0


            runs = runs + 1
            print(runs)
        clock.tick(snake_speed)



    #while not game_over:
    pygame.quit()
    quit()


loop()
