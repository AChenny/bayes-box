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
        FRAME_WIDTH = 950
        FRAME_HEIGHT = 150

        #Second Formula frame
        SECOND_FORMULA_FRAME_WIDTH = 450
        SECOND_FORMULA_FRAME_HEIGHT = 150
        secFormFrame = tkinter.Canvas(canvas, width=SECOND_FORMULA_FRAME_WIDTH, \
        height=SECOND_FORMULA_FRAME_HEIGHT)

        #Background colors for the Formula text
        color1 = "#90FF93" #P(E|H) green
        color2 = "#90B1FF" #P(E|NOT-H) blue
        color3 = "#B22222" #P(H) red
        secFormFrame.create_rectangle(130, (SECOND_FORMULA_FRAME_HEIGHT/2), 330, (SECOND_FORMULA_FRAME_HEIGHT/2) - 35, fill=color1, outline = color1)
        secFormFrame.create_rectangle(48, (SECOND_FORMULA_FRAME_HEIGHT/2), 105, (SECOND_FORMULA_FRAME_HEIGHT/2) + 40, fill=color1, outline = color1)
        secFormFrame.create_rectangle(145, (SECOND_FORMULA_FRAME_HEIGHT/2), 421, (SECOND_FORMULA_FRAME_HEIGHT/2) + 40, fill=color2, outline = color2)


        #NUMERATOR
        #P(E|H)
        peh1 = label.ProbLabel(23, "E|H")
        peh1.draw(secFormFrame, 140, (SECOND_FORMULA_FRAME_HEIGHT/2) - 20)

        # x
        secFormFrame.create_text(240, (SECOND_FORMULA_FRAME_HEIGHT/2) - 20, text="x", font=("Calibri", 23, ""))

        # P(H)
        ph1 = label.ProbLabel(23, "H")
        ph1.draw(secFormFrame, 280, (SECOND_FORMULA_FRAME_HEIGHT/2) - 20)

        #Division line
        secFormFrame.create_line(0, (SECOND_FORMULA_FRAME_HEIGHT/2), SECOND_FORMULA_FRAME_WIDTH, (SECOND_FORMULA_FRAME_HEIGHT/2), width = 3)

        #Denominator
        #SAA
        secFormFrame.create_text(95, (SECOND_FORMULA_FRAME_HEIGHT/2) + 20, text="SAA + (", font=("Calibri", 23, ""))
        secFormFrame.create_text(435, (SECOND_FORMULA_FRAME_HEIGHT/2) + 20, text=")", font=("Calibri", 23, ""))
        #P(E|Not-H)
        eNotH1 = label.ProbLabel(23, "E|Not-H")
        eNotH1.draw(secFormFrame, 155, (SECOND_FORMULA_FRAME_HEIGHT/2) + 20)

        secFormFrame.create_text(295, (SECOND_FORMULA_FRAME_HEIGHT/2) + 20, text="x", font=("Calibri", 23, ""))

        #P(Not-H)
        notH1 = label.ProbLabel(23, "Not-H")
        notH1.draw(secFormFrame, 320, (SECOND_FORMULA_FRAME_HEIGHT/2) + 20)

        canvas.create_window(self.x, self.y, window=secFormFrame)

    #delete function should delete all the text in this frame
    #def delete(self, canvas):
