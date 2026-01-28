from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


questinon_bank = []
loss = False

for data in question_data:
    question = data["question"]
    answer = data["correct_answer"]
    new_question = Question(question, answer)
    questinon_bank.append(new_question)

quiz = QuizBrain(questinon_bank)

while quiz.still_has_question():
    quiz.next_question()
print("You`ve completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number} ")


