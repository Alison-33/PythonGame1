import pgzrun
import random

WIDTH = 1920
HEIGHT = 1080
R = 10
balls = []


def draw():
    screen.fill('white')
    for ball in balls:
        screen.draw.filled_circle((ball[0], ball[1]), ball[4], (ball[5], ball[6], ball[7]))
        for x in range(1, ball[4], 10):
            screen.draw.filled_circle((ball[0], ball[1]), ball[4]-x, (random.randint(ball[5], 255),
                                                              random.randint(ball[6], 255),
                                                              random.randint(ball[7], 255)))


# def draw():
#     screen.fill('white')
#     for ball in balls:
#         screen.draw.filled_circle((ball[0], ball[1]), R, (ball[5], ball[6], ball[7]))
#         for x in range(1, R, 3):
#             screen.draw.filled_circle((ball[0], ball[1]), R-x, (random.randint(ball[5], 255),
#                                                               random.randint(ball[6], 255),
#                                                               random.randint(ball[7], 255)))



def update():
    for ball in balls:
        ball[0] = ball[0] + ball[2]
        ball[1] = ball[1] + ball[3]

        if ball[0] > WIDTH - ball[4] or ball[0] < ball[4]:
            ball[2] = -ball[2]

        if ball[1] > HEIGHT - ball[4] or ball[1] < ball[4]:
            ball[3] = -ball[3]


# def on_mouse_move(pos, rel, buttons):
#     if mouse.LEFT in buttons:
#         # take the position of the place that mouse clicked
#         x = pos[0]
#         y = pos[1]
#
#         speed_x = random.randint(1, 5)
#         speed_y = random.randint(1, 5)
#         r = random.randint(5, 50)
#         color_r = random.randint(10, 255)
#         color_g = random.randint(10, 255)
#         color_b = random.randint(10, 255)
#         ball = [x, y, speed_x, speed_y, r, color_r, color_g, color_b]
#         balls.append(ball)


def on_mouse_down(pos):
    # take the position of the place that mouse clicked
    x = pos[0]
    y = pos[1]

    for i in range(10):
        speed_x = random.randint(1, 5)
        speed_y = random.randint(1, 5)
        r = random.randint(5, 100)
        color_r = random.randint(10, 255)
        color_g = random.randint(10, 255)
        color_b = random.randint(10, 255)
        ball = [x, y, speed_x, speed_y, r, color_r, color_g, color_b]
        balls.append(ball)


pgzrun.go()

