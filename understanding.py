from snake import Snake
snake=Snake()
new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto

for seg_num in range(len(snake.segments) - 1, 0, -1):
       new_x = snake.segments[seg_num - 1].xcor()
       print(new_x)