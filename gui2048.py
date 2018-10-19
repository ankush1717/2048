from class2048 import *
from tkinter import *

class Square:
    '''Objects of this class represent a square
    on a tkinter canvas.'''

    def __init__(self, canvas, center, size, color, order, value):
        (x, y) = center
        x1 = x - size / 2
        y1 = y - size/2
        x2 = x + size/2
        y2 = y + size/2
        self.handle = \
        canvas.create_rectangle(x1, y1, x2, y2,
        fill=color, outline=color)
        self.canvas = canvas
        self.center = center
        self.size = size
        self.color = color
        self.order = order
        self.value = value
        canvas.create_text(center, text=value, font="Times 20")

    def setColor(self, color):
        '''Changes this object's color to
        'color'.'''
        self.canvas.itemconfig(self.handle,
        fill=color, outline=color)
        self.color = color

    def move(self, x, y):
        '''Move this square by (x, y).'''
        self.canvas.move(self.handle, x, y)
        (cx, cy) = self.center
        self.center = (cx + x, cy + y)

    def moveTo(self, x, y):
        '''Move this square to the location (x, y)
        on its canvas.'''
        (cx, cy) = self.center
        dx = x - cx
        dy = y - cy
        self.move(dx, dy)

    def changeValue(self, value):
        c.create_text(self.center, text=value, font="Times 20 bold", )
        self.value = value


def make_GUI_board(board):
    squares = []
    x = -75
    order = 0
    for i in range(4):
        x += 150
        y = -75
        c.create_line(x+75, 0, x+75, 600, fill='blue', width=3)
        for j in range(4):
            y += 150
            order += 1
            if i == 1:
                c.create_line(0, y+75, 600, y+75, fill='blue', width=3)
            squares.append(Square(c,(x,y),144, 'peach puff', order-1, ''))

    for value in board:
        place = value[0] + (4 * value[1])
        for item in squares:
            if item.order == place:
                item.changeValue(board[value])
    for item in squares:
        if item.value == 2:
            item.setColor('lavender')
        if item.value == 4:
            item.setColor('cornflower blue')
        if item.value == 8:
            item.setColor('pale goldenrod')
        if item.value == 16:
            item.setColor('dark seagreen')
        if item.value == 32:
            item.setColor('seagreen')
        if item.value == 64:
            item.setColor('yellow')
        if item.value == 128:
            item.setColor('orange')
        if item.value == 256:
            item.setColor('orange red')
        if item.value == 512:
            item.setColor('hot pink')
        if item.value == 1024:
            item.setColor('light sea green')
        if item.value == 2048:
            item.setColor('sandy brown')
        if item.value == 4096:
            item.setColor('snow')
        if item.value == 8192:
            item.setColor('violet')



def update_GUI(board, event):
    update(board, event)
    make_GUI_board(board)


def buttonPressed(event):
    letter = event.char
    update_GUI(b, event.char)

def erase_board(board):
    board = {}

def new_game(board):
    board = make_board()
    print(board)
    print('button pressed')
    make_GUI_board(board)



if __name__ == '__main__':
    root = Tk()
    root.geometry('600x600')
    c = Canvas(root, width=600, height=600)
    c.pack()
    b = make_board()
    make_GUI_board(b)
    root.bind('<w>', buttonPressed)
    root.bind('<a>', buttonPressed)
    root.bind('<d>', buttonPressed)
    root.bind('<s>', buttonPressed)
    root.mainloop()
