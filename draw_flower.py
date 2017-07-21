# Square Flower Program

from turtle import *

# Define Functions for Square and Flower

def Square():
    for i in range(4):
		forward(100)
		right(80)
		speed(20)

def FlowerSquare():
    for i in range(18):
		shape("turtle")
		color("blue")
		Square()
		right(20)
# Main Method
FlowerSquare()

def FlowerEnd():
    goto(0,0)
    right(90)
    forward(200)
    exitonclick()
FlowerEnd()
