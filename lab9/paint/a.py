import pygame
import random

# Определение цветов
WHITE = (255, 255, 255)
ERASER_COLOR = (0, 0, 0)  # Цвет для "ластика" (черный)
GREEN = (34, 139, 34)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

pygame.display.set_caption("Paint")  # Заголовок окна

drawings = []  # Список для хранения фигур и линий
current_shape = None
current_color = WHITE
shape_size = 80


def run_paint_app():
    global current_shape, current_color
    pygame.init()
    canvas = pygame.display.set_mode((640, 480))
    frame_rate = pygame.time.Clock()
    
    font = pygame.font.Font(None, 20)
    instructions = [
        "Клавиши управления:",
        "R - Красный", "G - Зеленый", "B - Синий", "Y - Желтый", "X - Случайный цвет", 
        "W - Прямоугольник", "C - Круг", "S - Квадрат", "T - Прямоугольный треугольник",
        "E - Равносторонний треугольник", "D - Ромб",
        "Backspace - Ластик"
    ]
    
    drawing = False
    start_pos = None
    
    while True:
        canvas.fill((0, 0, 0))  # Очистка экрана
        
        # Отображение инструкций
        y_offset = 5
        for line in instructions:
            text_surface = font.render(line, True, WHITE)
            canvas.blit(text_surface, (5, y_offset))
            y_offset += 15
        
        # Перерисовка всех сохранённых элементов
        for draw in drawings:
            draw()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    current_color = RED
                elif event.key == pygame.K_g:
                    current_color = GREEN
                elif event.key == pygame.K_b:
                    current_color = BLUE
                elif event.key == pygame.K_y:
                    current_color = YELLOW
                elif event.key == pygame.K_x:
                    current_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                elif event.key == pygame.K_w:
                    current_shape = "rectangle"
                elif event.key == pygame.K_c:
                    current_shape = "circle"
                elif event.key == pygame.K_s:
                    current_shape = "square"
                elif event.key == pygame.K_t:
                    current_shape = "right_triangle"
                elif event.key == pygame.K_e:
                    current_shape = "equilateral_triangle"
                elif event.key == pygame.K_d:
                    current_shape = "rhombus"
                elif event.key == pygame.K_BACKSPACE:
                    current_color = ERASER_COLOR
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = pygame.mouse.get_pos()
            
            if event.type == pygame.MOUSEBUTTONUP and drawing:
                end_pos = pygame.mouse.get_pos()
                if current_shape == "rectangle":
                    drawings.append(lambda start=start_pos, end=end_pos, color=current_color: draw_rectangle(canvas, start, end, color))
                elif current_shape == "circle":
                    drawings.append(lambda start=start_pos, end=end_pos, color=current_color: draw_circle(canvas, start, end, color))
                elif current_shape == "square":
                    drawings.append(lambda start=start_pos, end=end_pos, color=current_color: draw_square(canvas, start, end, color))
                elif current_shape == "right_triangle":
                    drawings.append(lambda start=start_pos, end=end_pos, color=current_color: draw_right_triangle(canvas, start, end, color))
                elif current_shape == "equilateral_triangle":
                    drawings.append(lambda start=start_pos, end=end_pos, color=current_color: draw_equilateral_triangle(canvas, start, end, color))
                elif current_shape == "rhombus":
                    drawings.append(lambda start=start_pos, end=end_pos, color=current_color: draw_rhombus(canvas, start, end, color))
                drawing = False
                start_pos = None
        
        pygame.display.flip()
        frame_rate.tick(60)

# Функции для рисования фигур

def draw_rectangle(canvas, start, end, color):
    x1, y1 = start
    x2, y2 = end
    pygame.draw.rect(canvas, color, (x1, y1, x2 - x1, y2 - y1), 3)

def draw_circle(canvas, start, end, color):
    x1, y1 = start
    x2, y2 = end
    radius = max(abs(x2 - x1), abs(y2 - y1)) // 2
    center = ((x1 + x2) // 2, (y1 + y2) // 2)
    pygame.draw.circle(canvas, color, center, radius, 3)

def draw_square(canvas, start, end, color):
    x1, y1 = start
    x2, y2 = end
    size = min(abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(canvas, color, (x1, y1, size, size), 3)

def draw_right_triangle(canvas, start, end, color):
    x1, y1 = start
    x2, y2 = end
    points = [(x1, y1), (x2, y1), (x1, y2)]
    pygame.draw.polygon(canvas, color, points, 3)

def draw_equilateral_triangle(canvas, start, end, color):
    x1, y1 = start
    x2, y2 = end
    size = min(abs(x2 - x1), abs(y2 - y1))
    height = (size * (3 ** 0.5)) / 2
    points = [(x1, y2), (x2, y2), (x1 + size // 2, y2 - height)]
    pygame.draw.polygon(canvas, color, points, 3)

def draw_rhombus(canvas, start, end, color):
    x1, y1 = start
    x2, y2 = end
    size = min(abs(x2 - x1), abs(y2 - y1))
    points = [(x1, y1 - size // 2), (x1 + size // 2, y1), (x1, y1 + size // 2), (x1 - size // 2, y1)]
    pygame.draw.polygon(canvas, color, points, 3)

run_paint_app()
