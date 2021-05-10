import pgzrun
import random
import time

TILE_SIZE = 20
WIDTH = 40*TILE_SIZE
HEIGHT = 30*TILE_SIZE

snake_head = Actor('snake1')
snake_head.x = WIDTH/2
snake_head.y = HEIGHT/2
move_speed = 20
# time_speed = 0.5
counter = 0
can_move = True
is_lose = False
score = 0

cookie = Actor('cookie')
cookie.x = random.randint(10, 30) * TILE_SIZE
cookie.y = random.randint(10, 20) * TILE_SIZE

Snake = [snake_head]

direction = 'right'

for i in range(4):
    snake_body = Actor('snake1')
    snake_body.x = Snake[i].x - TILE_SIZE
    snake_body.y = Snake[i].y
    Snake.append(snake_body)


def draw():
    screen.clear()
    for body in Snake:
        body.draw()

    cookie.draw()

    screen.draw.text("Score: " + str(score), (360, 20), fontsize=25, color = 'white')

    if is_lose:
        screen.draw.text('Game Over!', (180, HEIGHT/2-100), fontsize=100, color='blue')


def update():
    global direction, counter, is_lose, can_move, score

    if can_move:
        if keyboard.left and direction != 'right':
            direction = 'left'
            can_move = False
        if keyboard.right and direction != 'left':
            direction = 'right'
            can_move = False
        if keyboard.up and direction != 'down':
            direction = 'up'
            can_move = False
        if keyboard.down and direction != 'up':
            direction = 'down'
            can_move = False

    if counter % (move_speed-int(score/5)) == 0:
        new_snake_head = Actor('snake1')
        if direction == 'right':
            new_snake_head.x = Snake[0].x + TILE_SIZE
            new_snake_head.y = Snake[0].y
        if direction == 'left':
            new_snake_head.x = Snake[0].x - TILE_SIZE
            new_snake_head.y = Snake[0].y
        if direction == 'up':
            new_snake_head.x = Snake[0].x
            new_snake_head.y = Snake[0].y - TILE_SIZE
        if direction == 'down':
            new_snake_head.x = Snake[0].x
            new_snake_head.y = Snake[0].y + TILE_SIZE

        if new_snake_head.y < 0 or new_snake_head.y > HEIGHT \
                or new_snake_head.x < 0 or new_snake_head.x > WIDTH:
            is_lose = True

        for i in range(len(Snake)):
            if i <= 3:  # it is not possible for the head to bump in the first 3 tiles of body
                continue
            if new_snake_head.x == Snake[i].x and new_snake_head.y == Snake[i].y:
                is_lose = True
                break

        if not is_lose:
            Snake.insert(0, new_snake_head)
            if new_snake_head.x == cookie.x and new_snake_head.y == cookie.y:
                cookie_on_snake = True
                while cookie_on_snake:
                    cookie.x = random.randint(10, 30) * TILE_SIZE
                    cookie.y = random.randint(10, 20) * TILE_SIZE
                    cookie_on_snake = False
                    for body in Snake:
                        if cookie.x == body.x and cookie.y == body.y:
                            cookie_on_snake = True

                score += 1
            else:
                del Snake[len(Snake) - 1]
            can_move = True

    counter += 1


# the following methods are written on the book, but there exists problems, for example
# if the snake is going right and we press up and left rapidly, the snake can turn about
# with out changing the head's y-position.

# def update():
#     global direction
#     if keyboard.left and direction != 'right':
#         direction = 'left'
#     if keyboard.right and direction != 'left':
#         direction = 'right'
#     if keyboard.up and direction != 'down':
#         direction = 'up'
#     if keyboard.down and direction != 'up':
#         direction = 'down'

# def moveSnake():
#     global counter, is_lose, score
#     new_snake_head = Actor('snake1')
#     if direction == 'right':
#         new_snake_head.x = Snake[0].x + TILE_SIZE
#         new_snake_head.y = Snake[0].y
#     if direction == 'left':
#         new_snake_head.x = Snake[0].x - TILE_SIZE
#         new_snake_head.y = Snake[0].y
#     if direction == 'up':
#         new_snake_head.x = Snake[0].x
#         new_snake_head.y = Snake[0].y - TILE_SIZE
#     if direction == 'down':
#         new_snake_head.x = Snake[0].x
#         new_snake_head.y = Snake[0].y + TILE_SIZE
#
#     if new_snake_head.y < 0 or new_snake_head.y > HEIGHT \
#             or new_snake_head.x < 0 or new_snake_head.x > WIDTH:
#         is_lose = True
#
#     for i in range(len(Snake)):
#         if i <= 3:  # it is not possible for the head to bump in the first 3 tiles of body
#             continue
#         if new_snake_head.x == Snake[i].x and new_snake_head.y == Snake[i].y:
#             is_lose = True
#             break
#
#     if not is_lose:
#         Snake.insert(0, new_snake_head)
#         if new_snake_head.x == cookie.x and new_snake_head.y == cookie.y:
#             cookie_on_snake = True
#             while cookie_on_snake:
#                 cookie.x = random.randint(10, 30) * TILE_SIZE
#                 cookie.y = random.randint(10, 20) * TILE_SIZE
#                 cookie_on_snake = False
#                 for body in Snake:
#                     if cookie.x == body.x and cookie.y == body.y:
#                         cookie_on_snake = True
#
#             score += 1
#         else:
#             del Snake[len(Snake) - 1]
#         clock.schedule_unique(moveSnake, time_speed)
#
# moveSnake()
pgzrun.go()

