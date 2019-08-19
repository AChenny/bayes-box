from tkinter import *
import math
import formula
import label

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

color1 = "#90FF93" #P(E|H) green
color2 = "#90B1FF" #P(E|NOT-H) blue
color3 = "#B22222" #P(H) red

#newColor1 = "#"

root = Tk()
def main():
	#Init variables
	p_left = 0.50 #P(E|H)
	p_middle = 0.50 #P(H)
	p_right = 0.50 #P(E|Not-H)

	TOTALHEIGHT = 300 #Height of the barGraph
	TOTALWIDTH = 600 #Width of the barGraph

	color1 = "#90FF93" #P(E|H) green
	color2 = "#90B1FF" #P(E|NOT-H) blue
	color3 = "#B22222" #P(H) red

	lastPressedX = 0
	lastPressedY = 0

	pressed_leftBox = False
	pressed_rightBox = False
	pressed_middleLine = False

	root.title("Bayesian Confirmation")
	#Canvas init
	canvas = Canvas(root, width=1200, height=625, highlightthickness=0)
	canvas.pack()

	#variable widgets
	varWidgets = {}

	#Draw static Objects/Lines
	drawStatics(canvas)

	#Variable Formula Text-------------------------------------
	VARIABLE_FORMULA_FRAME_WIDTH = 275
	VARIABLE_FORMULA_FRAME_HEIGHT = 100
	varFormFrame = Canvas(canvas, width = VARIABLE_FORMULA_FRAME_WIDTH, \
	height= VARIABLE_FORMULA_FRAME_HEIGHT, highlightthickness=0)

	#Numerator Entry1[P(E|H)] x Entry2[P(H)]
	c_entry1 = Entry(varFormFrame, font=("Calibri", 20, "bold"), background=color1)
	c_entry2 = Entry(varFormFrame, font=("Calibri", 20, "bold"), background=color1, fg=color3)
	c_label2 = Label(varFormFrame, text = "x", font=("Calibri", 20), background=color1)

	#Background highlights
	varFormFrame.create_rectangle(45, 4, 225, VARIABLE_FORMULA_FRAME_HEIGHT/2, fill=color1, outline = color1)
	varFormFrame.create_rectangle(88, VARIABLE_FORMULA_FRAME_HEIGHT/2, 265, 94, fill=color2, outline = color2)
	varFormFrame.create_rectangle(10, VARIABLE_FORMULA_FRAME_HEIGHT/2, 60, 94, fill=color1, outline=color1)

	#Denominator SAA + (Entry3[P(E|NOT-H) x P(NOT-H)])
	varFormFrame.create_text(35, 70, text="SAA", font=("Calibri", 23))
	varFormFrame.create_text(80, 70, text=" + (", font=("Calibri", 23))
	c_entry3 = Entry(varFormFrame, font=("Calibri", 20, "bold"), background=color2)

	text3_var = StringVar()
	c_label4 = Label(varFormFrame, textvariable=text3_var, font=("Calibri", 20, "bold"), background=color2, pady= 0)
	#Result = [P(H|E)]
	text4_var = StringVar()
	pheVarLabel = Label(canvas, textvariable=text4_var, font=("Calibri", 25, "bold"))

	TOP_SEPERATOR_Y = 160

	#Variable formula text
	canvas.create_window(810, 80, window= varFormFrame)

	#PHE Variable text
	canvas.create_window(1030, TOP_SEPERATOR_Y/2, window= pheVarLabel)

	varFormFrame.create_window(90, 25, window = c_entry1, width= 60)
	varFormFrame.create_window(185, 25, window = c_entry2, width= 60)
	varFormFrame.create_window(138, 25, window= c_label2)

	#varFormFrame.create_window(55, 75, window = c_label3)

	varFormFrame.create_window(130, 72, window = c_entry3, width=60)
	varFormFrame.create_window(215, 70, window = c_label4)
	varFormFrame.create_line(0, VARIABLE_FORMULA_FRAME_HEIGHT/2, VARIABLE_FORMULA_FRAME_WIDTH,\
	VARIABLE_FORMULA_FRAME_HEIGHT/2, width = 3)


	#Labels on bar graph-----------------------------------------------
	#Add background colors to the variable numbers on this canvas graph
	#color1 for P(E|H), color2 for P(E|NOT-H), and color3 for P(H)

	#--------BarGraph labels init------------
	#P(E|H)
	canPeh = label.ProbLabel(15, "E|H")
	canPeh.draw(canvas, 380, 370)

	leftLabel = canvas.create_text((400, 405), font=("Purisa", 15), text='=\n{0:.2f}'.format(p_left), justify=CENTER)

	#P(E|NOT-H)
	canPeNotH = label.ProbLabel(15, "E|Not-H")
	canPeNotH.draw(canvas, 1082, 370)
	rightLabel = canvas.create_text((1115, 405), font=("Purisa", 15), text='=\n{0:.2f}'.format(p_right, justify=CENTER))

	canPH = label.ProbLabel(15, "HTags")
	middleLabel = canvas.create_text((773, 580), font=("Purisa", 15), text=' = {0:.2f}'.format(p_middle), fill=color3)

	#Labels for Believe/Disbelieve and Confirmation/Disconfirmation that will are initially grey
	believeLabel = canvas.create_text((75, 475), font=("Calibri", 17, "bold"), text="BELIEVE", fill="grey")
	disbelieveLabel = canvas.create_text((75, 525), font=("Calibri", 17, "bold"), text="DISBELIEVE", fill="grey")
	confirmationLabel = canvas.create_text((240, 475), font=("Calibri", 17, "bold"), text="CONFIRMATION", fill="grey")
	disconfirmationLabel = canvas.create_text((240, 525), font=("Calibri", 17, "bold"), text="DISCONFIRMATION", fill="grey")

	#Array to hold all the widgets to be changed in the draw function
	varWidgets["c_entry1"] = c_entry1
	varWidgets["c_entry2"] = c_entry2
	varWidgets["c_entry3"] = c_entry3
	varWidgets["c_label2"] = c_label2
	varWidgets["c_label4"] = c_label4
	varWidgets["pheVarLabel"] = pheVarLabel
	varWidgets["text3_var"] = text3_var
	varWidgets["text4_var"] = text4_var
	varWidgets["varFormFrame"] = varFormFrame

	varWidgets["middleLabel"] = middleLabel
	varWidgets["leftLabel"] = leftLabel
	varWidgets["rightLabel"] = rightLabel
	varWidgets["canPH"] = canPH
	varWidgets["canPeh"] = canPeh
	varWidgets["canPeNotH"] = canPeNotH
	#PiChart and Bayes Results
	varWidgets["believeLabel"] = believeLabel
	varWidgets["disbelieveLabel"] = disbelieveLabel
	varWidgets["confirmationLabel"] = confirmationLabel
	varWidgets["disconfirmationLabel"] = disconfirmationLabel

	#Init beginning boxes
	left_rect = [450, 400, 750, 550]
	right_rect = [750, 400, 1050, 550]
	middle_line = 750

	varWidgets["left_rect"] = left_rect
	varWidgets["right_rect"] = right_rect
	varWidgets["middle_line"] = middle_line

	drawVars(canvas, p_left, p_middle, p_right, varWidgets)
	#Bind functions keyboard and mouse functions, details in a comment in the function itself
	canvas.bind("<Button-1>", lambda event: leftClick(event, canvas))
	canvas.bind("<Motion>", lambda event: changeCursor(event, root, canvas))
	root.bind("<Return>", lambda event: updateAll(canvas, varWidgets))
	canvas.bind("<B1-Motion>", lambda event: leftClickDrag(event, canvas, varWidgets))
	root.mainloop()

