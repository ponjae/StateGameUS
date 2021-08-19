import turtle
import pandas

turtle_writer = turtle.Turtle()
turtle_writer.hideturtle()
screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()


while len(states) > 0:
    states_left = len(states)
    correct = 50 - states_left
    answer = screen.textinput(title=f"{correct}/50 correct so far",
                              prompt="Please name a valid state in the US")
    answer = answer.capitalize()
    if answer == 'Exit':
        # Exit and create a csv containing states that were missed
        new_data = pandas.DataFrame(states)
        new_data.to_csv("missed_states.csv")
        break

    if answer in states:
        row_data = data[data["state"] == answer]
        turtle_writer.penup()
        turtle_writer.goto((int(row_data.x), int(row_data.y)))
        turtle_writer.pendown()
        turtle_writer.write(answer)
        states.remove(answer)
