import pgzrun
import random

HEIGHT = 600
WIDTH = 800
R = 50

def draw():
    screen.fill('white')

    for y in range(R, HEIGHT, 2*R):
        for x in range(R, WIDTH, 2*R):
            for r in range(R, 0, -10):
                screen.draw.filled_circle((x, y), r,
                                          (random.randint(0, 255),
                                           random.randint(0, 255),
                                           random.randint(0, 255)))


# def draw():
#     screen.fill('white')
#
#     for y in range(0, HEIGHT, R):
#         for x in range(0, WIDTH, R):
#             screen.draw.circle((x, y), R,
#                                (random.randint(0, 255),
#                                 random.randint(0, 255),
#                                 random.randint(0, 255)))


def on_mouse_down():
    draw()


pgzrun.go()
