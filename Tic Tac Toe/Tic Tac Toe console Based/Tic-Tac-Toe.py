#Tic Tac Toe von Atensor V.2.2 Codename: wenn jetz noch ne Funktion dazukommt habe ich es Übersehen.

from ast import If
from doctest import OutputChecker
from ipaddress import _BaseNetwork
from posixpath import normpath
from typing import Counter
from weakref import WeakSet
import random

def print_playfield():
    print('')
    print('  1 2 3 x')    
    print('1 ' + north_west + ' ' + north + ' ' + north_east)
    print('2 ' + west + ' ' + middle + ' ' + east)
    print('3 ' + south_west + ' ' + south + ' ' + south_east)
    print('y')
    print('')

move_p1 = ''
move_p2 = ''
wins_player1 = 0
wins_player2 = 0

pn_set = False

def map_reset():
        global north_west 
        north_west = '-'
        global north
        north = '-'
        global north_east
        north_east = '-'
        global west
        west = '-'
        global middle
        middle = '-'
        global east
        east = '-'
        global south_west
        south_west = '-'
        global south
        south = '-'
        global south_east
        south_east = '-'

        print('')
        print('Feld wurde zurückgesetzt')

def winning_txt():
    global wins_player1
    global wins_player2
    if playerturn == 'player_2':
        print('Herzlichen Glückwunsch ' + player_1 + ' du hast gegen ' + player_2 + ' gewonnen')
        map_reset()
        wins_player1 = wins_player1 + 1
    elif playerturn == 'player_1':
        print('Herzlichen Glückwunsch ' + player_2 + ' du hast gegen ' + player_1 + ' gewonnen')
        map_reset()
        wins_player2 = wins_player2 + 1

p_set = False

print('Platziermöglichkeiten nach (x y):')
print('1 1, 2 1, 3 1')
print('1 2, 2 2, 3 2')
print('1 3, 2 3, 3 3')
print('nutze "spielstand" un den spielstand abzurufen(bei "reset wird er auch resettet")')
print('nutze "clear" um das spiel zurückzusetzen')
print('nutze "reset" um das spiel komplett zurückzusetzen')

map_reset()

print_playfield()

