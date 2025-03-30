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

def game_over_screen():
    game_window.fill(COLOR_RED)
    game_over_text = font_large.render("Game Over", True, COLOR_BLACK)
    restart_text = font_small.render("Press R to Restart", True, COLOR_BLACK)
    game_window.blit(game_over_text, (50, 250))
    game_window.blit(restart_text, (100, 350))
    pygame.display.update()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_r:
                waiting = False  # Перезапуск игры
                main_game()

def main_game():
    global player_score, collected_coins, enemy_speed
    player_score = 0
    collected_coins = 0
    enemy_speed = 5
    
    # Загрузка изображений
    bg_image = pygame.image.load("lab8/racer/image/AnimatedStreet.png")
    player_car_image = pygame.image.load("lab8/racer/image/Player.png")
    enemy_car_image = pygame.image.load("lab8/racer/image/Enemy.png")
    coin_image = pygame.image.load("lab8/racer/image/coin.png")
    
    # Классы
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
            if pressed_keys[K_UP] and self.rect.top > 0:
                self.rect.move_ip(0, -5)
            if pressed_keys[K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
                self.rect.move_ip(0, 5)

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
    
    class GoldCoin(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(coin_image, (30, 30))
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
            self.weight = random.randint(1, 5)
        
        def move(self):
            self.rect.move_ip(0, enemy_speed)
            if self.rect.top > SCREEN_HEIGHT:
                self.rect.top = 0
                self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    
    # Создание объектов
    player = PlayerCar()
    enemy = EnemyCar()
    coin = GoldCoin()
    
    enemy_group = pygame.sprite.Group()
    enemy_group.add(enemy)
    
    coin_group = pygame.sprite.Group()
    coin_group.add(coin)
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player, enemy, coin)
    
    # Игровой цикл
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        game_window.blit(bg_image, (0, 0))
        
        score_display = font_small.render(f"Score: {player_score}", True, COLOR_BLACK)
        coins_display = font_small.render(f"Coins: {collected_coins}", True, COLOR_BLACK)
        game_window.blit(score_display, (10, 10))
        game_window.blit(coins_display, (280, 10))
        
        for sprite in all_sprites:
            game_window.blit(sprite.image, sprite.rect)
            sprite.move()
        
        # Проверка столкновения игрока с врагом
        if pygame.sprite.spritecollideany(player, enemy_group):
            pygame.mixer.Sound('crash.wav').play()
            time.sleep(0.5)
            game_over_screen()
        
        # Проверка столкновения игрока с монетой
        collected = pygame.sprite.spritecollideany(player, coin_group)
        if collected:
            collected_coins += collected.weight
            enemy_speed += 0.1* collected.weight
            collected.kill()
            
        if len(coin_group) == 0:
            new_coin = GoldCoin()
            coin_group.add(new_coin)
            all_sprites.add(new_coin)
        
        pygame.display.update()
        clock.tick(FPS)

# Запуск игры
font_large = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Race")
main_game()
