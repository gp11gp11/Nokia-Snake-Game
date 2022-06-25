#Nokia snake game

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

snake_isnot_dead = True
while snake_isnot_dead:
  screen.update()
  time.sleep(.1)
  
  snake.move()
  #Detect collision with food
  if snake.head.distance(food)<15:
    food.refresh()
    scoreboard.increase_score()
    snake.add_segment()
  #Detect collision with wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
    snake_isnot_dead = False
    scoreboard.game_over()
  """#Detect collision with tail
  for seg in snake.segments:
    if seg == snake.head:
      pass
    elif snake.head.distance(seg) < 1:
      snake_isnot_dead = False
      scoreboard.game_over()
      #OR BY USING TUPLE
          
  """
  
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      snake_isnot_dead = False
      scoreboard.game_over()

screen.exitonclick()
