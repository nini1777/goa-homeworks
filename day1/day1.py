from turtle import*

#we want to paint a house

#step 1: draw a squere
shape("turtle")
#speed(30)
width(7)
color("purple")
begin_fill()
forward(200)
left(90)
end_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of spuare 

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)    #heigh of the door 
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

#drawing a roof
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window
color("blue")
penup()
goto(140,140)
pendown()


left(120)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

penup()
goto(20,140) 
pendown()

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)


exitonclick()