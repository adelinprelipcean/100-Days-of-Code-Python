from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, question_text):
        self.score = 0
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR)
        
        self.score = Label(self.window,
                           text=f'Score: {self.score}',
                           bg=THEME_COLOR, fg='white',
                           font=('Arial', 18))
        self.score.grid(column=2, row=1, padx=20, pady=20)
        
        self.canvas = Canvas(self.window, height=250, width=300, bg='grey')
        self.typed_value = self.canvas.create_text(150, 125, 
                                                   text=question_text, 
                                                   font=('Arial', 20, 'italic'),
                                                   anchor='center',
                                                   width=280)
        self.canvas.grid(column=1, row=2, columnspan=2, padx=20, pady=20)
        
        self.right_image = PhotoImage(file='./images/true.png')
        self.right_button = Button(image=self.right_image)
        self.right_button.grid(column=1, row=3, padx=20, pady=20)
        
        self.wrong_image = PhotoImage(file='./images/false.png')
        self.wrong_button = Button(image=self.wrong_image)
        self.wrong_button.grid(column=2, row=3, padx=20, pady=20)
        
        self.window.mainloop()