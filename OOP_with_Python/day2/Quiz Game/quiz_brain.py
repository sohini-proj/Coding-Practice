import random
class QuizBrain:
    def __init__(self,list):
        self.ques_num=0
        self.ques_list=list

    def game(self,num):
        points=0
        selected_ques=[]
        selected_ques = random.sample(self.ques_list, num)
        for i in selected_ques:
            self.ques_num+=1
            q=i.ques
            a=i.ans
            print("\n=================================================================================================")
            print(f"\npoint(s): {points}/{self.ques_num}")
            print(f"\nQuestion {self.ques_num}")
            user_ans = input(f"{q} (true/false): ").lower()

            if user_ans not in ["true", "false", "t", "f"]:
                print("INVALID ANSWER\n")

            else:
                # convert short form to full form
                if user_ans == "t":
                    user_ans = "true"
                elif user_ans == "f":
                    user_ans = "false"

                if user_ans == a.lower():
                    print("YAYYYYY THATS CORRECT !!!\n")
                    points += 1
                else:
                    print("wrong ans\n")
        print(F"""
=====================================================================================================================
                                                    GAME  OVERRRR
                                                     SCORE: {points}/{num}
=====================================================================================================================
""")
    

        
        