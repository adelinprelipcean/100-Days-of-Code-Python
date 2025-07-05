class QuizBrain:
    def __init__(self,questions_list):
        self.score = 0
        self.question_number = 0
        self.questions_list = questions_list
        
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        self.user_answer = input(f"Q.{self.question_number + 1} {self.questions_list[self.question_number].text} (True/False)?: ")
        
    def check_answer(self):
        if self.questions_list[self.question_number].answer == self.user_answer:
            print('The answer is correct!')
            self.score +=1
        else:
            print(f'The answer is wrong, the correct answer is {self.questions_list[self.question_number].answer}.')
        self.question_number += 1
    
    