#On presses check if user clicks any of the draggable sections
def leftClick(event, canvas):
	x = event.x
	y = event.y
	leftBox = canvas.coords("left_rect")
	rightBox = canvas.coords("right_rect")

	#Gets the width of the box to get the length of the lines on top of the boxes (Which are the draggable portion)
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

	#Check if user clicked the middle line
	elif leftBox[2] - 5 <= x <= leftBox[2] + 5 and 250 <= y <= 550:
		pressed_middleLine = True

#draws static objects and lines on the input canvas
def drawStatics(canvas):
	#Init canvas with seperators for each section
	TOP_SEPERATOR_Y = 160
	canvas.create_line(350, TOP_SEPERATOR_Y, 350, 625, width=5)
	canvas.create_line(0, TOP_SEPERATOR_Y, 1200, TOP_SEPERATOR_Y, width = 5)

	#Equals signs between formulas
	canvas.create_text(120, TOP_SEPERATOR_Y/2, text="=", font=("Calibri", 23, ""))
	canvas.create_text(635, TOP_SEPERATOR_Y/2, text="=", font=("Calibri", 23, ""))
	#Copyright mark
	canvas.create_text(40, 620, text= "© Lyle Crawford", fill="grey", font=("Times New Roman", 8))

	#Formula Frame
	phe1 = label.ProbLabel(23, "H|E")
	phe1.draw(canvas, 35, TOP_SEPERATOR_Y/2)
	formTemp = formula.Formula(3, 4, 5, 375, 80)
	formTemp.draw(canvas)
	#Bar graph
	# Create an open box for the left and right boxes
	create_open_rectangle(canvas, 450, 250, 1050, 550)

