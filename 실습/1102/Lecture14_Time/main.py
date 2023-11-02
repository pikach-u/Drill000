from pico2d import open_canvas, delay, close_canvas
import game_framework

import play_mode as start_mode

open_canvas(1600, 600, sync=True) # 그래픽카드가 제공하는 기본 싱크율로 맞춰준다
game_framework.run(start_mode)
close_canvas()

