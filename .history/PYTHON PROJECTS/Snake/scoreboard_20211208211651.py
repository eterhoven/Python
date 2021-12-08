from turtle import Turtle

with open("data.txt") a file:
    highest = file.read()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.high_score = highest
        self.write(f"Score: {self.score} High score: {self.high_score}", False,'center', ('Arial', 24, 'normal'))
        self.hideturtle() 
        
    def keep_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", False,'center', ('Arial', 24, 'normal'))
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.clear()
            self.score = 0
            self.write(f"Score: {self.score} High score: {self.high_score}", False,'center', ('Arial', 24, 'normal'))

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", False,'center', ('Arial', 24, 'normal')) 