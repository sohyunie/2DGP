import random
from pico2d import *
# module은 마치 singleton 객체인 것처럼 동작한다. 

RES_DIR = '../res'

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