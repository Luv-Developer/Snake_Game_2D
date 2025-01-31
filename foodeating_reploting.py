import pygame 
import random
x = pygame.init()
display = pygame.display.set_mode((900,600))
pygame.display.update()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
snakex = 55
snakey = 45
snake_size = 10
exit = False
over = False
velocityx = 0
velocityy = 0
#giving the food 
foodx = random.randint(0,500)
foody = random.randint(0,400)
food_size = 10
fps = 30
clock = pygame.time.Clock()
#Creating the score 
score = 0
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocityx = 10
                velocityy = 0
            elif event.key == pygame.K_LEFT:
                velocityx = -10
                velocityy = 0
            elif event.key == pygame.K_DOWN:
                velocityy  = 10
                velocityx = 0
            elif event.key == pygame.K_UP:
                velocityy = -10
                velocityx = 0
            else:
                print("You have pressed another key")
    snakex = snakex + velocityx
    snakey = snakey + velocityy
    display.fill(white)
    if abs(snakex - foodx)<7 and abs(snakey - foody)<7:
        score = score + 1 
        print("Score is ",score)
        foodx = random.randint(20,500)
        foody = random.randint(20,400)
    food = pygame.draw.rect(display,red,[foodx,foody,food_size,food_size])
    pygame.draw.rect(display,black,[snakex,snakey,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)
