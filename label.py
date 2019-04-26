#Label class
import tkinter
import math

class ProbLabel:
    #Font size
    #Text
    def __init__(self, fontSize, text):
        self.fontSize = fontSize
        self.text = text

    def draw(self, canvas, x, y):
        #Text can be 4 options
        #P(E|H)
        if (self.text == "E|H"):
            text1X = x
            text2X = text1X + self.fontSize
            text3X = text2X + round(self.fontSize/1.5)
            text4X = text3X + round(self.fontSize * 0.75)
            canvas.create_text(text1X, y, text="P", font=("Calibri", self.fontSize, "bold italic"), tags="canPeH")
            canvas.create_text(text2X, y, text="(E", font=("Calibri", self.fontSize, ""), tags="canPeH")
            canvas.create_text(text3X, y, text="|", font=("Calibri", self.fontSize, "bold"), tags="canPeH")
            canvas.create_text(text4X, y, text="H)", font=("Calibri", self.fontSize, ""), tags="canPeH")

        #P(H)
        elif (self.text == "H"):
            text1X = x
            text2X = text1X + self.fontSize
            canvas.create_text(text1X, y, text="P", font=("Calibri", self.fontSize, "bold italic"), fill="#990000")
            canvas.create_text(text2X, y, text="  (H)", font=("Calibri", self.fontSize, ""), fill="#990000")

        #P(H) with tags
        elif (self.text == "HTags"):
            text1X = x
            text2X = text1X + self.fontSize
            canvas.create_text(text1X, y, text="P", font=("Calibri", self.fontSize, "bold italic"), tags="canPH", fill="#990000")
            canvas.create_text(text2X, y, text="  (H)", font=("Calibri", self.fontSize, ""), tags="canPH", fill="#990000" )

        #P(E|NOT-H)
        elif (self.text == "E|Not-H"):
            text1X = x
            text2X = text1X + self.fontSize
            text3X = text2X + round(self.fontSize/1.5)
            text4X = text3X + round(self.fontSize * 2)
            canvas.create_text(text1X, y, text="P", font=("Calibri", self.fontSize, "bold italic"), tags="canPeNotH")
            canvas.create_text(text2X, y, text="(E", font=("Calibri", self.fontSize, ""), tags="canPeNotH")
            canvas.create_text(text3X, y, text="|", font=("Calibri", self.fontSize, "bold"), tags="canPeNotH")
            canvas.create_text(text4X, y, text="Not-H)", font=("Calibri", self.fontSize, ""), tags="canPeNotH")

        #P(NOT-H)
        elif (self.text == "Not-H"):
            text1X = x
            text2X = text1X + round(self.fontSize * 2.4)
            canvas.create_text(text1X, y, text="P", font=("Calibri", self.fontSize, "bold italic"))
            canvas.create_text(text2X, y, text="(Not-H)", font=("Calibri", self.fontSize, ""))

        #P(H|E)
        elif (self.text == "H|E"):
            text1X = x
            text2X = text1X + self.fontSize
            text3X = text2X + round(self.fontSize/1.4)
            text4X = text3X + round(self.fontSize * 0.65)
            canvas.create_text(text1X, y, text="P", font=("Calibri", self.fontSize, "bold italic"))
            canvas.create_text(text2X, y, text="(H", font=("Calibri", self.fontSize, ""))
            canvas.create_text(text3X, y, text="|", font=("Calibri", self.fontSize, "bold"))
            canvas.create_text(text4X, y, text="E)", font=("Calibri", self.fontSize, ""))
