import pygame, sys, random, time
from pygame.locals import *

pygame.init()

# Настройка FPS (кадров в секунду)
FPS = 60
clock = pygame.time.Clock()

# Цвета
COLOR_BLUE  = (0, 0, 255)
COLOR_RED   = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# Размеры экрана
SCREEN_WIDTH = 405
SCREEN_HEIGHT = 600
enemy_speed = 5 
player_score = 0  
collected_coins = 0  

# Шрифты
font_large = pygame.font.SysFont("Verdana", 60)  
font_small = pygame.font.SysFont("Verdana", 20)  
game_over_text = font_large.render("Game Over", True, COLOR_BLACK)  

# Загрузка изображений
bg_image = pygame.image.load("lab8/racer/image/AnimatedStreet.png")
player_car_image = pygame.image.load("lab8/racer/image/Player.png")
enemy_car_image = pygame.image.load("lab8/racer/image/Enemy.png")
coin_image = pygame.image.load("lab8/racer/image/coin.png")

game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_window.fill(COLOR_WHITE)
pygame.display.set_caption("Race")

# Класс врага
class EnemyCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = enemy_car_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0) 

    def move(self):
        global player_score
        self.rect.move_ip(0, enemy_speed) 
        if self.rect.top > SCREEN_HEIGHT:
            player_score += 1  
            self.rect.top = 0  
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс монеты
class GoldCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.transform.scale(coin_image, (30, 30))  
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

    def move(self):
        self.rect.move_ip(0, enemy_speed)  
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0  
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс игрока
class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = player_car_image
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)  

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)  
        if pressed_keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)  

# Создание объектов
player = PlayerCar()
enemy = EnemyCar()
coin = GoldCoin()

# Группы спрайтов
enemy_group = pygame.sprite.Group()
enemy_group.add(enemy)

coin_group = pygame.sprite.Group()
coin_group.add(coin)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coin)

# Ускорение врагов
INCREASE_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INCREASE_SPEED, 1000)

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == INCREASE_SPEED:
            enemy_speed += 0.5  
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    game_window.blit(bg_image, (0, 0))
    
    score_display = font_small.render(f"Score: {player_score}", True, COLOR_BLACK)
    coins_display = font_small.render(f"Coins: {collected_coins}", True, COLOR_BLACK)
    
    game_window.blit(score_display, (10, 10))  
    game_window.blit(coins_display, (320, 10))  

    for sprite in all_sprites:
        game_window.blit(sprite.image, sprite.rect)
        sprite.move()

    # Проверка столкновения игрока с врагом
    if pygame.sprite.spritecollideany(player, enemy_group):
        pygame.mixer.Sound('crash.wav').play()  
        time.sleep(0.5)

        game_window.fill(COLOR_RED)  
        game_window.blit(game_over_text, (30, 250))  

        pygame.display.update()
        for sprite in all_sprites:
            sprite.kill()  
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Проверка столкновения игрока с монетой
    collected = pygame.sprite.spritecollideany(player, coin_group)
    if collected:
        collected.kill()  
        collected_coins += 1  

    if len(coin_group) == 0:
        new_coin = GoldCoin()
        coin_group.add(new_coin)
        all_sprites.add(new_coin)

    pygame.display.update()
    clock.tick(FPS)
