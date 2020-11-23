from pico2d import *
from gobj import *
import os
os.chdir('d:/SoHyun/문서/2DGP/수업내용/3주차')



# extract to function
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

# class로 만든 것을 다른 파일로 빼낼 수 있다. 파이썬에서는 파일 하나를 모듈이라고 부르기도 한다. 


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