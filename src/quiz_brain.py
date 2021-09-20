class QuizBrain:

    def __init__(self, question_bank: list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank
        self.no_of_questions = len(self.question_list)
        self.current_question = None

    def out_of_questions(self):
        return self.question_number >= self.no_of_questions

    def next_question(self) -> str:
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        text = self.current_question.text
        return text

    def check_answer(self, user_answer: bool) -> bool:
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False



