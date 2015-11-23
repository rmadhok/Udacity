import turtle

def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_triangle(some_turtle):
	for i in range(1,4):
		some_turtle.forward(100)
		some_turtle.left(120)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
	
	#Create turtle called Raahil
	raahil = turtle.Turtle()
	raahil.shape("turtle")
	raahil.color("turquoise")
	raahil.speed(7)
	for i in range(1,36):
		draw_square(raahil)
		raahil.right(10)
	
	#Create Maya turtle -- makes circle
	#maya = turtle.Turtle()
	#maya.shape("arrow")
	#maya.color("blue")
	#maya.circle(100)

	#create dude turtle -- makes triangle
	#dude = turtle.Turtle()
	#dude.shape("triangle")
	#dude.color("black")
	#draw_triangle(dude)

	window.exitonclick()
	
draw_art()