from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.high_score = 0
        self.write(f"Score: {self.score}", False,'center', ('Arial', 24, 'normal'))
        self.hideturtle() 
        
    def keep_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False,'center', ('Arial', 24, 'normal'))
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", False,'center', ('Arial', 24, 'normal')) 