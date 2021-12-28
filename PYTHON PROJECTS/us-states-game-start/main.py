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
state_list = states["state"].to_list()
for i in range(len(state_list)):
    state_list[i] = state_list[i].lower()
print(state_list)
correct_answers = []
total_answers = len(correct_answers)
game_on = True
#while game_on:
    
#    answer_state = screen.textinput(title=f"{total_answers}/50 States Correct", prompt="What's another state name?")
    
    
