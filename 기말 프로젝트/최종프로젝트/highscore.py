import pickle
from pico2d import *
import time
import gfw

FILENAME = 'data.pickle'
scores = []
MAX_SCORE_COUNT = 5
last_rank = -1

class Entry:
    def __init__(self, score):
        self.score = score
        self.time = time.time()

def load():
    global font, image
    font = gfw.font.load('res/ENCR10B.ttf', 30)

    global scores
    try:
        f = open(FILENAME, "rb")
        scores = pickle.load(f)
        f.close()
        # print("Scores:", scores)
    except:
        print("No highscore file")

def save():
    f = open(FILENAME, "wb")
    pickle.dump(scores, f)
    f.close()

def add(score):
    global scores, last_rank
    entry = Entry(score)
    inserted = False
    for i in range(len(scores)):
        e = scores[i]
        if e.score < entry.score:
            scores.insert(i, entry)
            inserted = True
            last_rank = i + 1
            break
    if not inserted:
        scores.append(entry)
        last_rank = len(scores)

    if (len(scores) > MAX_SCORE_COUNT):
        scores.pop(-1)
    if last_rank <= MAX_SCORE_COUNT:
        save()

def handle_event(e):
    pass

def draw():
    global font
    color = (200, 50, 50)
    y = 370
    font.draw(700, y, 'score list', color)
    y -= 30
    for e in scores:
        str = e.score
        color = (50, 50, 50)
        font.draw(700, y, str, color)
        y -= 30

def update():
    pass
