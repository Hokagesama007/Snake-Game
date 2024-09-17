from turtle import Turtle
ALIGNMENT="center"
FONT=('Arial', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.text") as high_score:
            self.high_score = int(high_score.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_score()



    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} vs Highest Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
    def reset(self):
        if self.score > self.high_score:
            self.score = self.high_score
            with open("data.text",mode="w") as high_score:
                high_score.write(f"{self.high_score}")
        self.score=0
        self.update_score()



