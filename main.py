import pandas
from turtle import Screen, Turtle


screen = Screen()
screen.bgpic("blank_states_img.gif")

state_data = pandas.read_csv("50_states.csv")


counter = 0
correct_states = 0

printer = Turtle()
printer.penup()
printer.hideturtle()


while counter < 50:
    state_input = screen.textinput(f"{correct_states}/50 States Correct", "State name?").capitalize()
    if state_input in state_data["state"].to_list():
        state_x_cor = state_data[state_data["state"] == state_input].x.to_numpy()[0]
        state_y_cor = state_data[state_data["state"] == state_input].y.to_numpy()[0]
        printer.goto(state_x_cor, state_y_cor)
        printer.write(state_input, align="center")
        correct_states += 1
    counter += 1


screen.exitonclick()

