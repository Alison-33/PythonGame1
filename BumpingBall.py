import pgzrun

HEIGHT = 600  # height of window
WIDTH = 800  # width of window

x = WIDTH/2  # origin x coordinate of the ball
speed_x = 3  # speed of the ball along x-axis

y = HEIGHT/2  # origin y coordinate of the ball
speed_y = 3  # speed of the ball along y-axis

r = 30  # radius of the ball


# both draw() and update() would run in every frame generated.

# the function to draw the ball, run for every frame
def draw():
    screen.fill('white') # white background
    screen.draw.filled_circle((x, y), r, 'red')


def update():
    global y, speed_y, x, speed_x
    y = y+speed_y
    x = x+speed_x

    if x >= WIDTH-r or x <= r:
        speed_x = -speed_x
    if y >= HEIGHT-r or y <= r:
        speed_y = -speed_y

# start the game
pgzrun.go()
