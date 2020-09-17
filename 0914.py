from pico2d import *
import os
os.chdir('C:\\Users\\SoHyun\\AppData\\Local\\Programs\\Python\\Python38\\2DGP\\res')
open_canvas()
image=load_image('character.png')
image.draw_now(200,200)
image.draw_now(400,400)
for x in range(0,9):
    for y in range(0,7):
	    image.draw_now(x*100,y*100)
delay(3)

clear_canvas_now()
open_canvas()
grass=load_image('grass.png')
close_canvas()
open_canvas()
grass=load_image('grass.png')
character=load_image('character.png')
grass.draw_now(400,30)
character.draw_now(400,85)
delay(3)

x=0
while(x<800):
	clear_canvas_now()
	grass.draw_now(400,30)
	character.draw_now(x,90)
	x=x+2
	delay(0.01)

close_canvas()
open_canvas()
grass=load_image('grass.png')
character=load_image('character.png')
x=0
while(x<800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x=x+2
    delay (0.01)
close_canvas()

