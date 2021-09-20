from tkinter import *
from quiz_brain import QuizBrain
from question import get_questions, TOKEN

THEME_COLOR = "#375362"
TRUE_COLOR = "#8ce681"
FALSE_COLOR = "#e38686"
ROUNDS = 10


class QuizInterface:
    class QuizLabel(Label):
        def __init__(self, **kwargs):
            super().__init__(bg=THEME_COLOR, fg="white", **kwargs)

    class QuizButton(Button):
        def __init__(self, **kwargs):
            super().__init__(highlightthickness=0, **kwargs)

    def __init__(self, quiz_brain=QuizBrain(get_questions(amount=ROUNDS, token=TOKEN))):
        # Quiz brain
        self.quiz = quiz_brain

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
        self.question_label = self.QuizLabel(text="Q: 0/10")
        self.question_label.grid(column=0, row=0, sticky=W)
        self.score_label = self.QuizLabel(text="Score: 0/10")
        self.score_label.grid(column=1, row=0, sticky=E)

        # Canvas
        self.canvas = Canvas(width=300, height=300, highlightthickness=0,
                             bg="white")
        self.question = self.canvas.create_text(150,
                                                150,
                                                font=self.question_font,
                                                text="Question",
                                                fill=THEME_COLOR,
                                                width=290,
                                                justify="center")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        # Buttons
        self.true_button = self.QuizButton(image=self.true_img,
                                           command=lambda: self.button_press(True))
        self.true_button.grid(column=0, row=2)
        self.false_button = self.QuizButton(image=self.false_img,
                                            command=lambda: self.button_press(False))
        self.false_button.grid(column=1, row=2)

        # Setup
        self.next_question()
        self.window.mainloop()

    def button_press(self, answer):
        is_right = self.quiz.check_answer(answer)
        color = TRUE_COLOR if is_right else FALSE_COLOR
        self.canvas.config(bg=color)
        self.window.after(900, self.next_question)

    def new_game(self):
        question_bank = get_questions(amount=ROUNDS, token=TOKEN)
        self.quiz = QuizBrain(question_bank)
        self.true_button.config(command=lambda: self.button_press(True))
        self.false_button.config(command=lambda: self.button_press(False))
        self.next_question()

    def next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.no_of_questions}")
        if self.quiz.out_of_questions():
            self.canvas.itemconfig(self.question,
                                   text=f"You've completed the quiz with the score "
                                        f"of {self.quiz.score}/{self.quiz.no_of_questions}!\n"
                                        f"Do you want another round?")
            self.true_button.config(command=self.new_game)
            self.false_button.config(command=quit)
        else:
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question_text)
            self.question_label.config(text=f"Q: {self.quiz.question_number}/{self.quiz.no_of_questions}")
