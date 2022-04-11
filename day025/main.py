import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?").title()

    if user_answer == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if user_answer in states_list:
        guessed_states.append(user_answer)
        for index in states_list:
            state_data = data[data.state == user_answer]
            writer.goto(int(state_data.x), int(state_data.y))
            writer.write(f"{user_answer} ", align="left", font=("Courier", 10, "normal"))
