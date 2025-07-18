import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.resizable(False, False)
words_no = [i for i in range(1, 101)]

def generate_word():
    try:
        data = pandas.read_csv('data/french_words.csv')
        word_no = random.choice(words_no)
        print(words_no)
        
        flashcard = tk.Canvas(window, bg=BACKGROUND_COLOR, height=526, width=800, highlightthickness=0)
        card_front = tk.PhotoImage(file='images/card_front.png')
        flashcard.card_front_img = card_front
        flashcard.create_image(0, 0, anchor='nw', image=card_front)
        flashcard_title = flashcard.create_text(400, 150, text=data.columns[0], font=('Arial', 40, 'italic'))
        flashcard_word = flashcard.create_text(400, 263, text=data['French'][word_no], font=('Arial', 60, 'bold'))
        flashcard.grid(row=0, column=0, columnspan=2)

        def right_answer():
            words_no.remove(word_no)
            generate_word()
        
        wrong_image = tk.PhotoImage(file='images/wrong.png')
        wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=generate_word)
        wrong_button.image = wrong_image
        wrong_button.grid(row=1, column=0)
        
        right_image = tk.PhotoImage(file='images/right.png')
        right_button = tk.Button(image=right_image, highlightthickness=0, command=right_answer)
        right_button.image = right_image
        right_button.grid(row=1, column=1)
        
        
        def translate():
            flashcard.itemconfig(flashcard_title, text=data.columns[1])
            flashcard.itemconfig(flashcard_word, text=data['English'][word_no])
            
        window.after(5000, translate)
    except IndexError:
        print('No more words!')

generate_word()

    
window.mainloop()