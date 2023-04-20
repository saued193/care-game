import pygame
from pygame.locals import *
import random

size = width,height = (800,800)
road_w = int(width / 1.6)
roadmark_w = int(width / 80)
right_lane = int(width / 2 + road_w / 4 - roadmark_w / 2)
left_lane = int(width / 2 - road_w / 4 + roadmark_w / 2)
speed = 2
running = True
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("car game")
screen.fill((60,220,0))
mycare = pygame.image.load("C:/Users/DELL/OneDrive/Desktop/car/assets/mycar.png")
cars = []
for i in range(1,4):
    cars.append(pygame.image.load(f"C:/Users/DELL/OneDrive/Desktop/car/assets/enemy{i}.png"))
othercar = cars[0]

mycare_loc = mycare.get_rect()
othercar_loc = othercar.get_rect()

mycare_loc.center = (right_lane, height * 0.8)
othercar_loc.center = (left_lane, height * 0.2)

counter = 0

while running:
    
    counter += 1
    if counter >= 2000:
        print(f'speed increased to {speed}')
        speed += 0.25
        counter = 0
    othercar_loc.bottom += speed
    if othercar_loc.center[1] > height:
        othercar = cars[random.randint(0,2)]
        if random.randint(0,1) == 0:
            othercar_loc.center = (left_lane, -200)
        else:
            othercar_loc.center = (right_lane, -200)
            
    if othercar_loc.center[0] == mycare_loc.center[0] and othercar_loc.bottom > mycare_loc.top:
        print("Crash happend, GAME OVER")
        break
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                mycare_loc.center = (left_lane, height * 0.8)
            if event.key in [K_d, K_RIGHT]:
               mycare_loc.center = (right_lane, height * 0.8)
               
    pygame.draw.rect(screen, (60,60,60), (width / 2 - road_w /2,0,road_w,height))
    pygame.draw.rect(screen, (255,240,0), (width / 2 - roadmark_w /2, 0, roadmark_w, height))
    pygame.draw.rect(screen, (255,255,255), (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height))
    pygame.draw.rect(screen, (255,255,255), (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height))
    
    screen.blit(mycare, mycare_loc)
    screen.blit(othercar, othercar_loc)
    pygame.display.update()
    
    
    
    
    
    
    
    pygame.quit
    
    
    
    
    