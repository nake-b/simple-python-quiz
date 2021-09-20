from quiz_brain import QuizBrain
from gui import QuizInterface
from question import get_questions

question_bank = get_questions(10)
quiz = QuizBrain(question_bank)
gui = QuizInterface(quiz)
