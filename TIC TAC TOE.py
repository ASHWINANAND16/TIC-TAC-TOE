import pygame
import sys
import time
from pygame.locals import *

#global variables
xo='x'
winner=None
draw=False
size=width,height=400,500
line=400/3
white=(255,255,255)
line_color=(0,0,0)

#board
board=[[None]*3,[None]*3,[None]*3]

#game display
pygame.init()
fps=30
clock=pygame.time.Clock()
screen=pygame.display.set_mode(size,0,32)
pygame.display.set_caption("TIC TAC TOE")

#loading images
opening_img=pygame.image.load("opening.png")
x_img=pygame.image.load("x.png")
o_img=pygame.image.load("o.png")

#resizing images
opening_img=pygame.transform.scale(opening_img,(400,500))
x_img=pygame.transform.scale(x_img,(80,80))
o_img=pygame.transform.scale(o_img,(80,80))

def opening():

    #opening screen
    screen.blit(opening_img,(0,0))
    pygame.display.update()
    time.sleep(1)
    screen.fill(white)

    #drawing rows
    pygame.draw.line(screen,line_color,(0,line),(400,line),7)
    pygame.draw.line(screen,line_color,(0,line*2),(400,line*2),7)

    #drawing columns
    pygame.draw.line(screen,line_color,(line,0),(line,500),7)
    pygame.draw.line(screen,line_color,(line*2,0),(line*2,500),7)

    status()

def status():

    global draw

    if winner is None:
        message=xo.upper()+"'s turn"
    else:
        message=winner.upper()+" wins!"
    if draw:
        message="It's a draw!"

    #displaying the message
    font=pygame.font.Font(None,30)
    img=font.render(message,1,white)
    screen.fill((0,0,0),(0,400,500,100))
    img_rect=img.get_rect(center=(200,450))
    screen.blit(img,img_rect)
    pygame.display.update()

def check():

    global board,winner,draw

    #check rows
    for row in range(0,3):
        if ((board[row][0]==board[row][1]==board[row][2]) and (board[row][0] is not None)):
            winner=board[row][0]
            pygame.draw.line(screen,(250,0,0),(0, (row + 1)*height/3 -height/6),(width, (row + 1)*height/3 - height/6 ), 4)
            break

    #check columns
    for column in range(0,3):
        if ((board[0][column]==board[1][column]==board[2][column]) and (board[0][column] is not None)):
            winner=board[0][column]
            pygame.draw.line (screen, (250,0,0),((col + 1)* width/3 - width/6, 0), ((col + 1)* width/3 - width/6, height), 4)
            break

    #check diagonals
    if(board[0][0]==board[1][1]==board[2][2] and board[0][0] is not None):
        winner=board[0][0]
        pygame.draw.line (screen, (250,70,70), (50, 50), (350, 350), 4)

    if(board[0][2]==board[1][1]==board[2][0] and board[0][2] is not None):
        winner=board[0][2]
        pygame.draw.line (screen, (250,70,70), (350, 50), (50, 350), 4)

    #check draw
    if(all ([all(row) for row in board]) and winner is None):
        draw=True

    status()

def drawxo(row,column):

    #drawing x or o
    global board,xo

    if row==1:
        pos_x=30
    if row==2:
        pos_x=line+30
    if row==3:
        pos_x=line*2+30

    if column==1:
        pos_y=30
    if column==2:
        pos_y=line+30
    if column==3:
        pos_y=line*2+30

    board[row-1][column-1]=xo

    if(xo=='x'):
        screen.blit(x_img,(pos_y,pos_x))
        xo='o'
    else:
        screen.blit(o_img,(pos_y,pos_x))
        xo='x'

    pygame.display.update()

def click():

    #coordinates of mouse click
    x,y=pygame.mouse.get_pos()

    #get column
    if(x<line):
        column=1
    elif(x<line*2):
        column=2
    elif(x<width):
        column=3
    else:
        column=None

    #get row
    if(y<line):
        row=1
    elif(y<line*2):
        row=2
    elif(y<400):
        row=3
    else:
        row=None

    if(row and column and board[row-1][column-1] is None):
        global xo
        drawxo(row,column)
        check()

def reset():

    global board,winner,draw,xo
    time.sleep(3)
    xo='x'
    draw=False
    opening()
    winner=None
    board=[[None]*3,[None]*3,[None]*3]

opening()

#loop to run the game undefinitely until closed
while(True):
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==MOUSEBUTTONDOWN:
            click()
            if(winner or draw):
                reset()
    pygame.display.update()
    clock.tick(fps)