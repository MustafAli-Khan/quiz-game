from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_Bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    NewQuestion = Question(question_text, question_answer)
    Question_Bank.append(NewQuestion)

quiz = QuizBrain(Question_Bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")

