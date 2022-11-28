from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # tap into questions from quiz_brain class
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Create canvas
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="",
            width= 275,
            font=FONT
        )
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)
        # create score text
        self.score_tracker = Label(text=f"Score: ", font=("Arial", 15), fg="white", bg=THEME_COLOR)
        self.score_tracker.grid(column=2, row=1)
        # create buttons
        tick_image = PhotoImage(file="images/true.png")
        self.tick = Button(image=tick_image, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.true_pressed)
        self.tick.grid(column=1, row=3)

        cross_image = PhotoImage(file="images/false.png")
        self.cross = Button(image=cross_image, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.false_pressed)
        self.cross.grid(column=2, row=3)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz")
            self.tick.config(state="disabled")
            self.cross.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))
        self.score_tracker.config(text=f"Score: {self.quiz.score}")

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))
        self.score_tracker.config(text=f"Score: {self.quiz.score}")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


