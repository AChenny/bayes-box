from tkinter import *
import math

p_left = 0.50 #P(E|H)
p_middle = 0.50 #P(H)
p_right = 0.50 #P(E|Not-H)
lastPressedX = 0
lastPressedY = 0
TOTALHEIGHT = 300
TOTALWIDTH = 600
pressed_leftBox = False
pressed_rightBox = False
pressed_middleLine = False
root = Tk()

#TODO: Export py file to exe
#FIXME: p_middle is actually p(not-h)
#TODO: Make the bayesian box smaller and put it to the right side of the window

def main():
	root.title("Bayesian Confirmation")
	canvas = Canvas(root, width=1200, height=625)
	#800 width on the right - bayes box
	#400 width on the left - pi chart
	canvas.pack()
	can_middle_line = canvas.create_line(350, 160, 350, 625, width=5)
	canvas.create_line(0, 160, 1200, 160, width = 5)
	#Formula
	#Entry1 = P(E|H)
	#Entry2 = P(H)
	#Entry3 = P(E|NOT-H)

	#TODO: Create a new formula inside Canvas that is bigger than it is now. (Should be the main focus, make as big as possible)
	canvas.create_text(330, 90, text="P", font= ("Calibri", 23, "bold italic"))
	canvas.create_text(398, 90, text="|     =", font=("Calibri", 23, "bold"), fill="black")
	canvas.create_text(378, 90, text="(H E)  ", font= ("Calibri", 23))

	c_entry1 = Entry(canvas, font=("Calibri", 20, "bold"))
	canvas.create_window(545, 65, window = c_entry1, width= 60)
	c_entry2 = Entry(canvas, font=("Calibri", 20, "bold"))
	canvas.create_window(655, 65, window = c_entry2, width= 60)
	c_label2 = Label(canvas, text = "x", font=("Calibri", 20))
	canvas.create_window(600, 68, window= c_label2)
	c_label3 = Label(canvas, text="SAA + (", font=("Calibri", 20))
	canvas.create_window(505, 115, window = c_label3)
	c_entry3 = Entry(canvas, font=("Calibri", 20, "bold"))
	canvas.create_window(590, 115, window = c_entry3, width=60)

	text3_var = StringVar()
	c_label4 = Label(canvas, textvariable=text3_var, font=("Calibri", 20))
	canvas.create_window(685, 115, window = c_label4)

	text4_var = StringVar()
	c_label5 = Label(canvas, textvariable=text4_var, font=("Calibri", 30, "bold"))
	canvas.create_window(825, 90, window= c_label5)
	canvas.create_line(460, 90, 740, 90, width = 5)

	

	#Labels on canvas
	#P(E|H)
	canvas.create_text(380, 370, text="P", font= ("Calibri", 15, "bold italic"))
	canvas.create_text(406, 370, text="|", font=("Calibri", 15, "bold"), fill="black")
	canvas.create_text(410, 370, text="(E H) ", font= ("Calibri", 15))
	leftLabel = canvas.create_text((400, 405), font=("Purisa", 15), text='=\n{0:.2f}'.format(p_left), justify=CENTER)

	#P(E|NOT-H)
	canvas.create_text(1082, 370, text="P", font= ("Calibri", 15, "bold italic"))
	canvas.create_text(1108, 370, text="|", font=("Calibri", 15, "bold"), fill="black")
	canvas.create_text(1130, 370, text="(E Not-H) ", font= ("Calibri", 15))
	rightLabel = canvas.create_text((1115, 405), font=("Purisa", 15), text='=\n{0:.2f}'.format(p_right, justify=CENTER))

	#P(H)
	canvas.create_text(708, 580, text="P", font= ("Calibri", 15, "bold italic"))
	canvas.create_text(730, 580, text="(H) ", font= ("Calibri", 15))
	middleLabel = canvas.create_text((773, 580), font=("Purisa", 15), text=' = {0:.2f}'.format(p_middle))

	believeLabel = canvas.create_text((75, 500), font=("Calibri", 17, "bold"), text="BELIEVE", fill="grey")
	disbelieveLabel = canvas.create_text((75, 550), font=("Calibri", 17, "bold"), text="DISBELIEVE", fill="grey")
	confirmationLabel = canvas.create_text((240, 500), font=("Calibri", 17, "bold"), text="CONFIRMATION", fill="grey")
	disconfirmationLabel = canvas.create_text((240, 550), font=("Calibri", 17, "bold"), text="DISCONFIRMATION", fill="grey")

	widgets = [c_entry1, c_entry2, c_entry3, text3_var, text4_var, leftLabel, rightLabel, middleLabel, believeLabel, disbelieveLabel, confirmationLabel, disconfirmationLabel]

	#Init beginning boxes
	# left_rect = [500, 350, 800, 500]
	# right_rect = [800, 350, 1100, 500]
	# middle_line = 800
	left_rect = [450, 400, 750, 550]
	right_rect = [750, 400, 1050, 550]
	middle_line = 750
	draw(canvas, left_rect, right_rect, middle_line, widgets)
	
	canvas.bind("<Button-1>", lambda event: leftClick(event, canvas))
	canvas.bind("<Motion>", lambda event: changeCursor(event, root, canvas))
	root.bind("<Return>", lambda event: updateButtonPress(canvas, widgets))
	canvas.bind("<B1-Motion>", lambda event: leftRelease(event, canvas, widgets))
	root.mainloop()

