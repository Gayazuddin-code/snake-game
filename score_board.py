from turtle import Turtle
import os

FONT_SIZE = 24
FONT = ("Arial", FONT_SIZE, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.scored = 0
        self.high_score = 0
        self.color("dark orange")
        self.penup()
        self.hideturtle()
        self.sety(260)
        self.read_highscore()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score :{self.scored} High Score :{self.high_score}", align="center", font=FONT)

    def reset_turtle(self):
        if self.scored > self.high_score:
            self.high_score = self.scored
            self.write_highscore()
        self.scored = 0
        self.update_scoreboard()

    def increase_score(self):
        self.scored += 1
        self.update_scoreboard()

    def read_highscore(self):
        if not os.path.isfile("highscore_data.txt"):
            print("true")
            self.write_highscore()
        else:
            with open("highscore_data.txt", mode="r+") as file:
                file_score = file.read()
                if file_score == "":
                    file.write("0")
                    self.high_score = 0
                else:
                    score = int(file_score)
                    self.high_score = score

    def write_highscore(self):
        with open("highscore_data.txt", mode="w") as file:
            score = str(self.high_score)
            file.write(score)
