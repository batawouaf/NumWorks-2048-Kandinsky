from kandinsky import *
import random
import time
try :
    platform = "NumWorks"
    import ion
    from ion import *
except :
    import os
    if os.name == 'Omega' :
        platform = "NumWorks"
    else :
       import keyboard
       platform = "Pc"
score=0
max_score=0
last_score=0
time_stop = 0.2
Running = True
nb_case=4
width_screen = 320
height_screen = 225
size_game = 200
size_tiles = int((size_game/nb_case))
mide_game_x = (width_screen/2)-(size_game/2)
mide_game_y = (height_screen/2)-(size_game/2)
screen_game = []
ligne=[]
for _ in range(nb_case) :
    ligne.append(0)
for _ in range(nb_case) :
    screen_game.append(ligne[:])
# Moove part
def mvt_vertical(screen_game, max, indicator) :
   global score
   for y in range(len(screen_game)) :
       for x in range(len(screen_game)) :
           if screen_game[y][x] != 0:
               if y != max :
                   if screen_game[y+indicator][x] == 0 :
                       screen_game[y+indicator][x], screen_game[y][x] = screen_game[y][x], 0
                   else :
                       if screen_game[y][x] == screen_game[y+indicator][x] :
                           screen_game[y+indicator][x], screen_game[y][x] = screen_game[y+indicator][x]* 2, 0
                           score+=screen_game[y+indicator][x]
def mvt_horizontal(screen_game, max, indicator) :
    global score
    for y in range(len(screen_game)) :
        for x in range(len(screen_game)) :
            if screen_game[y][x] != 0:
                if x != max:
                    if screen_game[y][x+indicator] == 0 :
                        screen_game[y][x+indicator], screen_game[y][x] = screen_game[y][x], 0
                    else :
                        if screen_game[y][x] == screen_game[y][x+indicator] :
                            screen_game[y][x+indicator], screen_game[y][x] = screen_game[y][x+indicator]* 2, 0
                            score+=screen_game[y][x+indicator]
def mvt_hub(mvt,screen_game) :
    global last_score
    last_score=score
    if mvt == "z" :
      for _ in range(len(screen_game)):
          mvt_vertical(screen_game, 0, -1)
    if mvt == "s" :
      for _ in range(len(screen_game)):
          mvt_vertical(screen_game, len(screen_game)-1, 1)
    if mvt == "q" :
      for _ in range(len(screen_game)):
          mvt_horizontal(screen_game,0,-1)
    if mvt == "d" :
      for _ in range(len(screen_game)):
          mvt_horizontal(screen_game, len(screen_game)-1, 1)
    place_rdm_number(screen_game)
    update()
# Get color for bg
def get_color(number) :
   if number == 2 :
       return "#eee4da"
   elif number == 4 :
       return "#ede0c8"
   elif number == 8 :
       return "#f2b179"
   elif number == 16 :
       return "#f59563"
   elif number == 32 :
       return "#f67c5f"
   elif number == 64 :
       return "#f65e3b"
   elif number == 128 :
       return "#edcf72"
   elif number == 256 :
       return "#edcc61"
   elif number == 512 :
       return "#edc850"
   elif number == 1024 :
       return "#edc53f"
   elif number == 0 :
       return "#ccc0b4"
   else :
       return "#000000"
def get_color_font(hex_color) :
    hex_color = str(hex_color)
    hex_color = hex_color.replace('#', '')
    decimal_color = []
    for i in range(0, 6, 2) :
        decimal_color.append(int( str(list(hex_color)[i]+ list(hex_color)[i+1]) , 16))
    return tuple(decimal_color)
