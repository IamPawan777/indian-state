import turtle
import pandas

sc = turtle.Screen()
sc.title("India State")
img = "India.gif"
sc.addshape(img)
turtle.shape(img)

data = pandas.read_csv("state_data.csv")
all_state = data.state.to_list()
guessed_states = []

while len(guessed_states) < 31:
    # INPUT BOX
    answer_state = sc.textinput(title=f"{len(guessed_states)}/28 State Correct",
                                prompt="What is another state ?").title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_states.csv")
        break

    if answer_state in all_state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)
