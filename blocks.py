from browser import document, alert, html, timer
from random import randint

boarder_size = 3
w = 10 + boarder_size*2
h = 20 + boarder_size*2
block_size = 20
BOARDER = 15

def paint_block(canvas_name, x, y, n):
    if canvas_name == "grid":
        height = h
        blank = "LightGray"
    else:
        height = 3
        blank = "White"
    if n == 8:
        fill_style = "Red"
    elif n == 9:
        fill_style = "Blue"
    elif n == 10:
        fill_style = "Orange"
    elif n == 11:
        fill_style = "Yellow"
    elif n == 12:
        fill_style = "Magenta"
    elif n == 13:
        fill_style = "Cyan"
    elif n == 14:
        fill_style = "Green"
    elif n == BOARDER:
        fill_style = "Black"
    else:
        fill_style = blank
    canvas=document[canvas_name].getContext("2d")
    canvas.beginPath()
    canvas.rect(x*block_size, (height-y)*block_size, block_size, block_size)
    canvas.fillStyle = fill_style 
    canvas.fill()

class PlayingGrid():
    def __init__(self):
        # This looks the wrong way around but it create an x,y array
        self.grid = [[0 for y in range(h)] for x in range(w)]
        for x in range(0, boarder_size):
            for y in range(0,h):
                self.grid[x][y] = BOARDER
        for x in range(w-boarder_size, w):
            for y in range(0,h):
                self.grid[x][y] = BOARDER
        for x in range(0, w):
            for y in range(0,boarder_size):
                self.grid[x][y] = BOARDER
    def draw_grid(self):
        for x in range(boarder_size,w-boarder_size):
            for y in range(boarder_size,h):
                paint_block("grid", x, y, 
                            self.grid[x][y])
    def draw_boarder(self):
        for x in range(0, boarder_size):
            for y in range(0,h):
                paint_block("grid", x, y, 
                            BOARDER)
        for x in range(w-boarder_size, w):
            for y in range(0,h):
                paint_block("grid", x, y, 
                            BOARDER)
        for x in range(0, w):
            for y in range(0,boarder_size):
                paint_block("grid", x, y, 
                            BOARDER)
        for x in range(0, w):
            for y in range(h-boarder_size, h):
                paint_block("grid", x, y, 
                            BOARDER)


class Block():
    def __init__(self):
        self.style = 0
        self.total_styles = 7
        self.rotation = 0
        # Select a sytle by random, no rotation
        self.style = randint(0,self.total_styles-1)
        # Prep grid for rotating blocks
        self.grid = [[0 for x in range(4)] for y in range(4)]
        self.sytle_grid()
        self.x = 0
        self.y = 0
    def sytle_grid(self):
        # Rotation is counter-intuitive
        # if rotate "true", its skips left to right
        #    So we precalculate the rotations so make them better
        #Debug
        document["details"].text = str(self.style) + " " + str(self.rotation)
        #I
        if self.style == 0 and \
          (self.rotation == 0 or self.rotation == 2):
            self.grid = [[ 0,  0,  0,  0], 
                         [ 0,  0,  0,  0], 
                         [ 8,  8,  8,  8], 
                         [ 0,  0,  0,  0]]
        if self.style == 0 and \
          (self.rotation == 1 or self.rotation == 3):
            self.grid = [[ 0,  8,  0,  0], 
                         [ 0,  8,  0,  0], 
                         [ 0,  8,  0,  0], 
                         [ 0,  8,  0,  0]]
        # O
        if self.style == 1:
            self.grid = [[ 0,  0,  0,  0], 
                         [ 0,  9,  9,  0], 
                         [ 0,  9,  9,  0], 
                         [ 0,  0,  0,  0]]
        #S
        if self.style == 2 and \
          (self.rotation == 0 or self.rotation == 2):
            self.grid = [[ 0,  0,  0,  0], 
                         [ 0,  0, 10, 10], 
                         [ 0, 10, 10,  0], 
                         [ 0,  0,  0,  0]]
        if self.style == 2 and \
          (self.rotation == 1 or self.rotation == 3):
            self.grid = [[ 0,  0,  0,  0], 
                         [ 0, 10,  0,  0], 
                         [ 0, 10, 10,  0], 
                         [ 0,  0, 10,  0]]
        #Z
        if self.style == 3 and \
          (self.rotation == 0 or self.rotation == 2):
            self.grid = [[ 0,  0,  0,  0], 
                         [ 0,  0,  0,  0], 
                         [ 0, 11, 11,  0], 
                         [ 0,  0, 11, 11]]
        if self.style == 3 and \
          (self.rotation == 1 or self.rotation == 3):
            self.grid = [[ 0,  0,  0,  0], 
                         [ 0,  0, 11,  0], 
                         [ 0, 11, 11,  0], 
                         [ 0, 11,  0,  0]]
        if self.style == 4 and self.rotation == 0:
            self.grid = [[ 0,  0,  0,  0], 
                         [ 0, 12,  0,  0], 
                         [12, 12, 12,  0], 
                         [ 0,  0,  0,  0]]
        if self.style == 4 and self.rotation == 1:
            self.grid = [[ 0,  0,  0,  0], 
                         [ 0, 12,  0,  0], 
                         [12, 12,  0,  0], 
                         [ 0, 12,  0,  0]]
        if self.style == 4 and self.rotation == 2:
            self.grid = [[ 0,  0,  0,  0], 
                         [ 0,  0,  0,  0], 
                         [12, 12, 12,  0], 
                         [ 0, 12,  0,  0]]
        if self.style == 4 and self.rotation == 3:
            self.grid = [[ 0,  0,  0,  0], 
                         [ 0, 12,  0,  0], 
                         [ 0, 12, 12,  0], 
                         [ 0, 12,  0,  0]]
        # L
        if self.style == 5 and self.rotation == 0:
            self.grid = [[ 0,  0,  0,  0], 
                         [ 0,  0, 13,  0], 
                         [13, 13, 13,  0], 
                         [ 0,  0,  0,  0]]
        if self.style == 5 and self.rotation == 1:
            self.grid = [[ 0,  0,  0,  0], 
                         [13, 13,  0,  0], 
                         [ 0, 13,  0,  0], 
                         [ 0, 13,  0,  0]]
        if self.style == 5 and self.rotation == 2:
            self.grid = [[ 0,  0,  0,  0], 
                         [ 0,  0,  0,  0], 
                         [13, 13, 13,  0], 
                         [13,  0,  0,  0]]
        if self.style == 5 and self.rotation == 3:
            self.grid = [[ 0,  0,  0,  0], 
                         [ 0, 13,  0,  0], 
                         [ 0, 13,  0,  0], 
                         [ 0, 13, 13,  0]]
        if self.style == 6 and self.rotation == 0:
            self.grid = [[ 0,  0,  0,  0], 
                         [14,  0,  0,  0], 
                         [14, 14, 14,  0], 
                         [ 0,  0,  0,  0]]
        if self.style == 6 and self.rotation == 1:
            self.grid = [[ 0,  0,  0,  0], 
                         [ 0, 14,  0,  0], 
                         [ 0, 14,  0,  0], 
                         [14, 14,  0,  0]]
        if self.style == 6 and self.rotation == 2:
            self.grid = [[ 0,  0,  0,  0], 
                         [ 0,  0,  0,  0], 
                         [14, 14, 14,  0], 
                         [ 0,  0, 14,  0]]
        if self.style == 6 and self.rotation == 3:
            self.grid = [[ 0,  0,  0,  0], 
                         [ 0, 14, 14,  0], 
                         [ 0, 14,  0,  0], 
                         [ 0, 14,  0,  0]]
    def rotate_anticlock(self):
        self.rotation = self.rotation -1
        if self.rotation == -1:
            self.rotation = 3
        self.sytle_grid()
    def rotate_clock(self):
        self.rotation = self.rotation +1
        if self.rotation == 4:
            self.rotation = 0
        self.sytle_grid()
    def paint(self, canvas_name):
        for x in range(0,4):
            for y in range(0,4):
                paint_block(canvas_name, x+self.x, y+self.y, 
                            self.grid[x][3-y])