#draw variables with the current values
def drawVars(canvas, peH, pH, peNotH, varWidgets):
	try:
		p_he = (p_left * (1-p_middle)) / ((p_left * (1-p_middle)) + (p_right * (p_middle)))
	except ZeroDivisionError:
		p_he = 0
	#----------------Formula frame--------------------
	c_entry1 = varWidgets.get("c_entry1")
	c_entry2 = varWidgets.get("c_entry2")
	c_entry3 = varWidgets.get("c_entry3")
	c_label2 = varWidgets.get("c_label2")
	#c_label4 = varWidgets.get("c_label4")
	pheVarLabel = varWidgets.get("pheVarLabel")
	text3_var = varWidgets.get("text3_var")
	text4_var = varWidgets.get("text4_var")

	#Update the formula entries and labels with new percentages
	#P(E|H) Entry
	c_entry1.delete(0, END)
	c_entry1.insert(0, "{0:.2f}".format(p_left))

	#P(E|NOT-H)
	c_entry3.delete(0, END)
	c_entry3.insert(0, "{0:.2f}".format(p_right))

	#P(H)
	c_entry2.delete(0, END)
	c_entry2.insert(0, "{0:.2f}".format(1-p_middle))
	text3_var.set('x  {0:.2f}  )'.format(p_middle))
	text4_var.set('=    {0:.2f}'.format(p_he))

	#--------------Bar Graph----------------
	leftBox = varWidgets.get("left_rect")
	rightBox = varWidgets.get("right_rect")
	middleLine = varWidgets.get("middle_line")

	leftLabel = varWidgets.get("leftLabel")
	rightLabel = varWidgets.get("rightLabel")
	middleLabel = varWidgets.get("middleLabel")

	canvas.delete("left_rect")
	canvas.delete("right_rect")
	canvas.delete("middle_line")
	canvas.delete("canPH")
	canvas.delete("canPeH")
	canvas.delete("canPeNotH")
	#Using the given coordinates create the left box and right box and the middle line
	canvas.create_rectangle(leftBox[0], leftBox[1], leftBox[2], leftBox[3], fill=color1, tags="left_rect", width=5)
	canvas.create_rectangle(rightBox[0], rightBox[1], rightBox[2], rightBox[3], fill=color2, tags="right_rect", width=5)
	canvas.create_line(middleLine, 250, middleLine, 550, width=5, fill=color3, tags="middle_line")

	#P(H) (Middle label)
	canPH = label.ProbLabel(15, "HTags")
	canPH.draw(canvas, middleLine - 30, 580)
	canvas.itemconfigure(middleLabel, text='= {0:.2f}'.format(round(1-p_middle,2)))
	canvas.coords(middleLabel, middleLine + 30 , 580)


	#P(E|H) Variable numbers
	canvas.coords(leftLabel, 400 , leftBox[1]- 10)
	canPeh = label.ProbLabel(15, "E|H")
	canPeh.draw(canvas, 380, leftBox[1] - 50)
	leftLabel = varWidgets.get("leftLabel")
	canvas.itemconfigure(leftLabel, text='=\n{0:.2f}'.format(round(p_left, 2)), justify=CENTER)

	#P(E|Not-H) variable numbers
	canvas.coords(rightLabel, 1115, rightBox[1]- 10)
	canPeNotH = label.ProbLabel(15, "E|Not-H")
	canPeNotH.draw(canvas, 1082, rightBox[1] - 50)
	rightLabel = varWidgets.get("rightLabel")
	canvas.itemconfigure(rightLabel, text='=\n{0:.2f}'.format(round(p_right, 2)), justify=CENTER)

	#---------------------Pi chart----------------------------------------------
	canvas.delete("pi1")
	canvas.delete("pi2")
	canvas.delete("pi_h")

	pi_degree = p_he * 360
	if pi_degree == 360:
		pi_degree = 359.9

	canvas.create_oval((75,200,275,400), fill=color2, tags="pi1")
	canvas.create_arc((75,200,275,400), fill=color1, extent= (-pi_degree), tags="pi2", start=90)

	#PI CHART P(H)
	pi_r = 110
	pi_angle = (360 * p_middle)-180
	pi_x = pi_r * math.sin(math.radians(pi_angle))
	pi_y = pi_r * math.sin(math.radians(90-pi_angle))
	canvas.create_line(175, 300, pi_x+175, pi_y+300, width = 3, tags="pi_h", fill=color3)

	#Believe/Disbelieve and Confirmation/Disconfirmation Thresholds
	believeLabel = varWidgets.get("believeLabel")
	disbelieveLabel = varWidgets.get("disbelieveLabel")
	confirmationLabel = varWidgets.get("confirmationLabel")
	disconfirmationLabel = varWidgets.get("disconfirmationLabel")

	if round(p_he, 2) == 0.50:
		canvas.itemconfigure(believeLabel, fill="#C0C0C0")
		canvas.itemconfigure(disbelieveLabel, fill="#C0C0C0")

	elif p_he > 0.50:
		canvas.itemconfigure(believeLabel, fill="black")
		canvas.itemconfigure(disbelieveLabel, fill="#C0C0C0")
	elif p_he < 0.50:
		canvas.itemconfigure(disbelieveLabel, fill="black")
		canvas.itemconfigure(believeLabel, fill="#C0C0C0")

	if round(p_he, 2) == (round(1-p_middle, 2)):
		canvas.itemconfigure(confirmationLabel, fill="#C0C0C0")
		canvas.itemconfigure(disconfirmationLabel, fill="#C0C0C0")

	elif round(p_he, 2) > (round(1-p_middle, 2)):
		canvas.itemconfigure(confirmationLabel, fill="black")
		canvas.itemconfigure(disconfirmationLabel, fill="#C0C0C0")
	elif round(p_he, 2) < (round(1-p_middle, 2)):
		canvas.itemconfigure(disconfirmationLabel, fill="black")
		canvas.itemconfigure(confirmationLabel, fill="#C0C0C0")

