from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0;
y = 0
while (True):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    x = x + 2
    delay(0.01)

    if (x >= 800):
        character.rotate_draw(90)
        character.draw_now(800, y + 90)
        y = y + 2
        delay(0.01)
        character.

close_canvas()