def redraw():
    play_grid.draw_grid()
    current_block.paint("grid")
    play_grid.draw_boarder()


def clash_blocks():
    clash = False
    for x in range(0,4):
        for y in range(0,4):
            b = current_block.grid[x][y] + play_grid.grid[x+current_block.x][(3-y)+current_block.y]
            if b>16:
                clash = True
    return clash
                
def freeze_current_block():
    print("Freeze!")
    for x in range(0,4):
        for y in range(0,4):
            if current_block.grid[x][3-y] > 0:
                play_grid.grid[x+current_block.x][y+current_block.y] = current_block.grid[x][3-y]


def test_new_position(movement):
    if movement == "left":
        current_block.x = current_block.x -1
    if movement == "right":
        current_block.x = current_block.x +1
    if movement == "down":
        current_block.y = current_block.y -1
    if movement == "rotate_c":
        current_block.rotate_clock()
    if clash_blocks():
        if movement == "left":
            current_block.x = current_block.x +1
            return False
        if movement == "right":
            current_block.x = current_block.x -1
            return False
        if movement == "down":
            current_block.y = current_block.y +1
            return False
        if movement == "rotate_c":
            current_block.rotate_anticlock()
            return False
    else:
        redraw()
        return True

def keyCode(ev):
    trace = document["traceKeyCode"]
    trace.text = f'event {ev.type}, keyCode : {ev.keyCode}'
    ev.stopPropagation()
    # Key codes for Up, Down, Left, Right, wasd
    if ev.keyCode == 37 or ev.keyCode == 65:
        test_new_position("left")
    if ev.keyCode == 39 or ev.keyCode == 68:
        test_new_position("right")
    if ev.keyCode == 38 or ev.keyCode == 87:
        test_new_position("rotate_c")

def tick():
    global current_block, next_block
#    next_block.rotate_clock()
#    next_block.sytle_grid()
#    next_block.paint("next")
    
    print(current_block.x, current_block.y)
    if not test_new_position("down"):
        freeze_current_block()        
        current_block = next_block
        current_block.x = w/2 - 2
        current_block.y = h - 6
        next_block = Block()
        next_block.paint("next")    
    redraw()

def init():
    element = document["grid"]
    element.width = w*block_size
    element.height = h*block_size
    element = document["next"]
    element.width = block_size*6
    element.height = block_size*4
    if not document["grid"].getContext:
      alert('An error occured creating a Canvas 2D context. '
          'This may be because you are using an old browser')
    play_grid.draw_grid()
    next_block.paint("next")    
    current_block.x = w/2 - 2
    current_block.y = h - 6

play_grid = PlayingGrid()
current_block = Block()
next_block = Block()
document.onkeydown = keyCode
#document["grid"].bind("keydown", keyCode)


init()
timer.set_interval(tick, 2000)
