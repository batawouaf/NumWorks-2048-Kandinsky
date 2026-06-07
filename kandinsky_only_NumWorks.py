from kandinsky import *
import random
import time
import ion
from ion import *
score=0
#max_score=2492
max_score=0
l_score=0

time_stop = 0.4

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
   #screen_game.append([0, 0, 0, 0,0,0])
   screen_game.append(ligne[:])

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
       return "#f8339e"
   elif number == 0 :
       return "#ccc0b4"
   else :
       return "#000000"
   

def place_rdm_number(screen_game) :
 s=0
 for x in range(0, len(screen_game)):
     print(x)
     for y in range(0, len(screen_game)):
       if screen_game[x][y]!=0:
         s+=1
 if s==len(screen_game)**2:
   return
 while True :
   rdm_x = random.randint(0, len(screen_game)-1)
   rdm_y = random.randint(0, len(screen_game)-1)
   if screen_game[rdm_y][rdm_x] == 0 :
     screen_game[rdm_y][rdm_x] = random.randint(1, 2)*2
     break

def mvt_up(screen_game) :
   global score
   for y in range(len(screen_game)) :
       for x in range(len(screen_game)) :
           if screen_game[y][x] != 0:
               if y != 0 :
                   if screen_game[y-1][x] == 0 :
                       screen_game[y-1][x], screen_game[y][x] = screen_game[y][x], 0
                   else :
                       if screen_game[y][x] == screen_game[y-1][x] :
                           screen_game[y-1][x], screen_game[y][x] = screen_game[y-1][x]* 2, 0
                           score+=screen_game[y-1][x]

def mvt_down(screen_game) :
   global score
   for y in range(len(screen_game)) :
       for x in range(len(screen_game)) :
           if screen_game[y][x] != 0:
               if y != len(screen_game)-1 :
                   if screen_game[y+1][x] == 0 :
                       screen_game[y+1][x], screen_game[y][x] = screen_game[y][x], 0
                   else :
                       if screen_game[y][x] == screen_game[y+1][x] :
                           screen_game[y+1][x], screen_game[y][x] = screen_game[y+1][x]* 2, 0
                           score+=screen_game[y+1][x]


def mvt_right(screen_game) :
   global score
   for y in range(len(screen_game)) :
       for x in range(len(screen_game)) :
           if screen_game[y][x] != 0:
               if x != len(screen_game)-1 :
                   if screen_game[y][x+1] == 0 :
                       screen_game[y][x+1], screen_game[y][x] = screen_game[y][x], 0
                   else :
                       if screen_game[y][x] == screen_game[y][x+1] :
                           screen_game[y][x+1], screen_game[y][x] = screen_game[y][x+1]* 2, 0
                           score+=screen_game[y][x+1]


def mvt_left(screen_game) :
   global score
   for y in range(len(screen_game)) :
       for x in range(len(screen_game)) :
           if screen_game[y][x] != 0:
               if x != 0 :
                   if screen_game[y][x-1] == 0 :
                       screen_game[y][x-1], screen_game[y][x] = screen_game[y][x], 0
                   else :
                       if screen_game[y][x] == screen_game[y][x-1] :
                           screen_game[y][x-1], screen_game[y][x] = screen_game[y][x-1]* 2, 0
                           score+=screen_game[y][x-1]


def update() :
   global score
   global l_score
   fill_rect(0, 0, width_screen, height_screen, "#bbada0")
   fill_rect(int(mide_game_x),int(mide_game_y), size_game, size_game, "#EEE6D8")
   draw_string(
   str(score),
   0,
   int((mide_game_y/2)-(16/2))
   )
   draw_string(
   "+ "+ str(score-l_score),
   0,
   int((mide_game_y/2)-(16/2)+16*1)
   )
   draw_string(
   "max",
   0,
   int((mide_game_y/2)-(16/2)+(16*2)+10)
   )
   draw_string(
   str(max_score),
   0,
   int((mide_game_y/2)-(16/2)+(16*3)+10)
   )
   for i in range(0, len(screen_game)) :
       for y in range(0, len(screen_game)) :
           fill_rect(int(mide_game_x+i*size_tiles),int(mide_game_y+y*size_tiles), size_tiles-2, size_tiles-2, str(get_color(screen_game[y][i])))
           if screen_game[y][i]!=0:
             draw_string(
             str(screen_game[y][i]),
             int((mide_game_x+i*(size_tiles)+size_tiles/2)-(10*len(list(str(screen_game[y][i])))/2)),
             int((mide_game_y+y*(size_tiles)+size_tiles/2)-(16/2))
             )
           
   time.sleep(time_stop)

def mvt_hub(mvt,screen_game) :
 global l_score
 l_score=score
 for _ in range(len(screen_game)):
   if mvt == "z" :
     mvt_up(screen_game)
   if mvt == "s" :
     mvt_down(screen_game)
   if mvt == "q" :
     mvt_left(screen_game)
   if mvt == "d" :
     mvt_right(screen_game)

 place_rdm_number(screen_game)
 update()

place_rdm_number(screen_game)
update()
while True :

   if ion.keydown(KEY_UP) :
       mvt_hub("z",screen_game)
   if ion.keydown(KEY_DOWN) :
       mvt_hub("s",screen_game)
   if ion.keydown(KEY_LEFT) :
       mvt_hub("q",screen_game)
   if ion.keydown(KEY_RIGHT) :
       mvt_hub("d",screen_game)
