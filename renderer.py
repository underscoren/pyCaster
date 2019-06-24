from sys import platform as _platform
from sys import stdout as std
from os import system

class Renderer:
    def __init__(self, width, height, fps): #in characters
        self._width = width
        self._height = height
        self._screen = " "*(width*height) #initialise internal screenbuffer
        self.fps = fps

    #automatically set the width and height of the console
    def initScreen(self):
        if _platform.startswith("win"): #win32 or win64
            system("mode con: cols=%s lines=%s" % (self._width, self._height))
            system("cls")
        else: #TODO: automatically set the console size on other OSes
            print("Your os isnt windows... You should set your console to be %s characters wide and %s characters long.")
            input("Press any key to continue...")

    #insert strings directly into the screenbuffer
    def writeScreen(self, string, index=0):
        if index > (self._width * self._height): #if you're writing outside the screenbuffer, dont bother doing anything
            return
        if (len(string) + index) > (self._width * self._height): #if the string is too long, truncate it
            string = string[:(self._width*self._height)-(len(string)+index)]

        self._screen = self._screen[:index] + string + self._screen[index+len(string):]

    #prints the screenbuffer
    def paintScreen(self):
        std.write(self._screen)
        std.flush()

    #clears the screenbuffer
    def clearScreen(self):
        self._screen = " "*(self._width*self._height)
    