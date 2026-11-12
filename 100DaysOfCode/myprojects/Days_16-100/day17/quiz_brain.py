# Handles the quiz

import html

ANSWER_MAPPING = {
    "true": "True",
    "t": "True",
    "false": "False",
    "f": "False"
}

class QuizBrain:
    def __init__(
            self,
            question_list:list
    ):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {html.unescape(current_question.text)} (True/False):  ")

        self.check_answer(user_answer, current_question.answer)



    def still_has_question(self):

        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        user = ANSWER_MAPPING.get(user_answer.strip().lower()).lower()

        correct = correct_answer.strip().lower()

        if user is None:
            print("Invalid answer.")
        elif user == correct:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
        print(f"The correct answer was: {correct_answer}.")





