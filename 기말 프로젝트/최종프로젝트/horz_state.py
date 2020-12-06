import random
import gfw
from pico2d import *
import gobj
from player import Player
from background import HorzScrollBackground
from platform import Platform
from jelly import Jelly
from heart import Heart
import pickle
import stage_gen
from button import Button
import gameover_state


canvas_width = 1120
canvas_height = 630
score = 0
heart = 10
def start(theme):
    gameover_state.theme = theme
    gfw.push(gameover_state)

def enter():
    gfw.world.init(['bg', 'platform', 'enemy', 'item', 'player', 'ui'])

    center = get_canvas_width() // 2, get_canvas_height() // 2

    # GameController
    for n, speed in [(1,10), (2,100), (3,150)]:
        bg = HorzScrollBackground('cookie_run_bg_%d.png' % n)
        bg.speed = speed
        gfw.world.add(gfw.layer.bg, bg)

    global player
    player = Player()
    player.bg = bg
    gfw.world.add(gfw.layer.player, player)

    score = 0
    heart = 10

    stage_gen.load(gobj.res('stage_01.txt'))

paused = False
def update():
    if paused:
        return
    gfw.world.update()

    dx = -300 * gfw.delta_time

    for layer in range(gfw.layer.platform, gfw.layer.item + 1):
        for obj in gfw.world.objects_at(layer):
            obj.move(dx)

    check_items()
    check_obstacles()

    stage_gen.update(dx)

def check_items():
    global score
    for item in gfw.world.objects_at(gfw.layer.item):
        if gobj.collides_box(player, item):
            score += 10
            print(score)
            gfw.world.remove(item)
            break

def check_obstacles():
    global heart
    for enemy in gfw.world.objects_at(gfw.layer.enemy):
        if enemy.hit: continue
        if gobj.collides_box(player, enemy):
            heart -= 1
            print(heart)
            print('Hit', enemy)
            enemy.hit = True
    if heart <= 0:
        paused = True
        gfw.pop()
        print("heart is 0")
        start("gameover_state")

def draw():
    gfw.world.draw()
    # UI
    global score
    font = gfw.font.load(gobj.res('ENCR10B.TTF'), 30)
    font.draw(900, 540, 'Score: %.lf' % score)
    for i in range(heart):
        heartObj = Heart(1095 - (i * 50), 605)
        heartObj.draw()

    #with open('res/ScoreFile.txt', 'w') as f:
    #    f.write(score+"\n")
    #f.close()
def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
        return
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
            return
        elif e.key == SDLK_a:
            # player.pos = 150,650
            # for x, y in [(100,400),(400,300),(650,250),(900,200)]:
            for i in range(10):
                x = random.randint(100, 900)
                y = random.randint(200, 400)
                pf = Platform(Platform.T_3x1, x, y)
                gfw.world.add(gfw.layer.platform, pf)
        elif e.key == SDLK_p:
            global paused
            paused = not paused
    #if handle_mouse(e):
    #    return
    if player.handle_event(e):
        return

capture = None 
def handle_mouse(e):
    global capture
    if capture is not None:
        holding = capture.handle_event(e)
        if not holding:
            capture = None
        return True

    for obj in gfw.world.objects_at(gfw.layer.ui):
        if obj.handle_event(e):
            capture = obj
            return True

    return False

def pause():
    pass

def resume():
    build_world()

def exit():
    pass



if __name__ == '__main__':
    gfw.run_main()
