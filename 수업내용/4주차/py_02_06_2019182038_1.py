import os
import math
os.chdir('d:/SoHyun/문서/2DGP/수업내용/4주차')
import helper
from pico2d import *
RES_DIR='../res'



open_canvas()

class Grass:
	def __init__(self):
		self.image=load_image(RES_DIR+'/grass.png')
	def draw(self): 
		self.image.draw(400,30)
	def update(self):
		pass

class Boy:
	def __init__(self):
		self.x, self.y = 400, 85
		self.dx, self.dy=0,0
		self.fidx=0
		self.image=load_image(RES_DIR+'/run_animation.png')
		self.towardx = 0
		self.towardy = 0 
	def draw(self): 
		self.image.clip_draw(self.fidx*100,0,100,100,self.x, self.y)
	def update(self):
		self.x+=self.dx
		self.y+=self.dy
		self.fidx=(self.fidx+1)%8
	def check(self):
		if self.check==True:
			self.dx, self.dy=0,0

boy=Boy()


			

grass=Grass()



deltax=0
deltay=0
towardx=0
towardy=0
def handle_events():
	global running	
	global boy
	global arrive
	events=get_events()
	for event in events:
		if event.type == SDL_QUIT:
			running = False
		elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
			running=False
		elif event.type == SDL_MOUSEBUTTONDOWN:
			boy.towardx = event.x
			boy.towardy = get_canvas_height()-event.y-1
			boy.dx, boy.dy=helper.delta((boy.x,boy.y), (boy.towardx, boy.towardy), 5)
			(deltax, deltay) = helper.delta((boy.x, boy.y), (towardx,towardy), 5)





running = True
while running:
	clear_canvas()
	grass.draw()
	boy.draw()
	update_canvas()

	handle_events()
	(posx, posy), done = helper.move_toward((boy.x, boy.y), (boy.dx, boy.dy), (boy.towardx, boy.towardy))
	if done==True:
		boy.x, boy.y=posx,posy

	boy.update()
	grass.update()

	if boy.x>get_canvas_width():
		running=False

	delay(0.01)

close_canvas()