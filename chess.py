import pygame
from Chess.Piece import *

height, width = 1000, 600
re = min(height // 10, width // 10)
windowsize = (height, width)
GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COMBLUE = (233, 232, 255)

boardPieceArray = [
    [Rook(0, 0, "BR"), Horse(0, 1, "BH"), Bishop(0, 2, "BB"), Queen(0, 3, "BQ"), King(0, 4, "BK"), Bishop(0, 5, "BB"),
     Horse(0, 6, "BH"), Rook(0, 7, "BR")],
    [Pawn(1, 0, "B1"), Pawn(1, 1, "B2"), Pawn(1, 2, "B3"), Pawn(1, 3, "B4"), Pawn(1, 4, "B5"), Pawn(1, 5, "B6"),
     Pawn(1, 6, "B7"), Pawn(1, 7, "B8")], [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [Pawn(6, 0, "W1"), Pawn(6, 1, "W2"), Pawn(6, 2, "W3"), Pawn(6, 3, "W4"), Pawn(6, 4, "W5"), Pawn(6, 5, "W6"),
     Pawn(6, 6, "W7"), Pawn(6, 7, "W8")],
    [Rook(7, 0, "WR"), Horse(7, 1, "WH"), Bishop(7, 2, "WB"), Queen(7, 3, "WQ"), King(7, 4, "WK"), Bishop(7, 5, "WB"),
     Horse(7, 6, "WH"), Rook(7, 7, "WR")]]
boardDelArray = []
menuIconArray = [None, None]


# board generator
def chessboard(x, y, selist):
    screen.fill(GRAY)
    boardColorArray = [['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'], ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w'],
                       ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'], ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w'],
                       ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'], ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w'],
                       ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'], ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w']]
    for i in range(8):
        for j in range(8):
            if boardColorArray[i][j] == 'w':
                pygame.draw.rect(screen, WHITE, pygame.Rect((i * re) + re, (j * re) + re, re, re))
            else:
                pygame.draw.rect(screen, (32, 178, 170), pygame.Rect((i * re) + re, (j * re) + re, re, re))
    selector(x, y, 4, BLACK)
    if selist is not None:
        for i in selist:
            x, y = i
            selector(x, y, 3, NAVYBLUE)
    setIcon()


# fetches icon for the board
def getIcon(iconame):
    if not iconame.isalpha():
        iconame = list(iconame)
        iconame[1] = "P"
        iconame = "".join(iconame)
    pathname = iconame + ".png"
    brook = pygame.image.load(pathname)
    brook = pygame.transform.scale(brook, (re, re))
    return brook


# sets icon in the screen
def setIcon():
    for i in range(8):
        # temp = []
        for j in range(8):
            if boardPieceArray[i][j] is not None:
                if boardPieceArray[i][j].img is None:
                    boardPieceArray[i][j].img = getIcon(boardPieceArray[i][j].name)
                screen.blit(boardPieceArray[i][j].img, ((j * re) + re, (i * re) + re))