#On presses check if it hits any of the sides with this function
def leftClick(event, canvas):
	x = event.x
	y = event.y
	leftBox = canvas.coords("left_rect")
	rightBox = canvas.coords("right_rect")
	left_width = leftBox[2] - leftBox[0]
	right_width = rightBox[2] - rightBox[0]

	global lastPressedX
	global lastPressedY
	global pressed_leftBox 
	global pressed_rightBox
	global pressed_middleLine
	lastPressedX = event.x
	lastPressedY = event.y
	pressed_leftBox = False
	pressed_rightBox = False
	pressed_middleLine = False

	#If this is true, then set a global that user has pressed the left box to go vertically
	if leftBox[0] < x <= leftBox[0] + left_width and leftBox[1] - 10 <= y <= leftBox[1]:
		pressed_leftBox = True

	#Check if it hit right box
	elif rightBox[0] < x <= rightBox[0] + right_width and rightBox[1] - 10 <= y <= rightBox[1]:
		pressed_rightBox = True

	elif leftBox[2] - 5 <= x <= leftBox[2] + 5 and 100 <= y <= 500:
		pressed_middleLine = True

#Line release will only do something if something is selected to be moved which will be determined by the mouse press
def leftRelease(event, canvas, widgets):
	global lastPressedX
	global lastPressedY

	leftBox = canvas.coords("left_rect")
	rightBox = canvas.coords("right_rect")
	middleLine = canvas.coords("middle_line")


	vertical_movement = lastPressedY - event.y
	vert_pct_move = (vertical_movement / 3) / 100
	horizontal_movement = lastPressedX - event.x
	hort_pct_move = (horizontal_movement / 6) / 100

	if pressed_leftBox == True:
		global p_left 
		p_left += vert_pct_move
		if p_left >= 1: 
			p_left = 1
		elif p_left <= 0:
			p_left = 0
		leftHeight = TOTALHEIGHT * (1-p_left) + 250
		#leftHeight = TOTALHEIGHT * (1-p_left) + 200
		new_left = [leftBox[0], leftHeight, leftBox[2], leftBox[3]]
		draw(canvas, new_left, rightBox, middleLine[0], widgets)

	elif pressed_rightBox == True:
		global p_right
		p_right += vert_pct_move
		if p_right >= 1: 
			p_right = 1
		elif p_right <= 0:
			p_right = 0
		rightHeight = TOTALHEIGHT * (1-p_right) + 250
		#rightHeight = TOTALHEIGHT * (1-p_right) + 200
		new_right = [rightBox[0], rightHeight, rightBox[2], rightBox[3]]
		draw(canvas, leftBox, new_right, middleLine[0], widgets)

	elif pressed_middleLine == True:
		global p_middle
		p_middle += hort_pct_move
		if p_middle >= 1: 
			p_middle = 1
		elif p_middle <= 0:
			p_middle = 0
		new_middle = TOTALWIDTH * (1-p_middle) + 450
		new_left = [leftBox[0], leftBox[1], new_middle, leftBox[3]]
		new_right = [new_middle, rightBox[1], rightBox[2], rightBox[3]]
		draw(canvas, new_left, new_right, new_middle, widgets)

	lastPressedX = event.x
	lastPressedY = event.y


