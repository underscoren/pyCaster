from platform import system
if not system() == "Windows":
    raise Exception("This will only work on windows due to the keyboard handling method")

import renderer
import keyboard
import clock
import graphics
from time import perf_counter
import math

FPS = 60
SCREEN_WIDTH = 120
SCREEN_HEIGHT = 40


c = clock.Clock(FPS)
r = renderer.Renderer(SCREEN_WIDTH, SCREEN_HEIGHT, FPS)
gfx = graphics.Graphics(r)
r.initScreen()

quit = False

then = perf_counter()
now = perf_counter()

playerX = 8
playerY = 8
playerA = 0

speed = 2
turnSpeed = 1.5

mapHeight = 16
mapWidth = 16

FOV = math.pi/3.5
depth = 16

map_tiles  = "################"
map_tiles += "#..............#"
map_tiles += "#..............#"
map_tiles += "#.........#....#"
map_tiles += "#.........#....#"
map_tiles += "#..............#"
map_tiles += "#..............#"
map_tiles += "#..............#"
map_tiles += "#..............#"
map_tiles += "#..............#"
map_tiles += "#..............#"
map_tiles += "#..............#"
map_tiles += "#........#######"
map_tiles += "#..............#"
map_tiles += "#..............#"
map_tiles += "################"

while not quit:
    then = perf_counter()
    elapsed = then-now
    now = then

    #clear screen
    r.clearScreen()

    #handle input
    if keyboard.getState(keyboard.key["W"]):
        playerX += math.sin(playerA) * speed * elapsed
        playerY += math.cos(playerA) * speed * elapsed
        if map_tiles[int(playerX) * mapWidth + int(playerY)] == "#":
            playerX -= math.sin(playerA) * speed * elapsed
            playerY -= math.cos(playerA) * speed * elapsed
    
    if keyboard.getState(keyboard.key["S"]):
        playerX -= math.sin(playerA) * speed * elapsed
        playerY -= math.cos(playerA) * speed * elapsed
        if map_tiles[int(playerX) * mapWidth + int(playerY)] == "#":
            playerX += math.sin(playerA) * speed * elapsed
            playerY += math.cos(playerA) * speed * elapsed
    
    if keyboard.getState(keyboard.key["A"]):
        playerA -= turnSpeed*0.75 * elapsed
    
    if keyboard.getState(keyboard.key["D"]):
        playerA += turnSpeed*0.75 * elapsed

    #game loop
    if keyboard.isPressed(keyboard.key["Q"]):
        quit=True
    
    for x in range(SCREEN_WIDTH): #iterate over every column on screen
        rayAngle = (playerA - FOV / 2.0) +  (x / SCREEN_WIDTH)*FOV

        distanceToWall = 0

        eyeX = math.sin(rayAngle)
        eyeY = math.cos(rayAngle)

        hitWall = False
        while not hitWall and distanceToWall < depth: #cast the ray out into the world
            distanceToWall += 0.1

            testX = int(playerX + eyeX * distanceToWall)
            testY = int(playerY + eyeY * distanceToWall)

            if testX < 0 or testX >= mapWidth or testY < 0 or testY >= mapHeight: #if you go out ot bounds, assume max depth
                hitWall = True
                distanceToWall = depth
            else:
                if map_tiles[testY * mapWidth + testX] == "#": #if you hit a wall, distanceToWall will have the distance saved
                    hitWall = True
        
        ceiling = SCREEN_HEIGHT / 2 - SCREEN_HEIGHT / distanceToWall
        floor = SCREEN_HEIGHT - ceiling

        shade = " " #pixel colour

        if distanceToWall <= depth/4:   shade = "█"
        elif distanceToWall < depth/3:  shade = "▓"
        elif distanceToWall < depth/2:  shade = "▓"
        elif distanceToWall < depth:    shade = "░"
        else:                           shade = " "

        for y in range(SCREEN_HEIGHT): #iterate over every row in the column
            if y < ceiling: #ceiling is blank
                gfx.writeLine(" ",x,y)
            elif y > ceiling and y <= floor:
                gfx.writeLine(shade,x,y) #wall shading calculated earlier
            else: #if we are floor, calculate different shade based on distance from bottom of screen
                b = 1 - (y - SCREEN_HEIGHT/2) / (SCREEN_HEIGHT/2)
                if b < 0.25:    shade = "#"
                elif b < 0.5:   shade = "x"
                elif b < 0.75:  shade = "."
                elif b < 0.9:   shade = "-"
                else:           shade = " "
                gfx.writeLine(shade,x,y)

    gfx.writeLine("{:.1f}fps X:{:.1f} Y:{:.1f} A:{:.1f}".format(1/elapsed, playerX, playerY, playerA), 0,0) #print stats

    #print screen
    r.paintScreen()
    
    #automatically sleep if we executed faster than 1/fps
    

    #time how long it took for the frame
    elapsed = perf_counter()-then
