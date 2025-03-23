import pygame
import random


WHITE = (255, 255, 255)
ERASER_COLOR = (0, 0, 0)  # Цвет для "ластика" (черный)
GREEN = (34, 139, 34)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

pygame.display.set_caption("Paint")  # Заголовок окна


def run_paint_app():
    pygame.init()  # Инициализируем Pygame
    canvas = pygame.display.set_mode((640, 480))  # Создаем окно приложения
    frame_rate = pygame.time.Clock()  # Таймер для контроля FPS
    
    brush_size = 15  # Радиус кисти для рисования
    current_color = WHITE  # Текущий выбранный цвет
    prev_pos = None  # Последняя позиция курсора для рисования линий
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return  # Завершаем приложение при закрытии окна или нажатии Esc
                
            # Обработка смены цвета при нажатии клавиш
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    current_color = RED
                elif event.key == pygame.K_g:
                    current_color = GREEN
                elif event.key == pygame.K_b:
                    current_color = BLUE
                elif event.key == pygame.K_y:
                    current_color = YELLOW
                elif event.key == pygame.K_BACKSPACE:
                    current_color = ERASER_COLOR
                elif event.key == pygame.K_x:
                    # Генерируем случайный цвет при нажатии 'x'
                    current_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    
                # Рисование прямоугольника и круга
                elif event.key == pygame.K_w:
                    draw_rectangle(canvas, pygame.mouse.get_pos(), 200, 100, current_color)
                elif event.key == pygame.K_c:
                    draw_circle(canvas, pygame.mouse.get_pos(), current_color)
                    
            # Рисование линии при нажатии и перемещении мыши
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                prev_pos = pygame.mouse.get_pos()
            
            if event.type == pygame.MOUSEMOTION and event.buttons[0] and prev_pos:
                draw_line(canvas, prev_pos, pygame.mouse.get_pos(), brush_size, current_color)
                prev_pos = pygame.mouse.get_pos()
                
        pygame.display.flip()
        frame_rate.tick(60)
        

# draw_line() рисует линию между двумя точками

def draw_line(canvas, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(canvas, color, (x, y), width)
        
# draw_rectangle() рисует прямоугольник в текущем положении курсора

def draw_rectangle(canvas, mouse_pos, width, height, color):
    x, y = mouse_pos
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(canvas, color, rect, 3)
    
# draw_circle() рисует круг в текущем положении курсора

def draw_circle(canvas, mouse_pos, color):
    x, y = mouse_pos
    pygame.draw.circle(canvas, color, (x, y), 100, 3)

run_paint_app()
