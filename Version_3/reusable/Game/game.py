from random import *
from turtle import *
from freegames import vector

bird = vector(0, 0)
balls = []
score = 0


def game():

    rgb_list = ['red','lightcoral']

    def tap(x, y):
        "Move bird up in response to screen tap."
        up = vector(0, 30)
        bird.move(up)

    def inside(point):
        "Return True if point on screen."
        return -200 < point.x < 200 and -200 < point.y < 200

    def draw(alive):
        "Draw screen objects."
        clear()

        goto(bird.x, bird.y)

        if alive:
            global score

            dot(13, rgb_list[randrange(0,2)])
            score += 1
        else:

            print(f"your score is : {score-39}")
            dot(10, 'red')

            quit()

        for ball in balls:
            goto(ball.x, ball.y)
            dot(20, 'darkgray')

        update()

    def move():
        "Update object positions."
        bird.y -= 5

        for ball in balls:
            ball.x -= 3

        if randrange(10) == 0:
            y = randrange(-199, 199)
            ball = vector(199, y)
            balls.append(ball)

        while len(balls) > 0 and not inside(balls[0]):
            balls.pop(0)
            # pass

        if not inside(bird):
            draw(False)
            return

        for ball in balls:
            if abs(ball - bird) < 15:
                draw(False)
                return

        draw(True)
        ontimer(move, 40)

    setup(420, 420, 600, 200)
    hideturtle()
    up()
    tracer(False)
    onscreenclick(tap)
    move()
    done()

game()
