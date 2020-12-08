from pico2d import *
import gfw
import gobj
from button import Button
import menu_state
import horz_state
import highscore

canvas_width = 1120
canvas_height = 630

def start(theme):
    horz_state.theme = theme
    #horz_state.enter()
    gfw.push(horz_state)

def menuStart(theme):
    highscore.add(str(horz_state.score))
    menu_state.theme = theme
    gfw.push(menu_state)

def build_world():
    gfw.world.init(['bg', 'ui'])

    center = (canvas_width//2, canvas_height//2)
    bg = gobj.ImageObject('gameover.png', center)
    gfw.world.add(gfw.layer.bg, bg)

    font = gfw.font.load(gobj.res('ENCR10B.TTF'), 40)
    l,b,w,h = 600,450,get_canvas_width()/3 + 90,80
    btn = Button(l,b,w,h,font,"retry game", lambda: gfw.pop())
    gfw.world.add(gfw.layer.ui, btn)

    value = 'save score : %.lf' %horz_state.score
    l,b,w,h = 600,250,get_canvas_width()/3 + 90,80
    btn = Button(l,b,w,h,font, value, lambda: menuStart("menu_state"))
    gfw.world.add(gfw.layer.ui, btn)

def enter():
    build_world()
    highscore.load()

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()
    
def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.pop()

    # print('ms.he()', e.type, e)
    if handle_mouse(e):
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

def exit():
    print("menu_state exits")
    pass

def pause():
    pass

def resume():
    build_world()

if __name__ == '__main__':
    gfw.run_main()
