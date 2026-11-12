from question_model import Question, OpenTriviaAPI
from quiz_brain import QuizBrain
from data import question_data

question_bank = [
    Question(**question)
    for question in question_data
]

question_bank = OpenTriviaAPI(

)

question_bank.select_category()

question_bank.request_questions()


quiz = QuizBrain(question_bank.questions)

while quiz.still_has_question():
    quiz.next_question()

    stage = "current" if quiz.still_has_question() else "final"

    print(
        f"Your {stage} score is: {quiz.score}/{quiz.question_number}."
        f"\n"
    )



