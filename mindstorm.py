import turtle

def draw_triangle(some_turtle):
    for i in range(1,4):
        some_turtle.forward(100)
        some_turtle.right(120)
    

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.speed(2)
    brad.color("yellow")
    brad.shape("turtle")
    for i in range(1,37):
        draw_triangle(brad)
        brad.right(10)

    window.exitonclick()


draw_art()



