import pgzrun
import random

WIDTH = 600
HEIGHT = 800

player_speed = 3
brick_speed = 1
player_on_ground = False
is_lose = False
score = 0

alien = Actor('alien')
alien.x = WIDTH / 2
alien.y = HEIGHT / 2
last_alien_y = alien.y

bricks = []

for i in range(5):
    b = Actor('brick')
    b.pos = 100*(i+1), 150*(i+1)
    bricks.append(b)


def draw():
    screen.clear()
    alien.draw()
    for brick in bricks:
        brick.draw()

    screen.draw.text("You have survived " + str(score) + " floors!", (350, 20), fontsize=25, color='white')

    if is_lose:
        screen.draw.text('Game Over!', (140, HEIGHT/2-100), fontsize=80, color='red')


def update():
    global player_on_ground, is_lose, brick_speed, last_alien_y, score
    player_on_ground = False
    for brick in bricks:
        if abs(alien.bottom - brick.top) < 10 and \
                brick.left - alien.left < alien.width * 2 / 3 and \
                alien.right - brick.right < alien.width * 2 / 3:
            player_on_ground = True
            alien.bottom = brick.top
            alien.image = 'alien'

            if last_alien_y < alien.y:
                score += 1
                if score % 5 == 0:
                    brick_speed += 1

    if keyboard.left:
        alien.x = alien.x - player_speed
    if keyboard.right:
        alien.x = alien.x + player_speed

    last_alien_y = alien.y

    if not player_on_ground:
        alien.y += player_speed
        alien.image = 'alien_falling'

    if bricks[0].top < 10:
        del bricks[0]
        new_brick = Actor('brick')
        new_brick.x = random.randint(100, 500)
        new_brick.y = HEIGHT
        bricks.append(new_brick)

    for brick in bricks:
        brick.y -= brick_speed

    if alien.top < 0 or alien.bottom > HEIGHT:
        is_lose = True

# anims = [Actor('1'), Actor('2'), Actor('3'), Actor('4'), Actor('5')]
#
# num_anims = len(anims)
# anim_index = 0
# player_x = WIDTH/2
# player_y = HEIGHT/2
# counter = 0
#
#
# for i in range(num_anims):
#     anims[i].x = player_x
#     anims[i].y = player_y
#
#
# def draw():
#     screen.fill('gray')
#     anims[anim_index].draw()
#
#
# def update():
#     global anim_index, player_x, counter
#     if keyboard.right:
#         counter += 1
#         player_x += 5
#         for i in range(num_anims):
#             anims[i].x = player_x
#         if player_x >= WIDTH:
#             player_x = 0
#         if counter % 5 == 0:
#             anim_index += 1
#         if anim_index >= num_anims:
#             anim_index = 0
#
#     if counter >= 10000:
#         counter = 0




pgzrun.go()
