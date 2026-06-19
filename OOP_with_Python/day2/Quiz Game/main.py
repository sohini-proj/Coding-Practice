from data import quiz_data
from question_model import question
from quiz_brain import QuizBrain

question_bank=[]
for i in quiz_data:
    new_ques=question(i["question"],i["answer"])
    question_bank.append(new_ques)


while True:
    print("""
    =====================================================================================================================
                                         🧠   Q U I Z   G A M E
                                  Think Fast • Answer Right • Beat The Score
    =====================================================================================================================
    """)
    game_1=QuizBrain(question_bank)
    num=int(input(f"\nEnter number of questions you would like(0 - {len(question_bank)}): "))
    game_1.game(num)
    ch=input("Do you wanna play again?(y/n): ")
    if ch=="n":
        break
