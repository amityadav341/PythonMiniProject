class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
    def still_has_question(self):
        if self.question_number==len(self.question_list):
            return False
        else:
           return True
    def next_question(self):
        current_question=self.question_list[self.question_number]
        current_question_ans=self.question_list[self.question_number].answer
        self.question_number+=1
        user_ans=input(f"Q{self.question_number}:{current_question.text} (True/False)?: ")
        self.check_ans(user_ans,current_question_ans)
    def check_ans(self,user_ans,curr_ans):
          if user_ans.lower()==curr_ans.lower():
              self.score+=1
              print("that's correct answer! ")
          else:
              print(f"that's wrong answer! Correct answer is {curr_ans}")
         
          print(f"Your current score is {self.score}/{self.question_number}")



# Author:- Amit Yadav

         
        