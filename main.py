import pygame
import math
import random

WIDTH, HEIGHT = 1080, 720
BG = (0, 0, 0)
GRAY = (128, 128, 128)
SCALE = 180
PERSPECTIVE = 4
ANGLE_STEP = 0.0001


def rotate_xw(x, w, angle):
    x_new = x * math.cos(angle) - w * math.sin(angle)
    w_new = x * math.sin(angle) + w * math.cos(angle)
    return x_new, w_new

def rotate_yw(y, w, angle):
    y_new = y * math.cos(angle) - w * math.sin(angle)
    w_new = y * math.sin(angle) + w * math.cos(angle)
    return y_new, w_new

def rotate_zw(z, w, angle):
    z_new = z * math.cos(angle) - w * math.sin(angle)
    w_new = z * math.sin(angle) + w * math.cos(angle)
    return z_new, w_new

def rotate_xy(x, y, angle):
    x_new = x * math.cos(angle) - y * math.sin(angle)
    y_new = x * math.sin(angle) + y * math.cos(angle)
    return x_new, y_new

def rotate_xz(x, z, angle):
    x_new = x * math.cos(angle) - z * math.sin(angle)
    z_new = x * math.sin(angle) + z * math.cos(angle)
    return x_new, z_new

def rotate_yz(y, z, angle):
    y_new = y * math.cos(angle) - z * math.sin(angle)
    z_new = y * math.sin(angle) + z * math.cos(angle)
    return y_new, z_new


def project_4d_to_2d(x, y, z, w):
    distance = PERSPECTIVE / (PERSPECTIVE + w)
    x = x * distance * SCALE + WIDTH // 2
    y = y * distance * SCALE + HEIGHT // 2
    return x, y


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tesseract Rotation Control")

vertices = [(-1, -1, -1, -1),
            ( 1, -1, -1, -1),
            ( 1,  1, -1, -1),
            (-1,  1, -1, -1),
            (-1, -1,  1, -1),
            ( 1, -1,  1, -1),
            ( 1,  1,  1, -1),
            (-1,  1,  1, -1),
            (-1, -1, -1,  1),
            ( 1, -1, -1,  1),
            ( 1,  1, -1,  1),
            (-1,  1, -1,  1),
            (-1, -1,  1,  1),
            ( 1, -1,  1,  1),
            ( 1,  1,  1,  1),
            (-1,  1,  1,  1)]

edges = [(0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7),
        (8, 9), (9, 10), (10, 11), (11, 8),
        (12, 13), (13, 14), (14, 15), (15, 12),
        (8, 12), (9, 13), (10, 14), (11, 15),
        (0, 8), (1, 9), (2, 10), (3, 11),
        (4, 12), (5, 13), (6, 14), (7, 15)]

vertex_colors = [(random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)) for _ in range(len(vertices))]

angles = {
    'xw': 0.0,
    'yw': 0.0,
    'zw': 0.0,
    'xy': 0.0,
    'xz': 0.0,
    'yz': 0.0}

keys_pressed = {
    pygame.K_q: False,  
    pygame.K_w: False,  
    pygame.K_e: False,  
    pygame.K_r: False,  
    pygame.K_t: False, 
    pygame.K_y: False,  
    pygame.K_a: False,  
    pygame.K_s: False,  
    pygame.K_d: False, 
    pygame.K_f: False,  
    pygame.K_g: False, 
    pygame.K_h: False}

font = pygame.font.Font(None, 24)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in keys_pressed:
                keys_pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            if event.key in keys_pressed:
                keys_pressed[event.key] = False

    screen.fill(BG)

    if keys_pressed[pygame.K_q]:
        angles['xw'] -= ANGLE_STEP
    if keys_pressed[pygame.K_w]:
        angles['xw'] += ANGLE_STEP
    if keys_pressed[pygame.K_e]:
        angles['yw'] -= ANGLE_STEP
    if keys_pressed[pygame.K_r]:
        angles['yw'] += ANGLE_STEP
    if keys_pressed[pygame.K_t]:
        angles['zw'] -= ANGLE_STEP
    if keys_pressed[pygame.K_y]:
        angles['zw'] += ANGLE_STEP
    if keys_pressed[pygame.K_a]:
        angles['xy'] -= ANGLE_STEP
    if keys_pressed[pygame.K_s]:
        angles['xy'] += ANGLE_STEP
    if keys_pressed[pygame.K_d]:
        angles['xz'] -= ANGLE_STEP
    if keys_pressed[pygame.K_f]:
        angles['xz'] += ANGLE_STEP
    if keys_pressed[pygame.K_g]:
        angles['yz'] -= ANGLE_STEP
    if keys_pressed[pygame.K_h]:
        angles['yz'] += ANGLE_STEP
    rotated_vertices = []

    for x, y, z, w in vertices:
        x, w = rotate_xw(x, w, angles['xw'])
        y, w = rotate_yw(y, w, angles['yw'])
        z, w = rotate_zw(z, w, angles['zw'])
        x, y = rotate_xy(x, y, angles['xy'])
        x, z = rotate_xz(x, z, angles['xz'])
        y, z = rotate_yz(y, z, angles['yz'])

        rotated_vertices.append((x, y, z, w))

    projected_vertices = []
    for x, y, z, w in rotated_vertices:
        x_proj, y_proj = project_4d_to_2d(x, y, z, w)
        projected_vertices.append((x_proj, y_proj))


    for i, edge in enumerate(edges):
        x1_proj, y1_proj = projected_vertices[edge[0]]
        x2_proj, y2_proj = projected_vertices[edge[1]]
        color1 = vertex_colors[edge[0]]
        color2 = vertex_colors[edge[1]]
        edge_color = ((color1[0] + color2[0]) // 2,
                        (color1[1] + color2[1]) // 2,
                        (color1[2] + color2[2]) // 2)

        pygame.draw.line(screen, edge_color, (x1_proj, y1_proj), (x2_proj, y2_proj), 2)

    text_color = GRAY
    text_xw = font.render(f"xw Angle: {angles['xw']:.2f}", True, text_color)
    text_yw = font.render(f"yw Angle: {angles['yw']:.2f}", True, text_color)
    text_zw = font.render(f"zw Angle: {angles['zw']:.2f}", True, text_color)
    text_xy = font.render(f"xy Angle: {angles['xy']:.2f}", True, text_color)
    text_xz = font.render(f"xz Angle: {angles['xz']:.2f}", True, text_color)
    text_yz = font.render(f"yz Angle: {angles['yz']:.2f}", True, text_color)

    screen.blit(text_xw, (10, 10))
    screen.blit(text_yw, (10, 30))
    screen.blit(text_zw, (10, 50))
    screen.blit(text_xy, (10, 70))
    screen.blit(text_xz, (10, 90))
    screen.blit(text_yz, (10, 110))

    pygame.display.flip()

pygame.quit()