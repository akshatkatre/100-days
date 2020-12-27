from tkinter import *
from quizzler_app_34.quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, q_brain: QuizBrain):
        self.quiz_brain = q_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="Questions go here",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Create images
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_clicked)
        self.true_button.grid(row=2, column=1)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_clicked)
        self.false_button.grid(row=2, column=0)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            question_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_clicked(self):
        is_correct = self.quiz_brain.check_answer("true")
        self.give_feedback(is_correct)

    def false_clicked(self):
        is_correct = self.quiz_brain.check_answer("false")
        self.give_feedback(is_correct)

    def give_feedback(self, is_answer_correct):
        bg_color: str
        if is_answer_correct == "correct":
            bg_color = 'Green'
        else:
            bg_color = 'Red'
        self.canvas.config(bg=bg_color)
        self.window.after(1000, self.get_next_question)
