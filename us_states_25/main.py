import turtle
import pandas as pd

#
data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()

def return_state_coordinates(state_name):
    """
    Take the states name, and returns the coordinates by looking up a
    pandas dataframe.
    :param state_name: Name of a US State
    :return: Returns x, y cooridinates as a tuple
    """
    x_list = data[data.state == new_state_name].x.tolist()
    y_list = data[data.state == new_state_name].y.tolist()
    if len(x_list) > 0 and len(y_list) > 0:
        return x_list[0], y_list[0]
    return None


IMAGE = 'blank_states_img.gif'
screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

correct_states = []


attempts = 50
for i in range(50):
    answer_state = screen.textinput(title=f"Guess the state {i}/{attempts}", prompt="State Name")
    name_list = answer_state.strip().split(' ')
    name_list_2 = [name.capitalize() for name in name_list]
    new_state_name = " ".join(name_list_2)
    if new_state_name == 'Q':
        missing_states = [state for state in all_states if state not in correct_states]
        missing_states_df = pd.DataFrame(missing_states)
        missing_states_df.to_csv("states_to_learn.csv")
        break
    coordinates = return_state_coordinates(new_state_name)
    if coordinates is not None:
        writer.goto(coordinates)
        writer.write(answer_state, move=False, align="Center")
        if new_state_name not in correct_states:
            correct_states.append(new_state_name)

new_df = pd.DataFrame(correct_states)
new_df.to_csv('learnt_states.csv')

screen.exitonclick()