# creates a hollow square
def selector(x, y, wid, color):
    if x is not None and y is not None:
        pygame.draw.line(screen, color, ((y * re) + re - wid // 2, (x * re) + re),
                         (((y + 1) * re) + re + wid // 2, (x * re) + re), wid)
        pygame.draw.line(screen, color, ((y * re) + re, (x * re) + re),
                         ((y * re) + re, ((x + 1) * re) + re), wid)
        pygame.draw.line(screen, color, (((y + 1) * re) + re, (x * re) + re),
                         (((y + 1) * re) + re, ((x + 1) * re) + re), wid)
        pygame.draw.line(screen, color, ((y * re) + re, ((x + 1) * re) + re),
                         (((y + 1) * re) + re, ((x + 1) * re) + re), wid)


def animate(a, b, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dx /= 100
    dy /= 100
    for i in range(10):
        x1 += dx
        x2 += dy
        print(x1)
        print(x2)
        chessboard(None, None)
        screen.blit(boardIconArray[a][b], (x1, x2))
        clock.tick(10)


# find the cell using coord
def getBoxAtPixel(x, y):
    for i in range(8):
        for j in range(8):
            left, top = leftTopCoordsOfBox(i, j)
            boxRect = pygame.Rect(left, top, re, re)
            if boxRect.collidepoint(x, y):
                return j, i
    return None, None


def leftTopCoordsOfBox(i, j):
    left = i * re + re
    top = j * re + re
    return left, top


# checks whether the move is valid and switches the turn if required
def moveassigner(selecta, selectb, a, b, currentturn):
    if boardPieceArray[selecta][selectb].possiblemove(boardPieceArray, a, b, 1) != 0:
        if boardPieceArray[a][b] is not None:
            boardDelArray.append(boardPieceArray[a][b])
        boardPieceArray[a][b] = boardPieceArray[selecta][selectb]
        boardPieceArray[selecta][selectb] = None
        boardPieceArray[a][b].updatepos(a, b)
        if currentturn == "B":
            return "W"
        else:
            return "B"
    else:
        return currentturn


# turns the pawn to queen that reaches the very end
def pawnpower():
    for i in range(0, 8):
        if boardPieceArray[0][i] is not None and boardPieceArray[7][i] is not None:
            if not boardPieceArray[0][i].name.isalpha():
                boardPieceArray[0][i] = Queen(0, i, "WQ")
            elif not boardPieceArray[7][i].name.isalpha():
                boardPieceArray[7][i] = Queen(7, i, "BQ")


# fetches the menu icons
def getmenuicon(iconame):
    pat = iconame + ".png"
    im = pygame.image.load(pat)
    im = pygame.transform.scale(im, (3 * height // 10, int(1.5 * width / 10)))
    return im


# sets the menu icons
def setmenuicon():
    for i in range(2):
        if menuIconArray[i] is None:
            name = "menu" + str(i + 1)
            menuIconArray[i] = getmenuicon(name)
        screen.blit(menuIconArray[i], (int(6.5 * height / 10), int((i * 2 + 1) * width / 10)))


# changes the specified menu color
def changeimgcolor(i):
    menuIconArray[i].fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
    menuIconArray[i].fill((125, 0, 0) + (0,), None, pygame.BLEND_RGBA_ADD)


# resets the specified menu color
def resetimgcolor(n):
    for i in range(2):
        if i != n:
            name = "menu" + str(i + 1)
            menuIconArray[i] = getmenuicon(name)


def getmenubox(x, y):
    for i in range(2):
        l, t = coords(i)
        boxRect = pygame.Rect(l, t, 3 * height // 10, int(1.5 * width / 10))
        if boxRect.collidepoint(x, y):
            return i
    return None


def coords(y):
    a = int(6.5 * height / 10)
    b = int((y * 2 + 1) * width / 10)
    return a, b


def menudisp():
    im = pygame.image.load("che.jpg")
    im = pygame.transform.scale(im, (height, width))
    screen.blit(im, (0, 0))
    setmenuicon()


def movelistgenerator(select1, select2):
    temp = []
    for i in range(8):
        for j in range(8):
            if boardPieceArray[select1][select2].possiblemove(boardPieceArray, i, j, 0) != 0:
                temp.append((i, j))
    return temp


def chessb():
    pygame.init()
    done = False
    motionstop = False
    currentturn = "W"
    movelist = None
    selecta, selectb = None, None
    chessboard(selecta, selectb, movelist)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
                a, b = getBoxAtPixel(x, y)
                chessboard(selecta, selectb, movelist)
                if not motionstop:
                    selector(a, b, 4, BLUE)
                else:
                    selector(a, b, 3, BLUE)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                a, b = getBoxAtPixel(x, y)
                if (a is not None and b is not None) and not motionstop and boardPieceArray[a][b] is not None:
                    if boardPieceArray[a][b].name[0] == currentturn:
                        motionstop = True
                        selecta, selectb = a, b
                        movelist = movelistgenerator(a, b)
                        chessboard(selecta, selectb, movelist)
                        selector(a, b, 5, BLACK)
                    else:
                        selector(a, b, 5, RED)
                elif motionstop:
                    # animate(selecta, selectb, selecta * re + re, selectb * re + re, a * re + re, b * re + re)
                    currentturn = moveassigner(selecta, selectb, a, b, currentturn)
                    pawnpower()
                    tempa, tempb = selecta, selectb
                    selecta, selectb = None, None
                    movelist = None
                    motionstop = False
                    chessboard(selecta, selectb, movelist)
                    if boardPieceArray[tempa][tempb] is not None:
                        selector(a, b, 5, RED)
        pygame.display.update()


def mainmenu():
    global screen
    pygame.init()
    screen = pygame.display.set_mode(windowsize)
    done = False
    menudisp()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEMOTION:
                a, b = pygame.mouse.get_pos()
                n = getmenubox(a, b)
                if n is not None:
                    changeimgcolor(n)
                resetimgcolor(n)
            if event.type == pygame.MOUSEBUTTONDOWN:
                a, b = pygame.mouse.get_pos()
                n = getmenubox(a, b)
                if n == 0:
                    chessb()
                    done = True
                elif n == 1:
                    done = True
        menudisp()
        pygame.display.update()


mainmenu()
