import pgzrun
import random

TILE_SIZE = 50
WIDTH = 10*TILE_SIZE
HEIGHT = 10*TILE_SIZE
stars = []
tiles = []
connected_set = set()
find_connected = []
score = 0
cookie = Actor('cookie')
cookie.x = 390
cookie.y = 28


def initialize():
    global stars, tiles, connected_set, score, find_connected
    stars = []
    tiles = []
    for i in range(10):
        row = []
        for j in range(10):
            x = random.randint(1, 6)
            row.append(x)
        stars.append(row)
    updateTiles()
    connected_set = set()
    find_connected = []
    score = 0


def updateTiles():
    global tiles
    tiles = []
    for i in range(10):
        for j in range(10):
            tile = Actor('star' + str(stars[i][j]))
            tile.left = j*TILE_SIZE
            tile.top = i*TILE_SIZE
            tiles.append(tile)


def draw():
    screen.clear()
    for tile in tiles:
        tile.draw()
    screen.draw.text("Score: " + str(score), (410, 20), fontsize=25, color='white')
    cookie.draw()


def on_mouse_down(pos):
    global connected_set, score
    if cookie.collidepoint(pos):
        initialize()
        return
    tile_x = pos[1]//TILE_SIZE
    tile_y = pos[0]//TILE_SIZE
    color = stars[tile_x][tile_y]
    connected_set = set()
    connected_set.add((tile_x, tile_y))
    find_connected.append((tile_x, tile_y))

    while len(find_connected) != 0:

        (x, y) = find_connected.pop()
        stars[x][y] = 0
        print(str(x) + " " + str(y))
        if y != 9:
            if stars[x][y+1] == color:
                find_connected.append((x, y+1))
                connected_set.add((x, y+1))

        if y != 0:
            if stars[x][y-1] == color:
                find_connected.append((x, y-1))
                connected_set.add((x, y-1))

        if x != 0:
            if stars[x-1][y] == color:
                find_connected.append((x-1, y))
                connected_set.add((x-1, y))

        if x != 9:
            if stars[x+1][y] == color:
                find_connected.append((x+1, y))
                connected_set.add((x+1, y))

    if len(connected_set) == 1:
        stars[tile_x][tile_y] = color
    else:
        score += len(connected_set)
        temp_column = []
        for (x, y) in connected_set:
            stars[x][y] = 0
            temp_column.append(y)
        for j in temp_column:
            temp_list = []
            for i in range(10):
                temp_list.append(stars[i][j])
            count = 0
            while 0 in temp_list:
                temp_list.remove(0)
                count += 1
            for i in range(count):
                temp_list.insert(0, 0)  # insert a 0 to the top of column
            for i in range(10):
                stars[i][j] = temp_list[i]

        temp_list = []
        empty_columns = []
        for i in range(10):
            temp_list.append(stars[9][i])
            if stars[9][i] == 0:
                empty_columns.append(i)

        while len(empty_columns) != 0:
            col = empty_columns.pop()
            for j in range(col, 9):
                for i in range(10):
                    stars[i][j] = stars[i][j+1]
            for i in range(10):
                stars[i][9] = 0

    updateTiles()


initialize()
pgzrun.go()
