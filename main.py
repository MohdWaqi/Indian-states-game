import turtle
import pandas

########################### Setting up the screen ##################################

screen = turtle.Screen()
screen.setup(width=650, height=750)
screen.addshape("Picture1 - Copy.gif")
image = turtle.shape("Picture1 - Copy.gif")
# def click(x, y):
#     print(x, y)
#
#
# screen.onscreenclick(click)
# screen.mainloop()

##################################### Reading the data from states.csv #########################

data = pandas.read_csv("states.csv")
all_states = data.states.to_list()
guessed_states = 0
guessed_list = []
should_continue = True

while should_continue:
    user = (
        screen.textinput(title=f"{guessed_states}/36 Guess the state", prompt="What's the name of the state?")).title()
    if user in all_states:
        guessed_states += 1
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()

        ###################### showing the state name on map if guessed correctly #####################

        position = data[data.states == user]
        state.setposition(int(position.x), int(position.y))
        state.write(arg=f"{user}")
        guessed_list.append(user)
    if user == "Off" or guessed_states == 36:
        should_continue = False
not_guessed = [state for state in all_states if state not in guessed_list]
learn = pandas.DataFrame(not_guessed)
learn.to_csv("states_to_learn")

screen.exitonclick()
