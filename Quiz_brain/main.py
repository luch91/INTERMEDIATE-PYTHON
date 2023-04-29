from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [] # a list of question objects
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