#Left click and drag will constantly update the boxes as the user moves their mouse while holding left click
def leftClickDrag(event, canvas, varWidgets):
	global lastPressedX
	global lastPressedY
	global p_left
	global p_right
	global p_middle

	#variables
	leftBox = canvas.coords("left_rect")
	rightBox = canvas.coords("right_rect")
	middleLine = canvas.coords("middle_line")

	#Find the difference of the event position relative to the top of the box (for vertical) and most left of the box (for horizontal)
	#Then round it to the nearest 3rd pixel for vertical and 6th pixel for horizontal
	#This position is used to get the most accurate representation of the percentages to 2 decimal places
	horizontal_position = round_to_near((event.x - 450), False)
	vertical_position = round_to_near((event.y - 250), True)

	if pressed_leftBox == True:
		p_left = 1-(vertical_position / 300)

		if p_left >= 1:
			p_left = 1
		elif p_left <= 0:
			p_left = 0

		new_leftHeight = ((1-p_left) * 300) + 250
		new_left = [leftBox[0], new_leftHeight, leftBox[2], leftBox[3]]
		varWidgets["left_rect"] = new_left
		drawVars(canvas, p_left, p_middle, p_right, varWidgets)

	elif pressed_rightBox == True:
		p_right = 1-(vertical_position / 300)

		if p_right >= 1:
			p_right = 1
		elif p_right <= 0:
			p_right = 0

		new_rightHeight = ((1-p_right) * 300) + 250
		new_right = [rightBox[0], new_rightHeight, rightBox[2], rightBox[3]]
		varWidgets["right_rect"] = new_right
		drawVars(canvas, p_left, p_middle, p_right, varWidgets)

	elif pressed_middleLine == True:
		p_middle = 1-(horizontal_position / 600)

		if p_middle >= 1:
			p_middle = 1
		elif p_middle <= 0:
			p_middle = 0

		new_middle = ((1-p_middle) * 600) + 450
		new_left = [leftBox[0], leftBox[1], new_middle, leftBox[3]]
		new_right = [new_middle, rightBox[1], rightBox[2], rightBox[3]]

		varWidgets["left_rect"] = new_left
		varWidgets["right_rect"] = new_right
		varWidgets["middle_line"] = new_middle

		drawVars(canvas, p_left, p_middle, p_right, varWidgets)

