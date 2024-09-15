import pygame
import time
import os


WIDTH = 800
HEIGHT = 500

pygame.font.init()

pygame.display.set_caption("Health:")

YELLOW_SPACESHIP = pygame.image.load(os.path.join("photos","Image20240813172642.png"))
RED_SPACESHIP = pygame.image.load(r"C:\Users\Admin\OneDrive\Documents\Game Dev 2\photos\Image20240813172853.png")
BACKGROUND = pygame.image.load(r"C:\Users\Admin\OneDrive\Documents\Game Dev 2\photos\Image20240813172900.png")

screen = pygame.display.set_mode((WIDTH,HEIGHT))
NEW_YELLOW = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP,(50,50)),90)
NEW_RED = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP,(50,50)),270)
yellow = pygame.Rect(100,300,50,50)
red = pygame.Rect(700,300,50,50)
BORDER = pygame.Rect(WIDTH/2,0,25,500)
yellow_bullets = []
red_bullets = []
yellow_health = 10
red_health = 10


def yellow_key_handle(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x > 0: #LEFT
        yellow.x -= 1
    if keys_pressed[pygame.K_d] and yellow.x < BORDER.x - 25: #RIGHT
        yellow.x += 1
    if keys_pressed[pygame.K_s] and yellow.y < 475: #DOWN
        yellow.y += 1
    if keys_pressed[pygame.K_w] and yellow.y > 5: #UP
        yellow.y -= 1

def red_key_handle(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x > BORDER.x + 25: #LEFT
        red.x -= 1
    if keys_pressed[pygame.K_RIGHT] and red.x < 775: #RIGHT
        red.x += 1
    if keys_pressed[pygame.K_DOWN] and red.y < 475: #DOWN
        red.y += 1
    if keys_pressed[pygame.K_UP] and red.y > 5: #UP
        red.y -= 1
running = True
while running:
    #Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and len(yellow_bullets) < 3:
                bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                yellow_bullets.append(bullet)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and len(red_bullets) < 3:
                bullet = pygame.Rect(red.x + red.width, red.y + red.height//2 - 2, 10, 5)
                red_bullets.append(bullet)
    screen.blit(BACKGROUND,(0,0))
    screen.blit(NEW_YELLOW,(yellow.x,yellow.y))
    screen.blit(NEW_RED,(red.x,red.y))
    for bullet in yellow_bullets:
        pygame.draw.rect(screen,"yellow",bullet)
        bullet.x += 10
        if bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
        elif red.colliderect(bullet):
            red_health = red_health - 1
            yellow_bullets.remove(bullet)
    winner_text = ""

    for bullet in red_bullets:
        pygame.draw.rect(screen,"red",bullet)
        bullet.x -= 10
        if bullet.x < 0:
            red_bullets.remove(bullet)
        elif yellow.colliderect(bullet):
            yellow_health = yellow_health - 1
            red_bullets.remove(bullet)

    if red_health <= 0:
        winner_text = "Yellow Wins!"
        font=pygame.font.SysFont("Times New Roman",50)
        text=font.render(winner_text,True,(0,0,0))
        screen.blit(text, (250,200))
        pygame.display.update()
        pygame.time.delay(5000)
        break
        


    if yellow_health <= 0:
        winner_text = "Red Wins!"
        font=pygame.font.SysFont("Times New Roman",50)
        text=font.render(winner_text,True,(0,0,0))
        screen.blit(text, (250,200))
        pygame.display.update()
        pygame.time.delay(5000)
        break

        

    pygame.draw.rect(screen,"black",BORDER)

    font=pygame.font.SysFont("Times New Roman",50)
    text=font.render("Health: "+str(yellow_health),True,(0,0,0))
    screen.blit(text, (0,0))

    text=font.render("Health: "+str(red_health),True,(0,0,0))
    screen.blit(text, (525,0))

    keys_pressed = pygame.key.get_pressed()
    yellow_key_handle(keys_pressed,yellow)

    red_key_handle(keys_pressed,red)

    pygame.display.update()


