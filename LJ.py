from graphics import *
from time import sleep

def calcLJForce(r, s, e):
	return 48 * e * ( ((pow(s,12))/(pow(r,13))) - 0.5 * (pow(s,6)/pow(r,7)) )

win = GraphWin("Lennard-Jones Potential Simulation",width = 1000, height = 1000) # create a window
win.setCoords(0, 0, 10000, 10000) # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)

x1 = 10000/2 - 3500
x2 = 10000/2 + 3500
v1 = 0
v2 = 0
molecule1 = Circle(Point(x1, 10000/2), 300)
molecule2 = Circle(Point(x2, 10000/2), 300)
molecule1.setFill("red")
molecule2.setFill("blue")
molecule1.draw(win) # draw it to the window
molecule2.draw(win)
message = Text(Point(10000/2, 3 * 10000/4), "Lennard-Jones Force Simulation")
message.setTextColor("black")
message.setSize(30)
message.setStyle("bold")
message.draw(win)

#win.close()

# SET UP LJ PARAMETERS
sigma = 1000
epsilon = 1e5
dt = 0.08
damp = 0.01
dampEff = 0

sleep(15)

while (True):
	# get LJ force
	r = x2 - x1
	force = calcLJForce(r, sigma, epsilon) + damp * v1
	print(force)

	# if there is little motion
	if (abs(force) < 1e-6):
		break
	# update velocities
	v1 = v1 - (force) * dt
	v2 = v2 + (force) * dt
	# update positions
	x1 = x1 + v1 * dt
	x2 = x2 + v2 * dt
	#x1 -= 0.5 * force * dt * dt
	#x2 += 0.5 * force * dt * dt

	molecule1.move(v1 * dt, 0)
	molecule2.move(v2 * dt, 0)
	dampEff += damp

print("I'M OUTTA HERE")
print ("r = ", x2-x1)
message = Text(Point(10000/2,10000/4), "Finished! Relaxed molecule distance: " + str(r))
message.setTextColor("green")
message.draw(win)
win.getMouse() # pause before closing