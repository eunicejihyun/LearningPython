from tkinter import *
from quiz_brain import QuizBrain

BACKGROUND = "#1A1A2E"
PADDING = 20
FONT = ("Helvetica", 20, "italic")


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("EJ's Quiz Game")
        self.window.config(padx=PADDING, pady=PADDING, bg=BACKGROUND)

        self.question_box = Label(text="Question here!", font=FONT, height=15, width=25, bg=BACKGROUND, fg="white",
                                  wraplength=400, justify=CENTER)
        self.question_box.grid(row=1, column=0, columnspan=2)

        self.score = Label(text="Score", bg=BACKGROUND, fg="white", font=("Helvetica", 12))
        self.score.grid(row=0, column=0, columnspan=2)

        TRUE_IMG = PhotoImage(file="images/true.png")
        self.true = Button(image=TRUE_IMG, bg=BACKGROUND, highlightthickness=0, border=0, command=self.click_true)
        self.true.grid(row=2, column=0)

        FALSE_IMG = PhotoImage(file="images/false.png")
        self.false = Button(image=FALSE_IMG, bg=BACKGROUND, highlightthickness=0, border=0, command=self.click_false)
        self.false.grid(row=2, column=1)

        self.get_next_q()

        self.window.mainloop()

    def click_true(self):
        answer = self.quiz.question_list[self.quiz.question_number-1].answer
        self.feedback(self.quiz.check_answer("true", answer))

    def click_false(self):
        answer = self.quiz.question_list[self.quiz.question_number-1].answer
        self.feedback(self.quiz.check_answer("false", answer))

    def get_next_q(self):
        self.question_box.config(fg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_box.config(text=q_text)
        else:
            self.question_box.config(text="You've reached the end of the quiz.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def feedback(self, is_correct: bool):
        if is_correct:
            self.question_box.config(fg="green")
        else:
            self.question_box.config(fg="red")
        self.window.after(1000, self.get_next_q)
