import pygame 
import time
import math
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.display.set_caption("MICKEY MOUSE CLOCK") 
left = pygame.image.load("lab7/clock/ima/leftarm.png")  # Левая рука (секунды)
right = pygame.image.load("lab7/clock/ima/rightarm.png")  # Правая рука (минуты)
main = pygame.transform.scale(pygame.image.load("lab7/clock/ima/clock.png"), (800, 600))

done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Получаем текущее время
    current_time = time.localtime()  
    minute = current_time.tm_min
    second = current_time.tm_sec

    minute_angle = -(minute * 6 + second * 0.1)  
    second_angle = -(second * 6)

    screen.fill((255, 255, 255))  
    screen.blit(main, (0, 0)) 

    scaled_right = pygame.transform.scale(right, (800, 600))  # Размер минутной стрелки
    scaled_left = pygame.transform.scale(left, (41, 500))  # Размер секундной стрелки

    rotated_rightarm = pygame.transform.rotate(scaled_right, minute_angle)
    rightarm_rect = rotated_rightarm.get_rect(center=(400, 300))  
    screen.blit(rotated_rightarm, rightarm_rect)
    rotated_leftarm = pygame.transform.rotate(scaled_left, second_angle)
    leftarm_rect = rotated_leftarm.get_rect(center=(400, 300)) 
    screen.blit(rotated_leftarm, leftarm_rect)

    pygame.display.flip() 
    clock.tick(60)  

pygame.quit()
