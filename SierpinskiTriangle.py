import turtle

def draw():
    #Initializes everything and draws a shape, in this case, a fractal

    #Receives as input various values
    triangle_length = float(raw_input("Length of Individual Triangle: "))
    complexity = float(raw_input("Complexity: ")) - 1
    y_coord = float(raw_input("Y-coordinate of the top of the fractal: "))
    
    #Initialize window
    window = turtle.Screen()
    
    #Initialize turtle
    me = turtle.Turtle()
    me.shape("turtle")
    me.pencolor("#000066")
    me.speed(0)
    me.width(1)
    me.fillcolor("#3DD91E")
    
    #Position turtle
    me.penup()
    me.goto(0, y_coord)
    me.pendown()
    me.right(60)


    #Draw Fractal
    drawFractal(me, triangle_length, complexity)

    #Exit on click
    window.exitonclick()


def drawFractal(turtle, triangle_length, complexity):
    #Uses recursion to loop an arbitrary number of times, using different numbers each time, enabling it to create a fractal of an arbitrary complexity
    for i in range(0, 3):
        """Move the fractal complexity down a level and draw that and then draw a side of the current fractal"""
        #Moves a specific amount forward depending on what level of the fractal it is on. This is a relationship involving simply various powers of 2
        turtle.forward(triangle_length * (2 ** complexity)) 
        if complexity == 0:
            drawTriangle(turtle, triangle_length)
        else:
            drawFractal(turtle, triangle_length, complexity - 1)
        turtle.forward(triangle_length * (2 ** complexity))
        turtle.right(120)
            
    
def drawTriangle(turtle, triangle_length):
    #Draws a triangle with a green fill, and ends with the turtle at the starting position facing the same direction
    i = 0
    turtle.begin_fill()
    while i < 3:
        turtle.forward(triangle_length)
        turtle.right(120)
        i += 1
    turtle.end_fill()  
        
#Draw Fractal
draw()
