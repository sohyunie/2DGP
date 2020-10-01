from pico2d import *
from gobj import *
import os
os.chdir('d:/SoHyun/문서/2DGP/수업내용/3주차')

# 프로그램마다 달라지는 부분을 이곳에 쓸 것이다.
def enter():
	global grass, team
	grass = Grass()
	team = [ Boy() for i in range(11) ]

def update():
	for b in team: b.update()

def draw():
	grass.draw()
	for b in team: b.draw()

# extract to function
def handle_event(e):
	global running
	if e.type== SDL_QUIT:
		running= False
	elif(e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
		running False

open_canvas() 

enter()

running = True

# 여기는 안 바뀔 부분
while running:
	# event handling
	evts = get_events()
	for e in evts: handle_event(e)

	# game logic
	update() 

	# game rendering
	clear_canvas()
	draw()
	update_canvas()

	delay (0.01)

close_canvas()