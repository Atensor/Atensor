# Tic Tac Toe 3.1 Sehr gute spiel by Atensor
from operator import add
from re import X
import pygame
import sys
import random


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode([600, 800])
pygame.display.set_caption('Tic Tac Toe')
screen.fill((255, 255, 255))
clock = pygame.time.Clock()


font = pygame.font.SysFont('Zusätze/OpenSans.ttf', 30)

ximage = pygame.image.load("Zusätze/X.png")


global move


global freespace
global change


global wins_player1
global wins_player2
global draws
wins_player1 = 0
wins_player2 = 0
draws = 0


def reset():
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global move
    global playerturn
    global change

    change = 1
    playerturn = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    move = 0

    screen.fill((255, 255, 255))


def isover(rect, pos):
    return True if rect.collidepoint(pos[0], pos[1]) else False


def zeichnen():
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 190, 190))
    pygame.draw.rect(screen, (0, 0, 0), (210, 0, 180, 190))
    pygame.draw.rect(screen, (0, 0, 0), (410, 0, 190, 190))
    pygame.draw.rect(screen, (0, 0, 0), (0, 210, 190, 180))
    pygame.draw.rect(screen, (0, 0, 0), (210, 210, 180, 180))
    pygame.draw.rect(screen, (0, 0, 0), (410, 210, 190, 180))
    pygame.draw.rect(screen, (0, 0, 0), (0, 410, 190, 190))
    pygame.draw.rect(screen, (0, 0, 0), (210, 410, 180, 190))
    pygame.draw.rect(screen, (0, 0, 0), (410, 410, 190, 190))

    pygame.draw.rect(screen, (0, 0, 0), (0, 620, 600, 190))


def circle():
    pygame.draw.circle(screen, (255, 255, 255), (cx, cy), 85, 20)


def cross():
    screen.blit(ximage, (xx, xy))


def getplayer():
    global playerturn
    playerturn = random.randint(1, 2)


def getmousepos():
    global move

    if x < 200 and y < 200:
        move = 1
    elif x > 200 and y < 200 and x < 400:
        move = 2
    elif x > 400 and y < 200:
        move = 3
    elif x < 200 and y > 200 and y < 400:
        move = 4
    elif x > 200 and y > 200 and x < 400 and y < 400:
        move = 5
    elif x > 400 and y > 200 and y < 400:
        move = 6
    elif x < 200 and y > 400 and y < 600:
        move = 7
    elif x > 200 and y > 400 and x < 400 and y < 600:
        move = 8
    elif x > 400 and y > 400 and y < 600:
        move = 9


def umwandlung():
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global move
    global playerturn

    if move == 1 and playerturn == 1 and a == 0:
        a = 1
    elif move == 2 and playerturn == 1 and b == 0:
        b = 1
    elif move == 3 and playerturn == 1 and c == 0:
        c = 1
    elif move == 4 and playerturn == 1 and d == 0:
        d = 1
    elif move == 5 and playerturn == 1 and e == 0:
        e = 1
    elif move == 6 and playerturn == 1 and f == 0:
        f = 1
    elif move == 7 and playerturn == 1 and g == 0:
        g = 1
    elif move == 8 and playerturn == 1 and h == 0:
        h = 1
    elif move == 9 and playerturn == 1 and i == 0:
        i = 1

    if move == 1 and playerturn == 2 and a == 0:
        a = 2
    elif move == 2 and playerturn == 2 and b == 0:
        b = 2
    elif move == 3 and playerturn == 2 and c == 0:
        c = 2
    elif move == 4 and playerturn == 2 and d == 0:
        d = 2
    elif move == 5 and playerturn == 2 and e == 0:
        e = 2
    elif move == 6 and playerturn == 2 and f == 0:
        f = 2
    elif move == 7 and playerturn == 2 and g == 0:
        g = 2
    elif move == 8 and playerturn == 2 and h == 0:
        h = 2
    elif move == 9 and playerturn == 2 and i == 0:
        i = 2


