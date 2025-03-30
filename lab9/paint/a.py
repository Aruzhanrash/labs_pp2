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

def run_paint_app():
    pygame.init()
    canvas = pygame.display.set_mode((640, 480))
    frame_rate = pygame.time.Clock()
    
    brush_size = 10
    shape_size = 80
    current_color = WHITE
    prev_pos = None
    
    font = pygame.font.Font(None, 20)
    instructions = [
        "Клавиши управления:",
        "W - Прямоугольник", "C - Круг", "S - Квадрат", "T - Прямоугольный треугольник",
        "E - Равносторонний треугольник", "D - Ромб",
        "Стрелки вверх/вниз - Изменение размера фигуры",
        "Стрелки влево/вправо - Изменение размера кисти",
        "Backspace - Ластик"
    ]
    
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
                pos = pygame.mouse.get_pos()
                if event.key == pygame.K_w:
                    drawings.append(lambda pos=pos, size=shape_size, color=current_color: draw_rectangle(canvas, pos, size, color))
                elif event.key == pygame.K_c:
                    drawings.append(lambda pos=pos, size=shape_size, color=current_color: draw_circle(canvas, pos, size, color))
                elif event.key == pygame.K_s:
                    drawings.append(lambda pos=pos, size=shape_size, color=current_color: draw_square(canvas, pos, size, color))
                elif event.key == pygame.K_t:
                    drawings.append(lambda pos=pos, size=shape_size, color=current_color: draw_right_triangle(canvas, pos, size, color))
                elif event.key == pygame.K_e:
                    drawings.append(lambda pos=pos, size=shape_size, color=current_color: draw_equilateral_triangle(canvas, pos, size, color))
                elif event.key == pygame.K_d:
                    drawings.append(lambda pos=pos, size=shape_size, color=current_color: draw_rhombus(canvas, pos, size, color))
                elif event.key == pygame.K_BACKSPACE:
                    current_color = ERASER_COLOR
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                prev_pos = pygame.mouse.get_pos()
            
            if event.type == pygame.MOUSEMOTION and event.buttons[0] and prev_pos:
                start, end = prev_pos, pygame.mouse.get_pos()
                drawings.append(lambda start=start, end=end, width=brush_size, color=current_color: draw_line(canvas, start, end, width, color))
                prev_pos = end
                
        pygame.display.flip()
        frame_rate.tick(60)

# Функции для рисования фигур

def draw_line(canvas, start, end, width, color):
    pygame.draw.line(canvas, color, start, end, width)

def draw_rectangle(canvas, mouse_pos, size, color):
    x, y = mouse_pos
    pygame.draw.rect(canvas, color, (x, y, size * 1.5, size), 3)

def draw_circle(canvas, mouse_pos, size, color):
    x, y = mouse_pos
    pygame.draw.circle(canvas, color, (x, y), size, 3)

def draw_square(canvas, mouse_pos, size, color):
    x, y = mouse_pos
    pygame.draw.rect(canvas, color, (x, y, size, size), 3)

def draw_right_triangle(canvas, mouse_pos, size, color):
    x, y = mouse_pos
    points = [(x, y), (x + size, y), (x, y + size)]
    pygame.draw.polygon(canvas, color, points, 3)

def draw_equilateral_triangle(canvas, mouse_pos, size, color):
    x, y = mouse_pos
    height = (size * (3 ** 0.5)) / 2
    points = [(x, y), (x + size, y), (x + size / 2, y - height)]
    pygame.draw.polygon(canvas, color, points, 3)

def draw_rhombus(canvas, mouse_pos, size, color):
    x, y = mouse_pos
    points = [(x, y - size // 2), (x + size // 2, y), (x, y + size // 2), (x - size // 2, y)]
    pygame.draw.polygon(canvas, color, points, 3)

run_paint_app()
