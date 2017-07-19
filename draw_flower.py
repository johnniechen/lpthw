import turtle

def draw_flower():
    window = turtle.Screen()
  
 
    for i in range(0,36):
        turtle.shape("turtle")
        turtle.forward(100)
        turtle.right(30)
        turtle.forward(100)
        turtle.right(120)
        turtle.speed(20)
    turtle.exitonclick()

draw_flower()