def nextplayer():
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global playerturn
    global freespace
    global change
    freespace = 0
    if a != 0:
        freespace += 1
    if b != 0:
        freespace += 1
    if c != 0:
        freespace += 1
    if d != 0:
        freespace += 1
    if e != 0:
        freespace += 1
    if f != 0:
        freespace += 1
    if g != 0:
        freespace += 1
    if h != 0:
        freespace += 1
    if i != 0:
        freespace += 1

    if freespace == change:
        geändert = 0
        if playerturn == 1:
            playerturn = 2
            geändert = 1
        elif playerturn == 2 and geändert == 0:
            playerturn = 1
        change += 1


def wincheck():
    global freespace
    global wins_player1
    global wins_player2
    global draws
    if a == 1 and b == 1 and c == 1 or d == 1 and e == 1 and f == 1 or g == 1 and h == 1 and i == 1 or a == 1 and d == 1 and g == 1 or b == 1 and e == 1 and h == 1 or c == 1 and f == 1 and i == 1 or a == 1 and e == 1 and i == 1 or c == 1 and e == 1 and g == 1:
        reset()
        print('p1 win')
        wins_player1 += 1
    if a == 2 and b == 2 and c == 2 or d == 2 and e == 2 and f == 2 or g == 2 and h == 2 and i == 2 or a == 2 and d == 2 and g == 2 or b == 2 and e == 2 and h == 2 or c == 2 and f == 2 and i == 2 or a == 2 and e == 2 and i == 2 or c == 2 and e == 2 and g == 2:
        reset()
        print('p2 win')
        wins_player2 += 1
    if freespace == 9:
        reset()
        print('Unentschieden')
        draws += 1


def showSprites():
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global xx
    global xy
    global cx
    global cy
    global playerturn

    if a == 1:
        xx = 20
        xy = 20
        cross()
    if b == 1:
        xx = 220
        xy = 20
        cross()
    if c == 1:
        xx = 420
        xy = 20
        cross()
    if d == 1:
        xx = 20
        xy = 220
        cross()
    if e == 1:
        xx = 220
        xy = 220
        cross()
    if f == 1:
        xx = 420
        xy = 220
        cross()
    if g == 1:
        xx = 20
        xy = 420
        cross()
    if h == 1:
        xx = 220
        xy = 420
        cross()
    if i == 1:
        xx = 420
        xy = 420
        cross()

    if a == 2:
        cx = 100
        cy = 100
        circle()
    if b == 2:
        cx = 300
        cy = 100
        circle()
    if c == 2:
        cx = 500
        cy = 100
        circle()
    if d == 2:
        cx = 100
        cy = 300
        circle()
    if e == 2:
        cx = 300
        cy = 300
        circle()
    if f == 2:
        cx = 500
        cy = 300
        circle()
    if g == 2:
        cx = 100
        cy = 500
        circle()
    if h == 2:
        cx = 300
        cy = 500
        circle()
    if i == 2:
        cx = 500
        cy = 500
        circle()

    if playerturn == 1:
        xx = 10
        xy = 630
        cross()
    elif playerturn == 2:
        cx = 90
        cy = 710
        circle()


def text():
    global wins_player1
    global wins_player2
    global draws
    text = font.render(('Unnentschieden: ' + str(draws)),
                       False, (255, 255, 255))
    text2 = font.render(('Spieler 1: ' + str(wins_player1)),
                        False, (255, 255, 255))
    text3 = font.render(('Spieler 2: ' + str(wins_player2)),
                        False, (255, 255, 255))
    screen.blit(text, (250, 675))
    screen.blit(text2, (250, 700))
    screen.blit(text3, (250, 725))
    pygame.display.update()


getplayer()
reset()
go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            getmousepos()
            print(move)
    if playerturn != 1 and playerturn != 2:
        getplayer()
    nextplayer()
    zeichnen()
    keys = pygame.key.get_pressed()
    umwandlung()
    showSprites()
    wincheck()
    text()
    pygame.display.update()
    clock.tick(5000)