while True:

    if p_set == False:
        if pn_set == False:
            player_1 = input('Player 1, bitte gebe deinen Namen an: ')
            print('')
            player_2 = input('Player 2, bitte gebe deinen Namen an: ')
            print('')
            pn_set = True
        
        elif pn_set == True:
            ermittelt = False
            while ermittelt == False:
                ermittlungsmethode = input('wie soll der erste spieler vermittelt werden per "Auswahl" oder per "Zufall"? ')
                if ermittlungsmethode == 'Zufall':
                    zufallsspieler = random.randint(1,2)
                    if zufallsspieler == 1:
                        playerturn = 'player_1'
                    elif zufallsspieler == 2:
                        playerturn = 'player_2'
                    ermittelt = True
                    p_set = True
                    print('')
                elif ermittlungsmethode == 'Auswahl':
                    firstplayer = False
                    while firstplayer == False:
                        playerturn = input('Wer möchte anfangen? (' + player_1 + ' oder ' + player_2 + ') ')
                        print('')
                        if playerturn == player_1:
                            playerturn = 'player_1'
                            firstplayer = True
                            ermittelt = True
                            p_set = True
                        elif playerturn == player_2:
                            playerturn = 'player_2'
                            firstplayer = True
                            ermittelt = True
                            p_set = True
                        else:
                            print('Bitte nocheinmal eingeben:')
                else:
                    print('Bitte nochmal eingeben')

    elif p_set == True: 
        
        if playerturn == 'player_1':

            playerturn = 'player_2'
        
            move_p1 = input(player_1 + ' wohin möchtest du dein X platzieren? ')
            print('')

            if move_p1 == '1 1':
                if north_west == '-':
                    north_west = 'X'
                else:
                    print('Feld ist schon Besetzt (Zugwiederholung)')
                    playerturn = 'player_1'
            elif move_p1 == '2 1':
                if north == '-':
                    north = 'X'
                else:
                    print('Feld ist schon Besetzt (Zugwiederholung)')
                    playerturn = 'player_1'
            elif move_p1 == '3 1':
                if north_east == '-':
                    north_east = 'X'
                else:
                    print('Feld ist schon Besetzt (Zugwiederholung)')
                    playerturn = 'player_1'
            elif move_p1 == '1 2':
                if west == '-':
                    west = 'X'
                else:
                    print('Feld ist schon Besetzt (Zugwiederholung)')
                    playerturn = 'player_1'
            elif move_p1 == '2 2':
                if middle == '-':
                    middle = 'X'
                else:
                    print('Feld ist schon Besetzt (Zugwiederholung)')
                    playerturn = 'player_1'
            elif move_p1 == '3 2':
                if east == '-':
                    east = 'X'
                else:
                    print('Feld ist schon Besetzt (Zugwiederholung)')
                    playerturn = 'player_1'
            elif move_p1 == '1 3':
                if south_west == '-':
                    south_west = 'X'
                else:
                    print('Feld ist schon Besetzt (Zugwiederholung)')
                    playerturn = 'player_1'
            elif move_p1 == '2 3':
                if south == '-':
                    south = 'X'
                else:
                    print('Feld ist schon Besetzt (Zugwiederholung)')
                    playerturn = 'player_1'
            elif move_p1 == '3 3':
                if south_east == '-':
                    south_east = 'X'
                else:
                    print('Feld ist schon Besetzt (Zugwiederholung)')
                    playerturn = 'player_1'
            elif move_p1 == 'clear':
                map_reset()
            elif move_p1 == 'reset':
                map_reset()
                p_set = False
                pn_set = False
                wins_player1 = 0
                wins_player2 = 0
            elif move_p1 == 'spielstand':
                print(player_1+' hat '+str(wins_player1)+' Siege und '+player_2+' hat '+str(wins_player2)+' Siege')
                print('')
                playerturn = 'player_1'
            else:
                    print('Ungültige Eingabe (Zugwiederholung)')
                    playerturn = 'player_1'
            print_playfield()
    
    
        else:

            playerturn = 'player_1'
            
            move_p2 = input(player_2 + ' wohin möchtest du dein O platzieren? ')
            print('')

            if move_p2 == '1 1':
                if north_west == '-':
                    north_west = 'O'
                else :
                    print('Feld ist schon Besetzt (Zugwiederholung)')
                    playerturn = 'player_2'
            elif move_p2 == '2 1':
                if north == '-':
                    north = 'O'
                else :
                    print('Feld ist schon Besetzt (Zugwiederholung)')
                    playerturn = 'player_2'
            elif move_p2 == '3 1':
                if north_east == '-':
                    north_east = 'O'
                else :
                    print('Feld ist schon Besetzt (Zugwiederholung)')
                    playerturn = 'player_2'
            elif move_p2 == '1 2':
                if west == '-':
                    west = 'O'
                else :
                    print('Feld ist schon Besetzt (Zugwiederholung)')
                    playerturn = 'player_2'
            elif move_p2 == '2 2':
                if middle == '-':
                    middle = 'O'
                else :
                    print('Feld ist schon Besetzt (Zugwiederholung)')
                    playerturn = 'player_2'
            elif move_p2 == '3 2':
                if east == '-':
                    east = 'O'
                else :
                    print('Feld ist schon Besetzt (Zugwiederholung)')
                    playerturn = 'player_2'
            elif move_p2 == '1 3':
                if south_west == '-':
                    south_west = 'O'
                else :
                    print('Feld ist schon Besetzt (Zugwiederholung)')
                    playerturn = 'player_2'
            elif move_p2 == '2 3':
                if south == '-':
                    south = 'O'
                else :
                    print('Feld ist schon Besetzt (Zugwiederholung)')
                    playerturn = 'player_2'
            elif move_p2 == '3 3':
                if south_east == '-':
                    south_east = 'O'
                else :
                    print('Feld ist schon Besetzt (Zugwiederholung)')
                    playerturn = 'player_2'
            elif move_p2 == 'clear':
                map_reset()
            elif move_p2 == 'reset':
                map_reset()
                p_set = False
                pn_set	= False
                wins_player1 = 0
                wins_player2 = 0
            elif move_p2 == 'spielstand':
                print(player_1+' hat '+str(wins_player1)+' Siege und '+player_2+' hat '+str(wins_player2)+' Siege')
                print('')
                playerturn = 'player_2'
            else:
                    print('Ungültige Eingabe (Zugwiederholung)')
                    playerturn = 'player_2'
            print_playfield()
        
        if north_west == 'X' and north == 'X' and north_east == 'X' or north_west == 'O' and north == 'O' and north_east == 'O':
            winning_txt()
        elif west == 'X' and middle == 'X' and east == 'X' or  west == 'O' and middle == 'O' and east == 'O':
            winning_txt()
        elif south_west == 'X' and south == 'X' and south_east == 'X' or south_west == 'O' and south == 'O' and south_east == 'O':
            winning_txt()
        elif north_west == 'X' and west == 'X' and south_west == 'X' or north_west == 'O' and west == 'O' and south_west == 'O':
            winning_txt()
        elif north == 'X' and middle == 'X' and south == 'X' or  north == 'O' and middle == 'O' and south == 'O':
            winning_txt()
        elif north_east == 'X' and east == 'X' and south_east == 'X' or  north_east == 'O' and east == 'O' and south_east == 'O':
            winning_txt()
        elif north_west == 'X' and middle == 'X' and south_east == 'X' or  north_west == 'O' and middle == 'O' and south_east == 'O':
            winning_txt()
        elif north_east == 'X' and middle == 'X' and south_west == 'X' or  north_east == 'O' and middle == 'O' and south_west == 'O':
            winning_txt()
        elif north_west != '-' and north != '-' and north_east != '-' and west != '-' and middle != '-' and east != '-' and south_west != '-' and south != '-' and south_east != '-':
            print('Unnentschieden')
            map_reset()