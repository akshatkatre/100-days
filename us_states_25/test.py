import pandas as pd

data = pd.read_csv('50_states.csv')


def return_state_coordinates(state_name):
    name_list = state_name.strip().split(' ')
    name_list_2 = [name.capitalize() for name in name_list]
    state_name = " ".join(name_list_2)
    print(state_name)
    x_list = data[data.state == state_name].x.tolist()
    y_list = data[data.state == state_name].y.tolist()
    if len(x_list) > 0 and len(y_list) > 0:
        return x_list[0], y_list[0]
    return None


print(return_state_coordinates('Alabama'))
print(return_state_coordinates('new york'.capitalize()))