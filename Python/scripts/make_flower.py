import turtle

def make_petal(petal):
	for i in range(1,2):
		petal.forward(100)
    	petal.left(45)
    	petal.forward(100)
    	petal.left(135)
 
def draw_flower():   
	window = turtle.Screen()
	window.bgcolor("red")
	
	flower = turtle.Turtle()
	flower.shape("arrow")
	flower.color("yellow")
	flower.speed(2)
	make_petal(flower)
	petals = 36
	turn = 360/petals
	for i in range(1, petals):
		make_petal(flower)
		flower.left(turn)
		
	window.exitonclick()
	
draw_flower()