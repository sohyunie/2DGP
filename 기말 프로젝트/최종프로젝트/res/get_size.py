from pico2d import *
import json

with open('res/out/cookies.json', 'r') as f:
    cookies = json.load(f)

open_canvas()

cookies_2 = []
for cookie in cookies:
    if 'size' in cookie: continue
    try:
        image = load_image('res/out/%s.png' % cookie['id'])
    except IOError:
        continue
    size = (image.w - 2) // 8 - 2
    cookie['size'] = size
    cookies_2.append(cookie)
    print(cookie)

close_canvas()

with open('res/out/cookies_2.json', 'w') as f:
    json.dump(cookies_2, f, indent=2)

