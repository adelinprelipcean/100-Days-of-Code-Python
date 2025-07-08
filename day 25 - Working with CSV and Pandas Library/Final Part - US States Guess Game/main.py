import turtle
import pandas

screen = turtle.Screen()
screen.setup(730, 500)
screen.title("US States Quiz Game")

screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
screen.tracer(0)

states = pandas.read_csv("50_states.csv")
score = 0
not_guessed_states = states["state"].tolist()

while(score <= 50):
    answer = screen.textinput(title="Guess the State", prompt=f"Score: {score}")
    if answer == 'exit':
        (pandas.DataFrame(data={'Not Guessed States':[state for state in not_guessed_states]})).to_csv("not_guessed_states.csv")
        break
    try:
        turtle.teleport(int(states.x[states["state"].str.lower() == answer.lower()]), int(states.y[states["state"].str.lower() == answer.lower()]))
        turtle.write(f"{answer.capitalize()}")
        not_guessed_states.remove((states.state[states.state.str.lower() == answer.lower()]).to_string().strip(" 1234567890"))
        score += 1
    except:
        print("NOT FOUND")

