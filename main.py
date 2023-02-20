import pygame
import pygame.gfxdraw
import os
import math

pygame.init()

bg_color = (255, 255, 255)
pen_color = (0, 0, 0)
pen_size = 6

screen = pygame.display.set_mode((1080,720), pygame.RESIZABLE)
screen.fill(bg_color)
pygame.display.set_caption("PROG STUDIOS Draw")

clock = pygame.time.Clock()

drawing = False
last_pos = None

def set_pen_color(color):
    global pen_color
    pen_color = color

def set_pen_size(size):
    global pen_size
    pen_size = size

def draw_line(start_pos, end_pos):
    if start_pos == end_pos:
        pygame.gfxdraw.aacircle(screen, start_pos[0], start_pos[1], pen_size, pen_color)
        pygame.gfxdraw.filled_circle(screen, start_pos[0], start_pos[1], pen_size, pen_color)
        return   
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start_pos[0] + float(i) / distance * dx)
        y = int(start_pos[1] + float(i) / distance * dy)
        pygame.gfxdraw.aacircle(screen, x, y, pen_size, pen_color)
        pygame.gfxdraw.filled_circle(screen, x, y, pen_size, pen_color)

def save_image():
    filename = "draw.png"
    pygame.image.save(screen, filename)
    print(f"Image saved as {os.path.abspath(filename)}")

button_font = pygame.font.SysFont('Arial', 18)
button_text = button_font.render("Save as PNG", True, (255,255,255))
button_width, button_height = button_text.get_width() + 10, button_text.get_height() + 10
button_surf = pygame.Surface((button_width, button_height))
button_rect = button_surf.get_rect()
button_rect.bottomright = (screen.get_width() - 10, screen.get_height() - 10)
button_surf.fill((0, 0, 0))
button_surf.blit(button_text, (5, 5))
screen.blit(button_surf, button_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                save_image()
            else:
                drawing = True
                last_pos = event.pos
                draw_line(last_pos, event.pos)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
            last_pos = None
        elif event.type == pygame.MOUSEMOTION and drawing:
            draw_line(last_pos, event.pos)
            last_pos = event.pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                set_pen_color((0, 0, 0))
            elif event.key == pygame.K_r:
                set_pen_color((255, 0, 0))
            elif event.key == pygame.K_g:
                set_pen_color((0, 255, 0))
            elif event.key == pygame.K_b:
                set_pen_color((0, 0, 255))
            elif event.key == pygame.K_1:
                set_pen_size(4)
            elif event.key == pygame.K_2:
                set_pen_size(8)
            elif event.key == pygame.K_c:
                screen.fill(bg_color)
            elif event.key == pygame.K_s:
                save_image()
        elif event.type == pygame.VIDEORESIZE:
            # Get the new window size
            window_size = event.size
            # Create a new surface with the new size
            new_screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
            # Fill the new surface with the background color
            new_screen.fill(bg_color)
            # Copy the contents of the old surface to the new surface
            new_screen.blit(screen, (0, 0))
            # Replace the old surface with the new surface
            screen = new_screen
            pygame.display.set_caption("PROG STUDIOS Draw")

    pygame.display.update()
    clock.tick(60)
