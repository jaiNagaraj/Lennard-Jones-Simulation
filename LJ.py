from graphics import *
from time import sleep

def calcLJForce(r, s, e):
	return 48 * e * ( ((pow(s,12))/(pow(r,13))) - 0.5 * (pow(s,6)/pow(r,7)) )

win = GraphWin("Lennard-Jones Potential Simulation",width = 1000, height = 1000)
WINDOW_WIDTH = 10000
WINDOW_HEIGHT = 10000
PARTICLE_OFFSET = 3500
CIRCLE_RADIUS = 300
win.setCoords(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

x1 = WINDOW_WIDTH/2 - PARTICLE_OFFSET
x2 = WINDOW_WIDTH/2 + PARTICLE_OFFSET
v1 = 0
v2 = 0
molecule1 = Circle(Point(x1, WINDOW_HEIGHT/2), CIRCLE_RADIUS)
molecule2 = Circle(Point(x2, WINDOW_HEIGHT/2), CIRCLE_RADIUS)
molecule1.setFill("red")
molecule2.setFill("blue")
molecule1.draw(win)
molecule2.draw(win)
message = Text(Point(WINDOW_WIDTH/2, 3 * WINDOW_HEIGHT/4), "Lennard-Jones Force Simulation")
message.setTextColor("black")
message.setSize(30)
message.setStyle("bold")
message.draw(win)

# SET UP LJ PARAMETERS
sigma = 1000
epsilon = 1e5
dt = 0.08
damp = 0.01
tolerance = 1e-6

while (True):
	# get LJ force
	r = x2 - x1
	force = calcLJForce(r, sigma, epsilon) + damp * v1

	# if there is negligible motion
	if (abs(force) < tolerance):
		break
	# update velocities
	v1 -= (force) * dt
	v2 += (force) * dt
	# update positions
	x1 += v1 * dt
	x2 += v2 * dt

	molecule1.move(v1 * dt, 0)
	molecule2.move(v2 * dt, 0)

message = Text(Point(WINDOW_WIDTH/2,WINDOW_HEIGHT/4), "Finished! Relaxed molecule distance: " + str(r))
message.setTextColor("green")
message.draw(win)
win.getMouse() # pause before closing