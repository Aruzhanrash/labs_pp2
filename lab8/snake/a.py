import pygame, random, sys, time
pygame.init()

# Константы экрана и игры
WIDTH, HEIGHT = 620, 400
TILE_SIZE = 20  
VELOCITY = 5  # Уменьшена скорость змейки

# Цвета
BACKGROUND_COLOR = (30, 30, 30)
SNAKE_COLOR = (0, 200, 200)
FOOD_COLOR = (200, 50, 50)
TEXT_COLOR = (255, 255, 255)

# Создание экрана
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

font_style = pygame.font.Font(None, 30)

# Функция для отображения текста
def show_text(message, x, y, color=TEXT_COLOR):
    text_surface = font_style.render(message, True, color)
    window.blit(text_surface, (x, y))

# Функция генерации еды (не на змейке и не на стене)
def spawn_food(snake_body):
    while True:
        food_x = random.randint(0, (WIDTH - TILE_SIZE) // TILE_SIZE) * TILE_SIZE
        food_y = random.randint(0, (HEIGHT - TILE_SIZE) // TILE_SIZE) * TILE_SIZE
        if (food_x, food_y) not in snake_body and 0 <= food_x < WIDTH and 0 <= food_y < HEIGHT:
            return food_x, food_y

# Функции для отрисовки змейки и еды
def render_snake(body):
    for part in body:
        pygame.draw.rect(window, SNAKE_COLOR, (part[0], part[1], TILE_SIZE, TILE_SIZE))

def render_food(position):
    pygame.draw.rect(window, FOOD_COLOR, (position[0], position[1], TILE_SIZE, TILE_SIZE))

# Основная игровая функция
def main():
    snake_body = [(100, 100), (90, 100), (80, 100)]
    move_direction = "RIGHT"
    food_pos = spawn_food(snake_body)
    points = 0
    stage = 1
    speed = VELOCITY
    
    clock = pygame.time.Clock()
    game_running = True
    
    while game_running:
        window.fill(BACKGROUND_COLOR)
        
        # Обработка событий (движение)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and move_direction != "DOWN":
                    move_direction = "UP"
                elif event.key == pygame.K_DOWN and move_direction != "UP":
                    move_direction = "DOWN"
                elif event.key == pygame.K_LEFT and move_direction != "RIGHT":
                    move_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and move_direction != "LEFT":
                    move_direction = "RIGHT"
        
        # Движение змейки
        x, y = snake_body[0]
        if move_direction == "UP":
            y -= TILE_SIZE
        elif move_direction == "DOWN":
            y += TILE_SIZE
        elif move_direction == "LEFT":
            x -= TILE_SIZE
        elif move_direction == "RIGHT":
            x += TILE_SIZE
        
        # Проверка на столкновения
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or (x, y) in snake_body:
            game_running = False  # Проигрыш
        
        # Добавление нового сегмента змейки
        snake_body.insert(0, (x, y))
        
        # Проверка еды
        if (x, y) == food_pos:
            points += 1
            food_pos = spawn_food(snake_body)
            if points % 3 == 0:
                stage += 1
                speed += 1  # Медленнее увеличиваем скорость
        else:
            snake_body.pop()
        
        # Отрисовка элементов
        render_snake(snake_body)
        render_food(food_pos)
        
        # Отображение счета
        show_text(f"Очки: {points}", 10, 10)
        show_text(f"Уровень: {stage}", 500, 10)
        
        pygame.display.update()
        clock.tick(speed)
    
    # Экран поражения
    window.fill(BACKGROUND_COLOR)
    show_text("Вы проиграли!", WIDTH // 2 - 60, HEIGHT // 2 - 10, FOOD_COLOR)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    sys.exit()

# Запуск игры
main()
