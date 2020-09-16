from pico2d import *

import os
os.getcwd()

os.chdir('e:\\jieun\\2dgame')
os.listdir()
open_canvas()

grass = load_image('grass.png')
ch = load_image('character.png')


ch
grass

ch.draw_now(400,90)
grass.draw_now(400,30)

delay(5)

x = 0
while(x<800):
    clear_canvas_now()
    grass.draw(400, 30)
    character.draw(x, 90)
    x = x + 2
    update_canvas()
    delay(0.01)
    get_events()


close_canvas()
    

