import pgzrun


needles = []
start_needle = Actor('needle', anchor=(170+50, 1.5))
start_needle.x = 220
start_needle.y = 300
rotate_speed = 1
score = 0



def draw():
    screen.fill('white')
    start_needle.draw()
    for needle in needles:
        needle.draw()
    screen.draw.circle((400, 300), 80, 'red')
    screen.draw.text(str(score), (50, 250), fontsize=30, color='green')
    if rotate_speed == 0:
        screen.draw.text("Game over!", (10, 320), fontsize=35, color='red')


def update():
    for needle in needles:
        needle.angle = needle.angle + rotate_speed


def on_key_down():
    global rotate_speed
    global score
    new_needle = Actor('needle', anchor=(170 + 50, 1.5))
    new_needle.x = 400
    new_needle.y = 300
    for needle in needles:
        if new_needle.colliderect(needle):
            print('游戏失败')
            rotate_speed = 0
            music.play_once('溜走')

    needles.append(new_needle)
    if rotate_speed > 0:
        score += 1
        music.play_once('弹簧')



def restart():
    global needles
    needles = []


pgzrun.go()
