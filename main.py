import random
total_questions=5

class Quiz:
    def __init__(self):
        self.score=0
        self.questions=[]
        self.wrong_answers=[]
        with open("questions.txt","r") as f:
            for line in f:
                line=line.strip()
                data=line.split(",")
                self.questions.append(data)
            random.shuffle(self.questions)
            self.questions=random.sample(self.questions,5)
            
    def start_quiz(self):
        self.name=input("Enter your name:")
        self.display_questions()
        self.show_result()
        self.show_wrong_answers()
        
    def display_questions(self):
        for qnum,i in enumerate(self.questions,start=1):
            print(qnum,".",i[0])
            print(i[1])
            print(i[2])
            print(i[3])
            print(i[4])
            while True:
                ans=input("Enter your answer (A/B/C/D):")
                if ans in ['A','B','C','D','a','b','c','d']:
                    break
                print('Invalid Option')
            self.check_answer(ans,i[5],qnum,i)
            
    def check_answer(self,answer,correctanswer,qnum,line):
        if answer.upper()==correctanswer.upper():
            self.score+=1
            print("Correct Answer!!!")
            print(f"Question {qnum} of {total_questions}")
            print("Current score:",self.score)
        else:
            self.wrong_answers.append((line,answer))
            print("Wrong answer")
            print("Correct answer is:",correctanswer)
            
    def show_result(self):
        print("\nName:",self.name)
        print("Correct Answers:",self.score,"/",total_questions)
        print("Wrong answers:",total_questions-self.score,"/",total_questions)
        print("Percentage:",(self.score/total_questions)*100,"%")
        
    def show_wrong_answers(self):
        if not self.wrong_answers:
            print("\nExcellent! No wrong answers.")
            return

        print("\nQuestions answered incorrectly:")

        for question, user_answer in self.wrong_answers:
            print("\nQuestion:", question[0])
            print("Your answer:", user_answer)
            print("Correct answer:", question[5])
        
    def save_score(self):
        with open("scores.txt","a") as f:
            f.write(f"{self.name} - {self.score}/{total_questions}\n")

quiz=Quiz()
quiz.start_quiz()
quiz.save_score()