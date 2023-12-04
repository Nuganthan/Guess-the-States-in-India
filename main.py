import pandas
import turtle

screen = turtle.Screen()
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("28_india_states.csv")
all_states = data.state.to_list()
guessed_states = []

is_game_on = True
while is_game_on:
    guess = (screen.textinput(title=f"{len(guessed_states)}/28 states correct", prompt="What are the states in India")
             .title())

    if guess in all_states:
        guessed_states.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(guess)

    if guess == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

screen.exitonclick()

