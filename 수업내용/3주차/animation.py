from pico2d import *
import os
os.chdir('C:\\Users\\SoHyun\\AppData\\Local\\Programs\\Python\\Python38\\2DGP\\res')
os.listdir()

open_canvas()
grass=load_image('grass.png')
character=load_image('run_animation.png')

x = 0
frame = 0
while(x < 800):
	clear_canvas()
	grass.draw(400, 30)
	#clip_draw (left, bottom, width, height, x, y)
	character.clip_draw(frame*100, 0, 100, 100, x, 90)
	update_canvas()
	frame=(frame+1)%8
	x+=5
	delay(0.05)
	get_events()

close_canvas()