from tkinter import *

p_left = 0.50 #P(E|H)
p_middle = 0.50 #P(H)
p_right = 0.50 #P(E|Not-H)
lastPressedX = 0
lastPressedY = 0
TOTALHEIGHT = 400
TOTALWIDTH = 800
pressed_leftBox = False
pressed_rightBox = False
pressed_middleLine = False
root = Tk()

#TODO: Export py file to exe
#FIXME: p_middle is actually p(not-h)

def main():
	root.title("Bayesian Confirmation")
	canvas = Canvas(root, width=1200, height=625)
	canvas.pack()

	#Formula
	#Entry1 = P(E|H)
	#Entry2 = P(H)
	#Entry3 = P(E|NOT-H)
	formulaFrame = Frame(root)
	leftside = Frame(formulaFrame)
	lbl = Label(leftside, text= "P(H|E)=")
	lbl.pack(anchor='c')
	leftside.pack(side=LEFT)

	rightside = Frame(formulaFrame)

	numerator = Frame(rightside)
	entry1 = Entry(numerator, width=5)
	
	entry1.pack(side=LEFT)
	lbl = Label(numerator, text='*')
	lbl.pack(side=LEFT)
	entry2 = Entry(numerator, width=5)
	entry2.pack(side=LEFT)
	numerator.pack()

	division_bar = Frame(rightside, bg='black', height=4)
	division_bar.pack(fill=X, expand=True)

	denominator = Frame(rightside)
	text2 = Label(denominator, text= "SAA + (")
	text2.pack(side=LEFT)
	entry3 = Entry(denominator, width=5)
	entry3.pack(side=LEFT)

	text3_var = StringVar()
	text3 = Label(denominator, textvariable=text3_var)
	text3.pack(side=LEFT)


	text4_var = StringVar()
	text4 = Label(formulaFrame, textvariable=text4_var, font=("Calibri", 15, "bold"))
	text5 = Label(formulaFrame, text="=")
	text4.pack(side=RIGHT)
	text5.pack(side=RIGHT)

	denominator.pack()
	rightside.pack(side=LEFT)

	formulaFrame.pack()

	#Labels on canvas
	leftLabel = canvas.create_text((125, 350), font=("Purisa", 15), text='P(E|H) \n[{0:.2f}]'.format(p_left))
	rightLabel = canvas.create_text((1100, 350), font=("Purisa", 15), text='P(E|NOT-H) \n[{0:.2f}]'.format(p_right))
	middleLabel = canvas.create_text((605, 605), font=("Purisa", 15), text='P(H) = [{0:.2f}]'.format(p_middle))

	believeLabel = canvas.create_text((375, 50), font=("Calibri", 30), text="BELIEVE", fill="grey")
	disbelieveLabel = canvas.create_text((375, 125), font=("Calibri", 30), text="DISBELIEVE", fill="grey")

	confirmationLabel = canvas.create_text((875, 50), font=("Calibri", 30), text="CONFIRMATION", fill="grey")
	disconfirmationLabel = canvas.create_text((875, 125), font=("Calibri", 30), text="DISCONFIRMATION", fill="grey")

	widgets = [entry1, entry2, entry3, text3_var, text4_var, leftLabel, rightLabel, middleLabel, believeLabel, disbelieveLabel, confirmationLabel, disconfirmationLabel]

	#Init beginning boxes
	left_rect = [200, 380, 600, 580]
	right_rect = [600, 380, 1000, 580]
	middle_line = 600
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
	vert_pct_move = (vertical_movement / 4) / 100
	horizontal_movement = lastPressedX - event.x
	hort_pct_move = (horizontal_movement / 8) / 100

	if pressed_leftBox == True:
		global p_left 
		p_left += vert_pct_move
		if p_left >= 1: 
			p_left = 1
		elif p_left <= 0:
			p_left = 0
		leftHeight = TOTALHEIGHT * (1-p_left) + 180
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
		rightHeight = TOTALHEIGHT * (1-p_right) + 180
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
		new_middle = TOTALWIDTH * (1-p_middle) + 200
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
	canvas.create_rectangle(leftBox[0], leftBox[1], leftBox[2], leftBox[3], fill="red", tags="left_rect", width=10)
	canvas.create_rectangle(rightBox[0], rightBox[1], rightBox[2], rightBox[3], fill="blue", tags="right_rect", width=10)
	canvas.create_line(middleLine, 180, middleLine, 580, width=10, fill="black", tags="middle_line")

	canvas.itemconfigure(widgets[5], text='P(E|H) \n[{0:.2f}]'.format(p_left))
	canvas.itemconfigure(widgets[6], text='P(E|NOT-H) \n[{0:.2f}]'.format(p_right))
	canvas.itemconfigure(widgets[7], text='P(H) = [{0:.2f}]'.format(1-p_middle))

	#Pi chart test
	canvas.create_oval((525,15,675,165), fill="blue", tags="pi1")
	#every 3.6 added to the extent is another %
	#P(H|E) % is the extent
	try:
		p_he = (p_left * (1-p_middle)) / ((p_left * (1-p_middle)) + (p_right * (p_middle)))
	except ZeroDivisionError:
		p_he = 0

	pi_degree = p_he * 360
	if pi_degree == 360:
		pi_degree = 359.9
	canvas.create_arc((525,15,675,165), fill="red", extent= pi_degree, tags="pi2", start=90)

	if p_he > 0.50:
		canvas.itemconfigure(widgets[8], fill="black")
		canvas.itemconfigure(widgets[9], fill="grey")
	elif p_he < 0.50: 
		canvas.itemconfigure(widgets[9], fill="black")
		canvas.itemconfigure(widgets[8], fill="grey")
	else:
		canvas.itemconfigure(widgets[8], fill="grey")
		canvas.itemconfigure(widgets[9], fill="grey")

	if p_he > (1-p_middle):
		canvas.itemconfigure(widgets[10], fill="black")
		canvas.itemconfigure(widgets[11], fill="grey")
	elif p_he <  (1-p_middle):
		canvas.itemconfigure(widgets[11], fill="black")
		canvas.itemconfigure(widgets[10], fill="grey")
	else:
		canvas.itemconfigure(widgets[10], fill="grey")
		canvas.itemconfigure(widgets[11], fill="grey")


	create_open_rectangle(canvas, 200, 180, 1000, 580)
	widgets[0].delete(0, END)
	widgets[0].insert(0, "{0:.2f}".format(p_left))

	#P(E|NOT-H)
	widgets[2].delete(0, END)
	widgets[2].insert(0, "{0:.2f}".format(p_right))

	#P(H)
	widgets[1].delete(0, END)
	widgets[1].insert(0, "{0:.2f}".format(1-p_middle))

	widgets[3].set('* {0:.2f})'.format(p_middle))


	widgets[4].set('{0:.2f}'.format(p_he))

