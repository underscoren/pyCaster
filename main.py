import renderer
import keyboard
import clock
import graphics
from time import perf_counter

FPS = 60
SCREEN_WIDTH = 100
SCREEN_HEIGHT = 35


c = clock.Clock(FPS)
r = renderer.Renderer(SCREEN_WIDTH, SCREEN_HEIGHT, FPS)
gfx = graphics.Graphics(r)
r.initScreen()

quit = False

then = perf_counter()
elapsed = perf_counter()-then

x = 50
y = 17

speed = 25

while not quit:
    then = perf_counter()

    #clear screen
    r.clearScreen()

    #poll keyboard
    if keyboard.getState(keyboard.key["W"]):
        if(y-speed*elapsed>0):
            y -= speed*elapsed
    
    if keyboard.getState(keyboard.key["S"]):
        if(y+speed*elapsed<SCREEN_HEIGHT):
            y += speed*elapsed
    
    if keyboard.getState(keyboard.key["A"]):
        if(x-speed*elapsed>0):
            x -= speed*elapsed
    
    if keyboard.getState(keyboard.key["D"]):
        if(x+speed*elapsed<SCREEN_WIDTH):
            x += speed*elapsed

    #game loop
    if keyboard.isPressed(keyboard.key["Q"]):
        quit=True
    
    gfx.writeLine(str(int(10/elapsed)/10) + "fps  X:"+str(int(x*10)/10) + " Y:"+str(int(y*10)/10), 0,0)
    gfx.writeLine("@",x,y)

    #print screen
    r.paintScreen()
    
    #automatically sleep if we executed faster than 1/fps
    c.sleep()

    #time how long it took for game loop (not 100% accurate to fps but close enough)
    elapsed = perf_counter()-then
