from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = [
    Question(**question)
    for question in question_data
]

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()


