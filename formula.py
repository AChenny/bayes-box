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

        #Background colors for the Formula text
        color1 = "#008000" #P(E|H) green
        color2 = "#4169E1" #P(H) red
        color3 = "#FF0000" #P(E|NOT-H) blue
        secFormFrame.create_rectangle(100, 2, 180 ,35, fill=color1)
        secFormFrame.create_rectangle(105, 45, 240, 80, fill=color2)
        secFormFrame.create_rectangle(220, 2, 280, 35, fill=color3)

        #NUMERATOR
        #P(E|H)
        peh1 = label.ProbLabel(23, "E|H")
        peh1.draw(secFormFrame, 110, 15)

        # x
        secFormFrame.create_text(200, 15, text="x", font=("Calibri", 23, ""))

        # P(H)
        ph1 = label.ProbLabel(23, "H")
        ph1.draw(secFormFrame, 230, 15)


        #Division line
        secFormFrame.create_line(0, (SECOND_FORMULA_FRAME_HEIGHT/2), SECOND_FORMULA_FRAME_WIDTH, (SECOND_FORMULA_FRAME_HEIGHT/2), width = 5)

        #Denominator
        #SAA
        secFormFrame.create_text(60, 60, text="SAA + (", font=("Calibri", 23, ""))
        secFormFrame.create_text(375, 60, text=")", font=("Calibri", 23, ""))
        #P(E|Not-H)
        eNotH1 = label.ProbLabel(23, "E|Not-H")
        eNotH1.draw(secFormFrame, 115, 60)

        secFormFrame.create_text(250, 60, text="x", font=("Calibri", 23, ""))

        #P(Not-H)
        notH1 = label.ProbLabel(23, "Not-H")
        notH1.draw(secFormFrame, 270, 60)

        canvas.create_window(self.x, self.y, window=secFormFrame)

    #delete function should delete all the text in this frame
    #def delete(self, canvas):
