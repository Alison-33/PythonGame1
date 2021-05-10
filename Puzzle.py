import pgzrun
import random
import datetime

TILE_SIZE = 100
WIDTH = 3*TILE_SIZE
HEIGHT = 350

click1 = -1
click2 = -1
# click_time = 0
all_right = False

start = datetime.datetime.now().replace(microsecond=0)

end = 0
finish_time = 0
old_time = -1

txt = open('rank.txt', 'r')
line = txt.readline()
if len(line) >= 1:
    old_time = datetime.datetime.strptime(line, '%H:%M:%S')-\
               datetime.datetime.strptime("0:0:0", '%H:%M:%S')
txt.close()

cookie = Actor('cookie')
cookie.x = 50
cookie.y = 320

tiles = [Actor('3×3_01'), Actor('3×3_02'), Actor('3×3_03'),
         Actor('3×3_04'), Actor('3×3_05'), Actor('3×3_06'),
         Actor('3×3_07'), Actor('3×3_08'), Actor('3×3_09')]

for i in range(3):
    for j in range(3):
        tiles[i*3+j].left = j * TILE_SIZE
        tiles[i*3+j].top = i * TILE_SIZE


def swapPosition(i, j):
    temp = tiles[i].pos
    tiles[i].pos = tiles[j].pos
    tiles[j].pos = temp


for k in range(13):
    i = random.randint(0, 8)
    j = random.randint(0, 8)
    swapPosition(i, j)


def draw():
    screen.clear()
    for tile in tiles:
        tile.draw()
    if all_right:
        screen.draw.text("You Win!", (80, 300/2-50), fontsize=50, color='blue')
    else:
        for i in range(3):
            screen.draw.line((0, i*TILE_SIZE), (WIDTH, i*TILE_SIZE), 'white')
            screen.draw.line((i * TILE_SIZE, 0), (i * TILE_SIZE, 300), 'white')
        if click1 != -1:
            screen.draw.rect(Rect((tiles[click1].left, tiles[click1].top), (TILE_SIZE, TILE_SIZE)), 'red')

    if old_time != -1:
        screen.draw.text("Best: " + str(old_time), (120, 310), fontsize=20, color='white')
    else:
        screen.draw.text("Best: None", (120, 310), fontsize=20, color='white')

    screen.draw.text("Current Time: " + str(datetime.datetime.now().replace(microsecond=0)-start),
                     (105, 330), fontsize=20, color='white')
    cookie.draw()


def on_mouse_down(pos):
    global click1, click2
    for k in range(9):
        if tiles[k].collidepoint(pos):
            if click1 == -1:
                click1 = k
            elif click2 == -1:
                click2 = k
            break
    if cookie.collidepoint(pos):
        restart()

def update():
    global click1, click2, all_right, end, finish_time, old_time
    if click1 != -1 and click2 != -1:
        swapPosition(click1, click2)
        click1 = -1
        click2 = -1

    all_right = True
    for i in range(3):
        for j in range(3):
            if tiles[i*3+j].left != j*TILE_SIZE \
                    or tiles[i*3+j].top != i*TILE_SIZE:
                all_right = False
                break
    if all_right:
        end = datetime.datetime.now().replace(microsecond=0)
        finish_time = end - start

        if old_time == -1 or finish_time < old_time:
            txt = open('rank.txt', 'w')
            txt.write(str(finish_time))
            txt.close()
            old_time = finish_time


def restart():
    global start, all_right
    all_right = False
    start = datetime.datetime.now().replace(microsecond=0)
    for k in range(13):
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        swapPosition(i, j)


pgzrun.go()
