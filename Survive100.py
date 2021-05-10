import pgzrun
import random


HEIGHT = 600
WIDTH = 800
time = 0
balls = []
lives = []
invincible_time = 0

hero = Actor('hero')
live = 3


cookie = Actor('cookie')
cookie.x = 30
cookie.y = 30


class Ball:
    x = None
    y = None
    vx = None
    vy = None
    radius = None
    color = None

    def __init__(self, x, y, vx, vy, radius, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.color = color

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, self.color)

    def update(self):
        self.x += self.vx
        self.y += self.vy

        if self.x > WIDTH - self.radius or self.x < self.radius:
            self.vx = -self.vx
        if self.y > HEIGHT - self.radius or self.y < self.radius:
            self.vy = -self.vy


class SmartBall(Ball):
    targetX = None
    targetY = None

    def __init__(self, x, y, vx, vy, radius, color, targetX, targetY):
        super().__init__(x, y, vx, vy, radius, color)
        self.targetX = targetX
        self.targetY = targetY

    def updateValForTarget(self):
        if self.targetX > self.x:
            self.vx = random.randint(1, 2)
        elif self.targetX < self.x:
            self.vx = random.randint(-2, -1)
        if self.targetY > self.y:
            self.vy = random.randint(1, 2)
        elif self.targetY < self.y:
            self.vy = random.randint(-2, -1)


def initialize():
    global live, balls, time, invincible_time
    live = 3
    balls = []
    hero.image = 'hero'
    time = 0
    invincible_time = 0
    for i in range(live):
        live_pic = Actor('life')
        live_pic.x = 80+i*40
        live_pic.y = 30
        lives.append(live_pic)


def draw():
    screen.fill('white')
    for ball in balls:
        ball.draw()
    for i in range(live):
        lives[i].draw()
    if live == 0:
        screen.draw.text("Game Over!", (300, 280), fontsize=50, color='red')
        hero.draw()
    screen.draw.text(str(time) + " seconds", (350, 50), fontsize=30, color='blue')

    if invincible_time != 0 and invincible_time % 3 == 1:
        hero.draw()

    if invincible_time == 0:
        hero.draw()

    cookie.draw()


def on_mouse_down(pos):
    if cookie.collidepoint(pos):
        initialize()


def on_mouse_move(pos):
    if live > 0:
        hero.x = pos[0]
        hero.y = pos[1]


def update():
    global live, invincible_time
    if live <= 0:
        return
    for ball in balls:
        ball.update()
        if abs(hero.x - ball.x) < 25 and abs(hero.y - ball.y) < 30 \
                and invincible_time == 0:
            live -= 1
            invincible_time = 30
    if live <= 0:
        hero.image = 'hero_blowup'
    if invincible_time > 0:
        invincible_time -= 1


def count():
    global time
    if live > 0:
        time += 1
    if time % 1 == 0 and len(balls) < 20:
        x = WIDTH//2
        y = random.randint(5, HEIGHT//10)
        vx = random.choice([-3, -2, -1, 1, 2, 3])
        vy = random.randint(1, 3)
        r = 3

        if time % 5 == 0:
            color = 'red'
            ball = SmartBall(x, y, vx, vy, r, color, hero.x, hero.y)
        else:
            color = 'black'
            ball = Ball(x, y, vx, vy, r, color)
        balls.append(ball)

    for smart in balls:
        if isinstance(smart, SmartBall):
            smart.targetX = hero.x
            smart.targetY = hero.y
            smart.updateValForTarget()

    clock.schedule_unique(count, 1)


initialize()
count()
pgzrun.go()
