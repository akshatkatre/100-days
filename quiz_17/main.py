from quiz_17.question_model import Question
from quiz_17.data import question_data
from quiz_17.quiz_brain import QuizBrain

question_bank_list = []
for item in question_data[0]['results']:
    # print(item['text'], item['answer'])
    question_bank_list.append(Question(item['question'], item['correct_answer']))

quiz = QuizBrain(question_bank_list)
while quiz.still_has_questions():
    quiz.next_question()

print("The quiz is now complete.")
print(f"The FINAL SCORE : {quiz.get_score()}")
