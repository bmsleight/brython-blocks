from browser import document, alert, html
from random import randint

w = 10
h = 20
block_size = 20

class PlayingGrid():
    def __init__(self):
        # This looks the wrong way around but it create an x,y array
        self.grid = [[0 for x in range(h)] for y in range(w)]
    def fill_style_color(self, n, blank="LightGray"):
        if n == 1:
            return "Red"
        elif n == 2:
            return "Green"
        else:
            return blank
    def fill_style(self, x, y):
        return self.fill_style_color(self.grid[x][y])


    def draw_grid(self):
        canvas=document["grid"].getContext("2d")
        for x in range(0,w):
            for y in range(0,h):
                canvas.beginPath()
                canvas.rect(x*block_size, y*block_size, 
                            block_size, block_size)
                # Canvas is top to bottom
                # I want blocks to be bottom to top
                canvas.fillStyle = self.fill_style(x, h-y-1)
                canvas.fill()

class Block():
    def __init__(self):
        self.style = 0
        self.total_styles = 2
        self.rotation = 0
        self.total_rotates = 1 # Will be 4
        # Select a sytle by random, no rotation
        self.style = randint(0,self.total_styles-1)
        # Prep grid for rotating blocks
        self.grid = [[0 for x in range(4)] for y in range(4)]
        self.sytle_grid()
    def sytle_grid(self):
        if self.style == 0 and self.rotation == 0:
            self.grid = [[0, 0, 0, 0], 
                         [0, 0, 0, 0], 
                         [1, 1, 1, 1], 
                         [0, 0, 0, 0]]
        if self.style == 0 and self.rotation == 1:
            self.grid = [[0, 0, 1, 0], 
                         [0, 0, 1, 0], 
                         [0, 0, 1, 0], 
                         [0, 0, 1, 0]]
        if self.style == 1 and self.rotation == 0:
            self.grid = [[0, 0, 0, 0], 
                         [0, 1, 1, 0], 
                         [0, 1, 1, 0], 
                         [0, 0, 0, 0]]
        if self.style == 1 and self.rotation == 1:
            self.grid = [[0, 0, 0, 0], 
                         [0, 1, 1, 0], 
                         [0, 1, 1, 0], 
                         [0, 0, 0, 0]]
    def block(self, x, y):
        pass                   


def next_peice():
    canvas=document["next"].getContext("2d")
    for x in range(0,4):
        for y in range(0,4):
                canvas.beginPath()
                canvas.rect(x*block_size, y*block_size, 
                            block_size, block_size)
                canvas.fillStyle = play_grid.fill_style_color(next_block.grid[3-x][3-y], blank="White")
                canvas.fill()            


def initial_grid():
    canvas=document["grid"].getContext("2d")
    canvas.beginPath()
    canvas.rect(0, 0, w*block_size, h*block_size)
    canvas.fillStyle = "LightGray"
    canvas.fill()
    canvas=document["next"].getContext("2d")
    canvas.beginPath()
    canvas.rect(0, 0, block_size*4, block_size*4)
    canvas.fillStyle = "Gray"
    canvas.fill()


def init():
    global canvas
    element = document["grid"]
    element.width = w*block_size
    element.height = h*block_size
    element = document["next"]
    element.width = block_size*6
    element.height = block_size*4

    if not document["grid"].getContext:
      alert('An error occured creating a Canvas 2D context. '
          'This may be because you are using an old browser')
    initial_grid()

play_grid = PlayingGrid()
current_block = Block()
next_block = Block()
init()
play_grid.grid[2][0] = 2
play_grid.draw_grid()
next_peice()