#Using coordinates of a rectangle, will use lines to create an open rectangle instead
def create_open_rectangle(canvas, x1, y1, x2, y2):
	canvas.delete("box1")
	canvas.delete("box2")
	canvas.delete("box3")
	canvas.delete("box4")
	canvas.create_line(x1-2, y1, x2+3, y1, width = 5, tags="box1")
	canvas.create_line(x2, y1, x2, y2+4, width = 5, tags="box2")
	canvas.create_line(x2, y2+1, x1, y2+1, width = 5, tags="box3")
	canvas.create_line(x1, y2+4, x1, y1, width = 5, tags="box4")

#Update everything when this function is called using the updated entries
def updateAll(canvas, varWidgets):
	#init global percentages, then set them as the entry values
	global p_left
	global p_middle
	global p_right

	#Get the variable in entry1, entry2 and entry3
	entry1 = varWidgets.get("c_entry1")
	entry2 = varWidgets.get("c_entry2")
	entry3 = varWidgets.get("c_entry3")

	print(entry1.get())

	p_left = float(entry1.get())
	p_middle = 1-(float(entry2.get()))
	p_right = float(entry3.get())

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

	#Change rectangle coords after getting new values from the entries
	middleLine = TOTALWIDTH * (1-p_middle) + 450
	leftHeight = TOTALHEIGHT * (1-p_left) + 250
	rightHeight = TOTALHEIGHT * (1-p_right) + 250

	leftBox = [450, leftHeight, middleLine, 550]
	rightBox = [middleLine, rightHeight, 1050, 550]
	varWidgets["left_rect"] = leftBox
	varWidgets["right_rect"] = rightBox
	varWidgets["middle_line"] = middleLine

	drawVars(canvas, p_left, p_middle, p_right, varWidgets)

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

	elif leftBox[2] - 5 <= x <= leftBox[2] + 5 and 250 <= y <= 550:
		root.config(cursor='sb_h_double_arrow')
	else:
		root.config(cursor="")

#Take a number then round it to the nearest third or sixth
def round_to_near(number, third):
	number = round(number, 2)

	if third:
		newNumber = 0
		x = (number / 3) % 1

		if x == 0.0:
			newNumber = number

		elif x > 0.5:
			newNumber = number + 1

		elif x < 0.5:
			newNumber = number - 1

		return newNumber

	if not third:
		newNumber = 0
		x = round(((number / 6) % 1), 2)

		if x == 0.0:
			newNumber = number

		elif x == round(((1/6) % 1), 2):
			newNumber = number - 1

		elif x == round(((2/6) % 1), 2):
			newNumber = number - 2

		elif x == round(((3/6) % 1), 2):
			newNumber = number + 3


		elif x == round(((4/6) % 1), 2):
			newNumber = number + 2


		elif x == round(((5/6) % 1), 2):
			newNumber = number + 1

		return newNumber

main()
