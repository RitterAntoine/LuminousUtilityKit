import pygame as pg
from random import randint


def life_simulation():
    width_count, height_count = 120, 75
    size = 10
    resolution = width, height = width_count * size + 1, height_count * size + 1
    FPS = 10
    
    screen = pg.display.set_mode(resolution)
    clock = pg.time.Clock()
    
    blocks = [[randint(0, 1) for _ in range(width_count)] for _ in range(height_count)]
    next_blocks_stage = [[0] * width_count for _ in range(height_count)]
    
    
    def paint_block(field, x, y):
        neighbors = sum(field[y + dy][x + dx] for dx in (-1, 0, 1) for dy in (-1, 0, 1)) - field[y][x]
        return 1 if (field[y][x] and neighbors in (2, 3)) or (not field[y][x] and neighbors == 3) else 0
    
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
    
        screen.fill(pg.Color('black'))
    
        for x in range(0, width, size):
            pg.draw.line(screen, (30, 30, 30), (x, 0), (x, height))
        for y in range(0, height, size):
            pg.draw.line(screen, (30, 30, 30), (0, y), (width, y))
    
        for y in range(1, height_count - 1):
            for x in range(1, width_count - 1):
                if blocks[y][x] == 1:
                    pg.draw.rect(screen, (1, 250, 1), (x * size + 2, y * size + 2, size - 2, size - 2))
                next_blocks_stage[y][x] = paint_block(blocks, x, y)
    
        blocks, next_blocks_stage = next_blocks_stage, blocks
    
        pg.display.set_caption(f"FPS: {int(clock.get_fps())}")
        clock.tick(FPS)
        pg.display.flip()
    