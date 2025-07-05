from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_bank = []
for question in question_data:
    questions_bank.append(Question(question.get('question'), question.get('correct_answer')))
    
quiz = QuizBrain(questions_bank)
while quiz.still_has_questions():
    quiz.next_question()
    quiz.check_answer()
    
print(f"Your final score is {quiz.score}")
