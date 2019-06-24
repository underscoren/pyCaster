class Graphics:
    
    def __init__(self, renderer):
        self._renderer = renderer
        self._width = renderer._width #copy variables for easy access
        self._height = renderer._height

    def coordsToIndex(self, x, y): #get screenbuffer index from screen coordinates
        return int(y)*self._width+int(x)
    
    def indexToCoords(self, index): #get coordinates from screenbuffer index
        return (index%self._width,index//self._width)

    def writeLine(self, string, x, y): #writes line to screenbuffer via coodrdinates
        #TODO: implement text wrapping on edge of screen
        self._renderer.writeScreen(string, self.coordsToIndex(x,y))