#Draws everything on the screen with values
def draw(canvas, leftBox, rightBox, middleLine, widgets):
	canvas.delete("left_rect")
	canvas.delete("right_rect")
	canvas.delete("middle_line")
	canvas.delete("pi1")
	canvas.delete("pi2")
	canvas.delete("pi_h")
	canvas.create_rectangle(leftBox[0], leftBox[1], leftBox[2], leftBox[3], fill="#00CC00", tags="left_rect", width=5)
	canvas.create_rectangle(rightBox[0], rightBox[1], rightBox[2], rightBox[3], fill="#3333FF", tags="right_rect", width=5)
	canvas.create_line(middleLine, 250, middleLine, 550, width=5, fill="red", tags="middle_line")

	canvas.itemconfigure(widgets[5], text='=\n{0:.2f}'.format(round(p_left, 2)), justify=CENTER)
	canvas.itemconfigure(widgets[6], text='=\n{0:.2f}'.format(round(p_right, 2)), justify=CENTER)
	canvas.itemconfigure(widgets[7], text='= {0:.2f}'.format(round(1-p_middle,2)))

	#Pi chart test
	canvas.create_oval((75,200,275,400), fill="#3333FF", tags="pi1")
	#every 3.6 added to the extent is another %
	#P(H|E) % is the extent
	try:
		p_he = (p_left * (1-p_middle)) / ((p_left * (1-p_middle)) + (p_right * (p_middle)))
	except ZeroDivisionError:
		p_he = 0

	pi_degree = p_he * 360
	if pi_degree == 360:
		pi_degree = 359.9
	canvas.create_arc((75,200,275,400), fill="#00CC00", extent= (-pi_degree), tags="pi2", start=90)

	print(round(p_he, 3))

	#PI CHART P(H)
	pi_r = 110
	pi_angle = (360 * p_middle)-180
	pi_x = pi_r * math.sin(math.radians(pi_angle))
	pi_y = pi_r * math.sin(math.radians(90-pi_angle))
	canvas.create_line(175, 300, pi_x+175, pi_y+300, width = 3, tags="pi_h", fill="red")

	#FIXME: p_he values have to be too precise for it to be both greyed out
	print("p_he: " + str(round(p_he,3)) + "| p_middle: " + str(round(1-p_middle,3)))

	if round(p_he, 2) == 0.50:
		canvas.itemconfigure(widgets[8], fill="grey")
		canvas.itemconfigure(widgets[9], fill="grey")
		
	elif p_he > 0.50:
		canvas.itemconfigure(widgets[8], fill="black")
		canvas.itemconfigure(widgets[9], fill="grey")
	elif p_he < 0.50: 
		canvas.itemconfigure(widgets[9], fill="black")
		canvas.itemconfigure(widgets[8], fill="grey")

	if round(p_he, 2) == (round(1-p_middle, 2)):
		canvas.itemconfigure(widgets[10], fill="grey")
		canvas.itemconfigure(widgets[11], fill="grey")
		
	elif round(p_he, 2) > (round(1-p_middle, 2)):
		canvas.itemconfigure(widgets[10], fill="black")
		canvas.itemconfigure(widgets[11], fill="grey")
	elif round(p_he, 2) < (round(1-p_middle, 2)):
		canvas.itemconfigure(widgets[11], fill="black")
		canvas.itemconfigure(widgets[10], fill="grey")


	create_open_rectangle(canvas, 450, 250, 1050, 550)
	# create_open_rectangle(canvas, 200, 180, 1000, 580)
	widgets[0].delete(0, END)
	widgets[0].insert(0, "{0:.2f}".format(p_left))

	#P(E|NOT-H)
	widgets[2].delete(0, END)
	widgets[2].insert(0, "{0:.2f}".format(p_right))

	#P(H)
	widgets[1].delete(0, END)
	widgets[1].insert(0, "{0:.2f}".format(1-p_middle))

	widgets[3].set('x  {0:.2f}  )'.format(p_middle))


	widgets[4].set('=  {0:.2f}'.format(p_he))

def create_open_rectangle(canvas, x1, y1, x2, y2):
	canvas.delete("box1")
	canvas.delete("box2")
	canvas.delete("box3")
	canvas.delete("box4")
	canvas.create_line(x1-2, y1, x2+3, y1, width = 5, tags="box1")
	canvas.create_line(x2, y1, x2, y2, width = 5, tags="box2")
	canvas.create_line(x2, y2, x1, y2, width = 5, tags="box3")
	canvas.create_line(x1, y2, x1, y1, width = 5, tags="box4")

def updateButtonPress(canvas, widgets):
	#init global percentages, then set them as the entry values

	print("ENTER BUTTON")

	global p_left
	global p_middle
	global p_right
	p_left = float(widgets[0].get())
	p_middle = 1-(float(widgets[1].get()))
	p_right = float(widgets[2].get())

	#MINMAX VALUES 
	if p_left >= 1: 
		p_left = 1
	elif p_left <= 0:
		p_left = 0

	if p_middle >= 1: 
		p_middle = 1
	elif p_middle <= 0:
		p_middle = 0

	if p_right >= 1: 
		p_right = 1
	elif p_right <= 0:
		p_right = 0

	#Redraw rectangles after getting new values from the entries
	middle = TOTALWIDTH * (1-p_middle) + 450
	leftHeight = TOTALHEIGHT * (1-p_left) + 250
	rightHeight = TOTALHEIGHT * (1-p_right) + 250

	left_rect = [450, leftHeight, middle, 550]
	right_rect = [middle, rightHeight, 1050, 550]

	draw(canvas, left_rect, right_rect, middle, widgets)

#Change cursor on motion over drag-able areas
def changeCursor(event, root, canvas):
	leftBox = canvas.coords("left_rect")
	rightBox = canvas.coords("right_rect")
	left_width = leftBox[2] - leftBox[0]
	right_width = rightBox[2] - rightBox[0]

	x = event.x
	y = event.y

	if leftBox[0] < x <= leftBox[0] + left_width and leftBox[1] - 10 <= y <= leftBox[1]:
		root.config(cursor='sb_v_double_arrow')

	elif rightBox[0] < x <= rightBox[0] + right_width and rightBox[1] - 10 <= y <= rightBox[1]:
		root.config(cursor='sb_v_double_arrow')

	elif leftBox[2] - 5 <= x <= leftBox[2] + 5 and 200 <= y <= 500:
		root.config(cursor='sb_h_double_arrow')
	else: 
		root.config(cursor="")

main()








