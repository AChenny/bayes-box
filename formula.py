#Formula class
import tkinter
import label

#Class for method
class Formula:
    #Constants for how far the text are apart
    # Middle of the origin
    #P(H|E) Text LOCATION X= PHETEXT_X
    PHE_TEXT_X = -50

    def __init__(self, eH, h, notH, x, y):
        self.eH = eH
        self.h = h
        self.notH = notH
        self.x = x
        self.y = y

    def draw(self, canvas):
        #Frame for whole Formula
        FRAME_WIDTH = 900
        FRAME_HEIGHT = 150

        # TODO: Have constants that will be set as multipliers or something to add
        # as the font increases or decreases

        #Second Formula frame
        #TODO: Use the origin position to position the text IE: +x or -x etc.
        SECOND_FORMULA_FRAME_WIDTH = 380
        SECOND_FORMULA_FRAME_HEIGHT = 80
        secFormFrame = tkinter.Canvas(canvas, width=SECOND_FORMULA_FRAME_WIDTH, \
        height=SECOND_FORMULA_FRAME_HEIGHT)

        #TODO: Change to the 2 colors blue and green
        #Background colors for the Formula text
        color1 = "#90FF93" #P(E|H) green
        color2 = "#90B1FF" #P(E|NOT-H) blue
        color3 = "#FF9090" #P(H) red
        secFormFrame.create_rectangle(90, 2, 170,35, fill=color1)
        secFormFrame.create_rectangle(95, 45, 230, 80, fill=color2)
        secFormFrame.create_rectangle(230, 2, 290, 35, fill=color3)

        #NUMERATOR
        #P(E|H)
        peh1 = label.ProbLabel(23, "E|H")
        peh1.draw(secFormFrame, 100, 15)

        # x
        secFormFrame.create_text(200, 15, text="x", font=("Calibri", 23, ""))

        # P(H)
        ph1 = label.ProbLabel(23, "H")
        ph1.draw(secFormFrame, 240, 15)

        #Division line
        secFormFrame.create_line(0, (SECOND_FORMULA_FRAME_HEIGHT/2), SECOND_FORMULA_FRAME_WIDTH, (SECOND_FORMULA_FRAME_HEIGHT/2), width = 3)

        #Denominator
        #SAA
        secFormFrame.create_text(45, 60, text="SAA + (", font=("Calibri", 23, ""))
        secFormFrame.create_text(375, 60, text=")", font=("Calibri", 23, ""))
        #P(E|Not-H)
        eNotH1 = label.ProbLabel(23, "E|Not-H")
        eNotH1.draw(secFormFrame, 105, 60)

        secFormFrame.create_text(245, 60, text="x", font=("Calibri", 23, ""))

        #P(Not-H)
        notH1 = label.ProbLabel(23, "Not-H")
        notH1.draw(secFormFrame, 270, 60)

        canvas.create_window(self.x, self.y, window=secFormFrame)

    #delete function should delete all the text in this frame
    #def delete(self, canvas):
