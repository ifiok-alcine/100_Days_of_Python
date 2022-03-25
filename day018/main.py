# # Code to get the colour from a damian hirst image using colorgram.
# import colorgram
#
# colours = colorgram.extract('image.jpg', 30)
# rgb_colour = []
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     rgb_colour.append(new_colour)
#
# print(rgb_colour)
import random
import turtle

turtle.colormode(255)
colour_list = [(197, 165, 119), (144, 81, 56), (220, 201, 138), (61, 95, 121), (165, 150, 54), (136, 162, 180),
               (131, 34, 23), (52, 119, 87), (73, 37, 29), (190, 96, 82), (145, 177, 150), (100, 76, 80),
               (165, 147, 157), (21, 92, 68), (28, 59, 75), (225, 177, 167), (59, 44, 46), (133, 29, 33),
               (180, 202, 179), (26, 84, 89), (88, 147, 129), (13, 70, 58), (42, 65, 89), (180, 99, 102),
               (216, 181, 186), (182, 191, 204)]

ace = turtle.Turtle()
ace.penup()
ace.hideturtle()
ace.speed("fastest")
ace.setheading(225)
ace.forward(300)
ace.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    ace.dot(20, random.choice(colour_list))
    ace.forward(50)

    if dot_count % 10 == 0:
        ace.setheading(90)
        ace.forward(50)
        ace.setheading(180)
        ace.forward(500)
        ace.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
