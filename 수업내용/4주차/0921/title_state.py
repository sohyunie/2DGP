import gfw
from pico2d import *
import game_state
import os
os.chdir('d:/SoHyun/문서/2DGP/수업내용/4주차/0921')

# 프로그램마다 달라지는 부분을 이곳에 쓸 것이다.

def enter():
    global image
    image = load_image('res/title.png')

def update():
    pass

def draw():
    image.draw(400, 300)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(game_state)

def exit():
    global image
    del image

if __name__=='__main__':
    gfw.run_main()