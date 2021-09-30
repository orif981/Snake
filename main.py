import time
import random
import scoreboard
from scoreboard import ScoreBoard
from food import Food
from snake import Snake, screen


def hack():
    scoreboard1.score += random.randint(a=1234, b=4345)
    scoreboard1.clear()
    scoreboard1.write(f"Score: {scoreboard1.score}", False, "center", scoreboard.FONT)


p_snake = Snake()
game_on = True
eat = Food()
scoreboard1 = ScoreBoard()
while game_on:
    time.sleep(0.06)
    p_snake.move()
    screen.update()
    if p_snake.seg[0].distance(eat) <= 15:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        eat.setpos(x, y)
        scoreboard1.score += 1
        scoreboard1.rewrite()
        p_snake.extend()

    screen.onkey(hack, "h")

    if p_snake.seg[0].xcor() > 280 or p_snake.seg[0].xcor()<-280 or p_snake.seg[0].ycor()>280 or\
            p_snake.seg[0].ycor() < -280:
        scoreboard1.game_over()
        break

    for segment in p_snake.seg[1:]:
        if p_snake.seg[0].distance(segment) < 10:
            scoreboard1.game_over()
            game_on = False

try:
    with open (r'c:/networks/work/leaderboards.txt','a') as file:
        name = screen.textinput("Enter Your name", "")
        file.write(f"{name} - {scoreboard1.score} \n")
except:
    pass




screen.exitonclick()
if __name__ == '__main__':
    pass
