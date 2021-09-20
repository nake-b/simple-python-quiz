from data import get_token, get_data
import html


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __str__(self):
        return f"{self.text} - {self.answer}"


def get_questions(amount=10, token=get_token()) -> list:
    question_bank = []
    question_data = get_data(amount=amount,
                             token=token,
                             type="boolean")

    for question in question_data:
        text = question["question"]
        text = html.unescape(text)
        answer = question["correct_answer"]
        # Depending on opendb API to have correct data, maybe change this to raise an exception?
        answer = True if answer.lower() == "true" else False
        new_question = Question(text, answer)
        question_bank.append(new_question)

    return question_bank


TOKEN = get_token()
