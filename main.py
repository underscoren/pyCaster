import renderer
import keyboard
import clock
from time import perf_counter

FPS = 60

c = clock.Clock(FPS)
r = renderer.Renderer(100, 35, FPS)
r.initScreen()

quit = False

then = perf_counter()
elapsed = perf_counter()-then

while not quit:
    then = perf_counter()

    #clear screen
    r.clearScreen()

    #poll keyboard
    keyList = []
    for k in ("W","A","S","D"):
        if keyboard.isPressed(keyboard.key[k]):
            keyList.append(k)
    
    #game loop
    if keyboard.isPressed(keyboard.key["Q"]):
        quit=True
    
    r.writeScreen(str(int(1/elapsed)) + " fps")
    r.writeScreen(" ".join(keyList),100)

    #print screen
    r.paintScreen()
    
    #automatically sleep if we rendered faster than 1/fps
    c.sleep()

    #time how long it took for game loop (not accurate to fps but close enough)
    elapsed = perf_counter()-then
