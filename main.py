import renderer
import keyboard
from time import perf_counter as time_now
from time import sleep

r = renderer.Renderer(100, 35, 60)
r.initScreen()

quit = False

#TODO: move timing and screen rendering to gfx.py
then = time_now()
now = time_now()
elapsed = now-then

while not quit:
    then = time_now()

    #clear screen
    r.clearScreen()

    #poll keyboard
    keyList = []
    for k in ("W","A","S","D"):
        if keyboard.isPressed(keyboard.key[k]):
            keyList.append(k)
    
    #handle game loop
    r.writeScreen(str(1/elapsed)[:2])
    r.writeScreen(" ".join(keyList),100)

    #print screen
    r.paintScreen()
    now = time_now()
    elapsed = now-then
    if r.minRenderTime > elapsed: #if we rendered too fast (hah) limit to renderer fps by sleeping the difference
         sleep(r.minRenderTime-elapsed)
