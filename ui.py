from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface :

    def __init__(self,quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR,padx=20,pady=20)


        self.score_label = Label(text="Score : 0",foreground="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(background="white",width=300,height=250)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=250,
                                                     text="Some Question Text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)
        
        true_imge = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_imge,highlightthickness=0,command= self.true_perssed)
        self.true_button.grid(row=2,column=0)

        self.false_button = Button(image=false_image,highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2,column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(background = "white")
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text = q_text)
        else : 
            self.canvas.itemconfig(self.question_text,text= "You Have Reached the end of the Question List")  
            self.true_button.config(state="disabled")  

    def true_perssed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self,is_right):
        if is_right :
            self.canvas.config(background="green")
        else :
            self.canvas.config(background="red")  

        self.window.after(1000,self.get_next_question())