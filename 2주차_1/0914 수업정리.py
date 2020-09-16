 from pico2d import *
 import os

 os.getcwd()
 os.chdir('e:\\jieun\\2dgame')
 os.listdir()

 open_canvas()

 ch = load_image('character.png')

 ch.draw_now(200,400)
 ch.draw_now(400,100)

 for x in range(0,9):
	for y in range(0,7):
		ch.draw_now(x*100,y*100)

		
 clear_canvas_now()
 
