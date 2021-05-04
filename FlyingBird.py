import pgzrun
import random

WIDTH = 350
HEIGHT = 590

score = 0
speed = 1
time = 0.0

background = Actor('background')
bird = Actor('bird')
bird.x = 50
bird.y = HEIGHT/2

bar_up = Actor('bar_up')
bar_up.x = 300
bar_up.y = 0
bar_down = Actor('bar_down')
bar_down.x = 300
bar_down.y = 600


def draw():
    background.draw()
    bar_up.draw()
    bar_down.draw()
    bird.draw()
    screen.draw.text(str(score), (30, 30), fontsize=50, color='green')


def update():
    global score
    global speed
    global time
    time = time + 0.1
    bird.y = bird.y + 0.9*(time + 0.05*(time**2))
    bar_up.x = bar_up.x - 2*speed
    bar_down.x = bar_down.x - 2*speed
    if bar_up.x < 0:
        score += 1
        if (score % 5) == 0 and score != 0:
            speed += 0.5
        bar_up.x = WIDTH
        bar_down.x = WIDTH
        bar_up.y = random.randint(-200, 200)
        bar_down.y = 600 + bar_up.y
    if bird.colliderect(bar_up) or bird.colliderect(bar_down) \
            or bird.y == 0 or bird.y == HEIGHT:
        reset()


def on_mouse_down():
    global time
    bird.y = bird.y - 100
    time = 0


def reset():
    global time
    global score
    global speed
    score = 0
    speed = 1
    time = 0
    bird.x = 50
    bird.y = HEIGHT / 2
    bar_up.x = 300
    bar_up.y = 0
    bar_down.x = 300
    bar_down.y = 600



pgzrun.go()
