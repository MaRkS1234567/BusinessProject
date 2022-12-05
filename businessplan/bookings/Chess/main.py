import pygame as pg

pg.init()
clock  = pg.time.Clock()
FPS = 10
window_size = (700, 700)
background = (150, 90, 30)
screen = pg.display.set_mode(window_size)
run = True
screen.fill(background) #color background

white = (255, 255, 255)
black = (0, 0, 0)
grey = (180, 180, 180)
yellow  =(255, 255, 0)
colors = [black, grey]
cell_qty = 8
cell_size = 80

is_even_qty = (cell_qty % 2 == 0)
cell_color_index = 1 if (is_even_qty) else 0

for y in range(cell_qty):
    for x in range(cell_qty):
        pg.draw.rect(screen, colors[cell_color_index] ,(x*cell_size, y*cell_size, cell_size, cell_size))
        cell_color_index ^= True #binary XOR
    cell_color_index = cell_color_index^True if (is_even_qty) else cell_color_index

pg.display.update()

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    # pg.display.update()
    clock.tick(FPS)
