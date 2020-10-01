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

gra = load_image(RES_DIR + '/grass.png')
# cha2 = load_image(RES_DIR + '/character.png')

class Grass:
	def __init__(self):
		self.image = load_image(RES_DIR + '/grass.png')
	def draw(self):
		self.image.draw(400, 30)
class Boy:
	#constructor 생성자, 객체가 생성되면 반드시 불리는 부분
	def __init__(self, pos, delta):
		self.x, self.y = pos
		self.dx, self.dy = delta
		self.fidx = 0 
		self.image = load_image(RES_DIR + '/run_animation.png')
	def draw(self):
		self.image.clip_draw(self.fidx * 100, 0, 100, 100, self.x, self.y)
	def update(self):
		self.x += self.dx
		self.y += self.dy
		self.fidx = (self.fidx + 1) % 8

grass = Grass()
boy = Boy((0, 85), (2, 0.1)) # 객체 생성, instantiation
boy2 = Boy((0, 200), (1, 0.05))

running = True
while running:
	# 메인 게임루프는 어떤 오브젝트들이 있는지만 가지고 걔네들을 조율하는 역할
	# 구체적인 것 boy를 어떻게 그려야 하고 어떻게 업데이트 해야하는지는 각각의 class에 맡긴다. 
	# 앞으로 요구사항이 변경되었을 때 수정하기 더 용이해진다. 
	# 다형성 - 일 시키는 사람은 구체적으로 어떤 일이 실행되는지 모른다. 시키는 사람은 모르고 시킨다. 
	clear_canvas()
	grass.draw()
	boy.draw()
	boy2.draw()
	update_canvas()

	handle_events()

	boy.update()
	boy2.update()

	if boy.x > get_canvas_width():
		running = False

	delay (0.01)

# delay(2) # in seconds
# frame animation
close_canvas()

# game loop:
#	- update() - logic
#	- draw() - render

# game loop:
#	- update() - logic
# 	- event handling
#	- draw() - render