import pgzrun
import random


WIDTH = 480
HEIGHT = 852
TITLE = 'Plane'
score = 0
is_loose = False
life = 3
invincible_time = 100
invincible_counter = 0
is_invincible = False
time_counter = 0
enemy_speed = 1.0


background1 = Actor('background')
background1.x = WIDTH/2
background1.y = HEIGHT/2
background2 = Actor('background')
background2.x = WIDTH/2
background2.y = -HEIGHT/2

hero = Actor('hero')
hero.x = WIDTH/2
hero.y = HEIGHT*2/3

life_image = Actor('life')
life_image.y = HEIGHT - 50
life_image.x = 50

sounds.game_music.play(-1)  # -1 means infinite loop

bullets = []
enemies = []
enemy_bullets = []

def draw():
    background1.draw()
    background2.draw()

    for bullet in bullets:
        bullet.draw()

    for enemy in enemies:
        enemy.draw()

    for e_bullet in enemy_bullets:
        e_bullet.draw()

    str1 = "Score: " + str(score)
    screen.draw.text(str1, (200, HEIGHT-50), fontsize=30, color='white')
    if is_loose:
        screen.draw.text("Game over!", (50, HEIGHT/2), fontsize=90, color='red')

    life_image.x = 50
    for i in range(life):
        life_image.draw()
        life_image.x += 50

    if is_invincible:
        if invincible_counter % 6 == 0:
            hero.draw()

    else:
        hero.draw()


def on_mouse_move(pos, rel, buttons):
    hero.x = pos[0]
    hero.y = pos[1]
    if is_loose:
        return


def on_mouse_down():
    global bullets
    sounds.gun.play()
    new_bullet = Actor('bullet')
    new_bullet.x = hero.x
    new_bullet.y = hero.y - 70
    bullets.append(new_bullet)

    if is_loose:
        return

def update():
    global score, is_loose, life, invincible_counter, is_invincible, time_counter, enemy_speed

    if time_counter % int(500/enemy_speed) == 0:
        enemy_num = random.randint(1, 4)
        for i in range(enemy_num):
            new_enemy = Actor('enemy')
            new_enemy.x = WIDTH / enemy_num * i + 50
            new_enemy.y = 0 + random.randint(0, 100)
            enemies.append(new_enemy)

    for enemy in enemies:
        if time_counter % 100 == 0:
            new_bullet = Actor('enemy_bullet')
            new_bullet.x = enemy.x
            new_bullet.y = enemy.y + 50
            enemy_bullets.append(new_bullet)

    for e_bullet in enemy_bullets:
        e_bullet.y += 5
        if e_bullet.y >= HEIGHT:
            enemy_bullets.remove(e_bullet)
        if e_bullet.colliderect(hero):
            sounds.explode.play()
            life -= 1
            is_invincible = True
            hero.x = WIDTH / 2
            hero.y = HEIGHT * 2 / 3
            if life == 0:
                is_loose = True
                hero.image = 'hero_blowup'

    background1.y += 1
    background2.y += 1
    if background1.y > HEIGHT/2 + HEIGHT:
        background1.y = -HEIGHT/2
    if background2.y > HEIGHT/2 + HEIGHT:
        background2.y = -HEIGHT/2

    for bullet in bullets:
        bullet.y -= 10
        if bullet.y < 0:
            bullets.remove(bullet)

    for enemy in enemies:
        enemy.y += 3
        if enemy.y > HEIGHT:
            enemy.y = 0
            enemy.x = random.randint(80, 400)

    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                sounds.got_enemy.play()
                score += 1
                enemies.remove(enemy)
                bullets.remove(bullet)

    if not is_invincible:
        for enemy in enemies:
            if hero.colliderect(enemy):
                sounds.explode.play()
                life -= 1
                is_invincible = True
                hero.x = WIDTH / 2
                hero.y = HEIGHT * 2 / 3
                if life == 0:
                    is_loose = True
                    hero.image = 'hero_blowup'

    if is_invincible:
        invincible_counter += 1
        if invincible_counter >= invincible_time:
            is_invincible = False
            invincible_counter = 0

    time_counter += 1

    if time_counter >= 10000:
        time_counter = 0

    if is_loose:
        return

    if time_counter % 300 == 0:
        enemy_speed += 0.3


pgzrun.go()
