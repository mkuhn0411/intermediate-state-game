import turtle
import pandas

screen = turtle.Screen()

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")
state_data = pandas.read_csv("50_states.csv")
all_states = state_data.state.to_list()
states_correct = []


def setup():
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)


def add_state(state, xcor, ycor):
    new_state = turtle.Turtle()
    new_state.up()
    new_state.hideturtle()
    new_state.goto(xcor, ycor)
    new_state.write(f"{state}")


def ask_user():
    correct_answer = None

    while not correct_answer:
        answer_state = screen.textinput(f"{len(states_correct)}/50 States Correct", "What's the state?").title()
        correct_state = state_data[state_data["state"] == answer_state]

        if answer_state.lower() == "exit":
            return

        if len(correct_state) > 0:
            add_state(answer_state, int(correct_state.x), int(correct_state.y))
            return answer_state


def generate_csv():
    # missing_states = list(filter(lambda s: s not in states_correct, all_states))
    missing_states = [s for s in all_states if s not in states_correct]

    missing_states_data = pandas.DataFrame(missing_states)
    missing_states_data.to_csv("states_to_learn.csv")


def run():
    setup()

    while len(states_correct) < 50:
        user_guess = ask_user()

        if user_guess is None:
            generate_csv()
            break
        else:
            states_correct.append(user_guess)


run()

