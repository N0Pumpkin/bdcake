import turtle as t
import math
Length_of_legs = 5
Width_of_legs = 50
def set_coordinates(x,y):
    t.up()
    t.goto([x,y])
    t.down()
def square(len, border, bor_size, fill):
    t.pensize(bor_size)                                                             #set the size of the pen
    t.pencolor(border)                                                              #set the color of the pen
    t.fillcolor(fill)                                                               #set the color of the inside of shape
    t.begin_fill()                                                                  #keep track of shape
    t.forward(len)                                                                  #draws a line of "length" length
    t.left(90)                                                                      #turn turtle left on 90
    t.forward(len)
    t.left(90)
    t.forward(len)
    t.left(90)
    t.forward(len)
    t.left(90)
    t.end_fill()
def circle(r, border, bor_size, fill):
    t   .pencolor(border)                                                           #set color of pen
    t.pensize(bor_size)                                                             #set size of pen
    t.fillcolor(fill)                                                               #set color inside of the shape
    t.begin_fill()                                                                  #keep track of the shape
    t.circle(r,360)                                                                 #Draws circle with radius "r"
    t.end_fill()                                                                    #fills the shape
def rectangle(len,width,border_size,border_color,fill_color):
    t.pensize(border_size)                                                          #set the size of the pen
    t.pencolor(border_color)                                                        #set the color of the pen
    t.fillcolor(fill_color)                                                         #set the color of the inside of shape
    t.begin_fill()                                                                  #keep track of shape
    t.forward(len)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(len)
    t.left(90)
    t.forward(width)
    t.end_fill()
def layer_function(length,width,color):
    t.setheading(0)
    rectangle(length, width, 2, color,color)                                        #creates one side of the one of the layer of the cake
    t.left(270)
    rectangle(length,-width,2,color,color)                                          #draws mirror side of the layer of the cake
def teardrop(size,border_size, color):
    t.pencolor(color)                                                               #setting the colors of color
    t.fillcolor(color)
    t.pensize(border_size)
    t.begin_fill()                                                                  #keep track of the shape
    t.circle(size, 180)                                                             # Draw the upper semi-circle
    t.setheading(0)
    t.circle(size/2,-180)                                                           # Draw the another semi-circle but smaller
    t.end_fill()                                                                    #fills the shape
def candle(size):
    t.setheading(0)
    rectangle(size,40,3,'White','White')
    xcor = t.xcor()
    ycor = t.ycor()
    set_coordinates(xcor,ycor+45)
    teardrop(5,1,'yellow')
def decoration(size):
    t.fillcolor("LightCoral")
    t.pencolor("LightCoral")
    t.pensize(2)
    t.begin_fill()
    #Creates a 5 waves as a decoration if we would have passed loops I would have used loop.
    t.setheading(-90)
    t.circle(size,180)
    t.setheading(-90)
    t.circle(size,180)
    t.setheading(-90)
    t.circle(size,180)
    t.setheading(-90)
    t.circle(size,180)
    t.setheading(-90)
    t.circle(size,180)
    t.setheading(180)
    t.forward(size*5*2)                                                             # draw a line that connects them in order to fill
    t.end_fill()
def main():
    t.speed(50)
    t.bgcolor("Aqua")

    #This part creates table
    color_of_table = input("Please specify the color of the table: ")               #user specify the color of the table
    length_of_table = int(input("Please specify the length of the table: "))        #user specify the length of the table
    rectangle(length_of_table,15,4,color_of_table,color_of_table)                   #draw the right side of the table
    t.left(270)
    rectangle(length_of_table,-15,4,color_of_table,color_of_table)                  #draw the mirror side of the table
    #This part creating legs
    coordinate_of_legs = length_of_table/2
    set_coordinates(coordinate_of_legs,0)                                           #setting the coordinate for the first leg
    t.left(90)
    rectangle(Length_of_legs, Width_of_legs, 5,color_of_table,color_of_table)       #draw the leg
    set_coordinates(length_of_table,0)                                              #setting the coordinate for the Second leg
    t.left(90)
    rectangle(Length_of_legs, Width_of_legs, 5,color_of_table,color_of_table)       #draw the leg
    set_coordinates(-coordinate_of_legs,0)                                          #setting the coordinate for the third leg
    t.left(90)
    rectangle(Length_of_legs, Width_of_legs, 5,color_of_table,color_of_table)       #draw the leg
    set_coordinates(-length_of_table,0)                                             #setting the coordinate for the fourth leg
    t.left(90)
    rectangle(-Length_of_legs, Width_of_legs, 5,color_of_table,color_of_table)      #draw the leg
    #This part create cake
    size_of_cake = int(input("What is the size of the cake, Please provide the number smaller than size of the table: "))
    set_coordinates(0,15)                                                           #put turtle on top of the table
    layer_function(size_of_cake,10,'red')                                           #create a red layer
    set_coordinates(0,25)                                                           #setting the position on top of the first layer
    layer_function(size_of_cake,15,'chocolate')                                     #create a chocolate layer
    set_coordinates(0,40)                                                           #put turtle on top of the second layer
    layer_function(size_of_cake,20,'yellow')                                        #draws the yellow layer
    set_coordinates(0,60)                                                           #put the turtle at the top of the cake
    layer_function(size_of_cake,25,'Dark red')
    set_coordinates(0,89)
    t.setheading(0)
    circle(size_of_cake/7,'Gold',5,"Gold")
    t.setheading(0)
    set_coordinates(size_of_cake/2,85)
    candle(2)
    set_coordinates(-size_of_cake/2,85)
    candle(2)
    set_coordinates(-size_of_cake,85)
    decoration(size_of_cake/5)
    set_coordinates(200,200)
    t.exitonclick()
main()
