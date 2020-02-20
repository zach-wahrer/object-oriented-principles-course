from random import randint
from turtle import Turtle


def create_turtle(name, color, shape, turtles_dict):
    turtles_dict[name] = Turtle()
    turtles_dict[name].color(color)
    turtles_dict[name].shape(shape)


def goto_loc(name, location, turtles_dict):
    turtles_dict[name].penup()
    turtles_dict[name].goto(location)
    turtles_dict[name].pendown()


def main():
    turtles = [
        ('sarah', 'pink', 'turtle', (-160, 100)),
        ('zach', 'blue', 'turtle', (-160, 70)),
        ('twoie', 'black', 'turtle', (-160, 40)),
        ('lulu', 'green', 'turtle', (-160, 10))
    ]

    turtles_dict = {}

    for name, color, shape, start_loc in turtles:
        create_turtle(name, color, shape, turtles_dict)
        goto_loc(name, start_loc, turtles_dict)

    for movement in range(200):
        for racer in turtles_dict.keys():
            turtles_dict[racer].forward(randint(1, 5))

    input('Press Enter to close')


if __name__ == "__main__":
    main()
