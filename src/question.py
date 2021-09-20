from data import get_token, get_data
import html


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __str__(self):
        return f"{self.text} - {self.answer}"


def get_questions(amount=10) -> list:
    question_bank = []
    question_token = get_token()
    question_data = get_data(amount=amount,
                             token=question_token,
                             type="boolean")

    for question in question_data:
        text = question["question"]
        text = html.unescape(text)
        answer = question["correct_answer"]
        # Depending on opendb API to have correct data, maybe change this?
        answer = True if answer.lower == "true" else False
        new_question = Question(text, answer)
        question_bank.append(new_question)

    return question_bank



