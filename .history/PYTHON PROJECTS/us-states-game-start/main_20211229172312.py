import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

#Function to get x and y co-ordinates of each state, not needed due to CSV file already having data
###############################
#def get_mouse_click_coor(x, y):
#    print(x, y)
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()
###############################

states = pandas.read_csv("./50_states.csv")
all_states = states["state"].to_list()

correct_answers = []
total_answers = len(correct_answers)


while total_answers > 50:
    answer_state = screen.textinput(title=f"{total_answers}/50 States Correct", prompt="What's another state name?")
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states["state"] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    
    
    
screen.exitonclick()