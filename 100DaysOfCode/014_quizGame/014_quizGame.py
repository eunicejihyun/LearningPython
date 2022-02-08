from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from quiz_ui import QuizUI

question_bank = []
score = 0

for qa in question_data:
    qa = Question(qa["question"], qa["correct_answer"])
    question_bank.append(qa)

quiz = QuizBrain(question_bank)
quiz_ui = QuizUI(quiz)
