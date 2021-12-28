import turtle

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