# Check if player can continue
def func_end(screen_game) :
    global Running
    impossible = 0
    for x in range(0, len(screen_game)) :
        for y in range(0, len(screen_game)) :
            nb_select = screen_game[x][y]
            if x != 0 :
                try :
                    nb_up = screen_game[x-1][y]
                    if nb_select != nb_up :
                        impossible += 1
                except :
                    impossible +=1
            if x != len(screen_game)-1 :
                try :
                    nb_down = screen_game[x+1][y]
                    if nb_select != nb_down :
                        impossible += 1
                except :
                    impossible +=1
            if y != len(screen_game)-1 :
                try :
                    nb_right = screen_game[x][y+1]
                    if nb_select != nb_right :
                        impossible += 1
                except :
                    impossible +=1
            if y != 0 :
                try :
                    nb_left = screen_game[x][y-1]
                    if nb_select != nb_left :
                        impossible += 1
                except :
                    impossible +=1
    if impossible == ((len(screen_game)**2)*4)-(4*len(screen_game)) :
        Running = False
def place_rdm_number(screen_game) :
    free_case=0
    for x in range(0, len(screen_game)):
        for y in range(0, len(screen_game)):
            if screen_game[x][y]!=0:
                free_case+=1
    if free_case == len(screen_game)**2:
        func_end(screen_game)
        return
    while True :
        rdm_x = random.randint(0, len(screen_game)-1)
        rdm_y = random.randint(0, len(screen_game)-1)
        if screen_game[rdm_y][rdm_x] == 0 :
            screen_game[rdm_y][rdm_x] = random.randint(1, 2)*2
            break
def update() :
    global score
    global last_score
    # Draw background and grid
    fill_rect(0,                0,                width_screen, height_screen, "#bbada0")
    fill_rect(int(mide_game_x), int(mide_game_y), size_game,    size_game,     "#EEE6D8")
    # Draw score
    draw_string(str(score),               0, int((mide_game_y/2)-(16/2))          , (255, 255, 255), (187, 173, 160) )
    draw_string("+ "+ str(score-last_score), 0, int((mide_game_y/2)-(16/2)+16*1)  , (255, 255, 255), (187, 173, 160)    )
    draw_string("max :",                    0, int((mide_game_y/2)-(16/2)+(16*2)+10), (255, 255, 255), (187, 173, 160) )
    draw_string(str(max_score),           0, int((mide_game_y/2)-(16/2)+(16*3)+10), (255, 255, 255), (187, 173, 160) )
    # Draw tiles
    for i in range(0, len(screen_game)) :
        for y in range(0, len(screen_game)) :
            fill_rect(int(mide_game_x+i*size_tiles),int(mide_game_y+y*size_tiles), size_tiles-2, size_tiles-2, str(get_color(screen_game[y][i])))
            # Draw number
            if screen_game[y][i]!=0 :
                color_font = int((len(list(str(screen_game[y][i])))*255)/10)
                draw_string(str(screen_game[y][i]),int((mide_game_x+i*(size_tiles)+size_tiles/2)-(10*len(list(str(screen_game[y][i])))/2)),int((mide_game_y+y*(size_tiles)+size_tiles/2)-(16/2)), (color_font,color_font,color_font), get_color_font(str(get_color(screen_game[y][i]))))
    time.sleep(time_stop)
place_rdm_number(screen_game)
update()
if platform == 'NumWorks' :
    while Running :
        if ion.keydown(KEY_UP) :
            mvt_hub("z",screen_game)
        if ion.keydown(KEY_DOWN) :
            mvt_hub("s",screen_game)
        if ion.keydown(KEY_LEFT) :
            mvt_hub("q",screen_game)
        if ion.keydown(KEY_RIGHT) :
            mvt_hub("d",screen_game)
elif platform == "Pc" :
    while Running :
        key_press = keyboard.read_key()
        if key_press in ["up", "haut"] :
            mvt_hub("z",screen_game)
        if key_press in ["down", "bas"] :
            mvt_hub("s",screen_game)
        if key_press in ["right", "droite"] :
           mvt_hub("d",screen_game)
        if key_press in ["left", "gauche"] :
           mvt_hub("q",screen_game)
draw_string("Game over", int((width_screen/2)-(10*len(list("Game over"))/2)),  int((height_screen/2)-16/2))
