import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_states = []

while len(guess_states) < 50:

    answer_state = screen.textinput(title=f"{len(guess_states)}/50 Guess the State", 
                                    prompt="What's another state's name ?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guess_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # if answer_state is on the states in all 50 states.csv file
    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        # create a turtle to write state name on the state x, y coordinates
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())



screen.exitonclick()


# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
