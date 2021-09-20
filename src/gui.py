from tkinter import *

THEME_COLOR = "#375362"
TRUE_COLOR = "#8ce681"
FALSE_COLOR = "#e38686"


class QuizInterface:
    class QuizLabel(Label):
        def __init__(self, **kwargs):
            super().__init__(bg=THEME_COLOR, fg="white", **kwargs)

    class QuizButton(Button):
        def __init__(self, **kwargs):
            super().__init__(highlightthickness=0, **kwargs)

    def __init__(self):
        # Style
        self.question_font = ("Arial", 17, "italic")

        # Window
        self.window = Tk()
        self.window.title("Simple Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Images
        self.true_img = PhotoImage(file="../images/true.png")
        self.false_img = PhotoImage(file="../images/false.png")

        # Labels
        self.question_label = self.QuizLabel(text="Q.0/10")
        self.question_label.grid(column=0, row=0, sticky=W)
        self.score_label = self.QuizLabel(text="Score: 0/10")
        self.score_label.grid(column=1, row=0, sticky=E)

        # Canvas
        self.canvas = Canvas(width=300, height=300, highlightthickness=0,
                             bg="white")
        self.question = self.canvas.create_text(300 / 2,
                                                350 / 2,
                                                font=self.question_font,
                                                text="Question",
                                                fill=THEME_COLOR,
                                                width=290)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20,
                         sticky=N + S + W + E)

        # Buttons
        self.true_button = self.QuizButton(image=self.true_img)
        self.true_button.grid(column=0, row=2)
        self.false_button = self.QuizButton(image=self.false_img)
        self.false_button.grid(column=1, row=2)

        # Setup
        self.window.mainloop()
