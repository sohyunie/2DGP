import random
from pico2d import *
import os
os.chdir('d:/SoHyun/문서/2DGP/수업내용/3주차')

RES_DIR = '../res'

# 동작의 추상화 - 함수 만들기, 클래스 생성 -> 코드 중복 방지 가능
def handle_events():
	global running
	evts = get_events()
	for e in evts:
		if e.type == SDL_QUIT:
			running = False
		elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
			running = False

open_canvas()

# gra = load_image(RES_DIR + '/grass.png')
# cha2 = load_image(RES_DIR + '/character.png')

class Grass:
	def __init__(self):
		self.image = load_image(RES_DIR + '/grass.png')
	def draw(self):
		self.image.draw(400, 30)
	# update는 필요없지만 함수를 만들어두는 게 필요할 수 있다. 
	def update(self):
		pass

class Boy:
	#constructor 생성자, 객체가 생성되면 반드시 불리는 부분
	def __init__(self):
		self.x = random.randint(100, 100)
		self.y = random.randint(100, 100)
		self.dx, self.dy = random.random(), random.random() # 0.0 ~ 1.0 사이의 float return
		self.fidx = random.randint(0, 7)
		self.image = load_image(RES_DIR + '/run_animation.png')
	def draw(self):
		self.image.clip_draw(self.fidx * 100, 0, 100, 100, self.x, self.y)
	def update(self):
		self.x += self.dx
		self.y += self.dy
		self.fidx = (self.fidx + 1) % 8

grass = Grass()
# boy = Boy((0, 85), (2, 0.1)) # 객체 생성, instantiation
# boy = Boy()
# boy2 = Boy((0, 200), (1, 0.05))
team = [ Boy() for i in range(11) ]
# for boy in team:
#	boy.x = random.randint(100, 700)
#	boy.y = random.randint(100, 500)

running = True
while running:
	clear_canvas()
	grass.draw()
	for boy in team:
		boy.draw()
	update_canvas()

	handle_events()
	for boy in team:
		boy.update()
	# boy2.update()
	grass.update()

	delay (0.03)

close_canvas()