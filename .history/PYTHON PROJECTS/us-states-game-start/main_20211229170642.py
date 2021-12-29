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

correct_answers = []
total_answers = len(correct_answers)
global correct_answers
global total_answers
game_on = True
while game_on:
    global correct_answers
    global total_answers
    
    answer_state = screen.textinput(title=f"{total_answers}/50 States Correct", prompt="What's another state name?")
    check_answer = states["state"].str.contains(f"{answer_state}").any()
    if check_answer == True:
        correct_answers.append(answer_state)
    
    #if states["state"].str.contains(f"{answer_state}") == True:
    #    correct_answers.append(answer_state)
    
    
    
turtle.mainloop()