def create_open_rectangle(canvas, x1, y1, x2, y2):
	canvas.delete("box1")
	canvas.delete("box2")
	canvas.delete("box3")
	canvas.delete("box4")
	canvas.create_line(x1-5, y1, x2+5, y1, width = 10, tags="box1")
	canvas.create_line(x2, y1, x2, y2, width = 10, tags="box2")
	canvas.create_line(x2, y2, x1, y2, width = 10, tags="box3")
	canvas.create_line(x1, y2, x1, y1, width = 10, tags="box4")

def updateButtonPress(canvas, widgets):
	#init global percentages, then set them as the entry values

	print("ENTER BUTTON")

	global p_left
	global p_middle
	global p_right
	p_left = float(widgets[0].get())
	p_middle = float(widgets[1].get())
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
	middle = TOTALWIDTH * (1-p_middle) + 200 
	leftHeight = TOTALHEIGHT * (1-p_left) + 200 
	rightHeight = TOTALHEIGHT * (1-p_right) + 200

	left_rect = [200, leftHeight, middle, 580]
	right_rect = [middle, rightHeight, 1000, 580]

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

	elif leftBox[2] - 5 <= x <= leftBox[2] + 5 and 200 <= y <= 580:
		root.config(cursor='sb_h_double_arrow')
	else: 
		root.config(cursor="")

main()








