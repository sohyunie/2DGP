from pico2d import *
import gfw
import gobj
from button import Button
import horz_state
import pickle
import highscore

canvas_width = 1120
canvas_height = 630

def passDef():
    pass

def build_world():
    bg_music.set_volume(10)
    bg_music.repeat_play()

    gfw.world.init(['bg', 'ui'])

    center = (canvas_width//2, canvas_height//2)
    bg = gobj.ImageObject('lobbyBG.png', center)
    gfw.world.add(gfw.layer.bg, bg)

    global font
    font = gfw.font.load(gobj.res('ENCR10B.TTF'), 40)
    l,b,w,h = 670,450,get_canvas_width()/3,80
    btn = Button(l,b,w,h,font,"Play game", lambda: start("horz_state"))
    gfw.world.add(gfw.layer.ui, btn)

def start(theme):
    global bg_music
    bg_music.stop()
    del bg_music
    gfw.world.remove(highscore)
    horz_state.theme = theme
    gfw.push(horz_state)

def enter():
    global bg_music
    bg_music = load_wav(gobj.res('sound/LobbyMusic.wav'))
    build_world()
    highscore.load()
    gfw.world.add(gfw.layer.ui, highscore)

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()
    #f = open('res/ScoreFile.txt', 'r') 
    #memo = f.read()
    #f.close()
    #font = gfw.font.load(gobj.res('ENCR10B.TTF'), 20)
    #font.draw(670, 350, 'Score List \n%s' % memo)

    
def handle_event(e):
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.pop()

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
    pass

if __name__ == '__main__':
    gfw.run_main()
