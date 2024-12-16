import pyperclip

def HelperTab(l):
    global MAX_X
    global MAX_Y
    MAX_X = len(l)
    MAX_Y = len(l[0])

def MAX_X():
    return MAX_X
def MAX_Y():
    return MAX_Y

def IsOutOfBounds(x,y):
    return x < 0 or x >= MAX_X or y < 0 or y >= MAX_Y

def Pr(m):
    print(m)
    pyperclip.copy(m)

def Dir4():
    return (
        (-1,0),
        (0,1),
        (1,0),
        (0,-1),
    )
def Dir8():
    return (
        (-1,0),
        (-1,1),
        (0,1),
        (1,1),
        (1,0),
        (1,-1),
        (0,-1),
        (-1,-1),
    )