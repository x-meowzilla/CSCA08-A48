from graphics import *


# you need to download graphics.py and place it in the same folder as this code
def HTree(n, size, x, y, win):
    ''' (int, float, float, float, GraphWin) -> NoneType
    draw an HTree
    the first int is the order of the H Tree,
    size is the size of the horizontal and vertical line  of each H tree
    x, y are the cordinate of the middle of the horizontal line of the H
    '''

    if (n > 0):
        x0 = x - size / 2
        x1 = x + size / 2
        y0 = y - size / 2
        y1 = y + size / 2

        line = Line(Point(x0, y), Point(x1, y))
        line.setWidth(2)
        line.draw(win)
        line = Line(Point(x0, y0), Point(x0, y1))
        line.setWidth(2)
        line.draw(win)
        line = Line(Point(x1, y0), Point(x1, y1))
        line.setWidth(2)
        line.draw(win)

        HTree(n - 1, size / 2, x0, y0, win)
        HTree(n - 1, size / 2, x0, y1, win)
        HTree(n - 1, size / 2, x1, y0, win)
        HTree(n - 1, size / 2, x1, y1, win)


if (__name__ == "__main__"):
    # title and dimensions
    win = GraphWin('HTree', 500, 500)
    # first parameter shows the order
    # if you want to see a clear HTree try the order of 1 -  6
    # if you want to see how slow a recursive function can work, try it with order > 6

    HTree(5, 200, win.getWidth() / 2, win.getWidth() / 2, win)
    message = Text(Point(win.getWidth() / 2, 20), 'Click anywhere inside the window to quit.')
    message.draw(win)
    win.getMouse()
    win.close()
