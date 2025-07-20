"""A simple flashcard app to learn French vocabulary using Tkinter and Pandas.
- Shows a French word and reveals the English translation after 5 seconds.
- ✅ = I knew it → removes the word from the list.
- ❌ = I didn't know it → adds it to a review list.
- Quit button saves wrong answers to 'review_words.csv' for later practice.
- Next time you start the app, it will load your review words.
TODO: remove words from review_words.csv after you learn them and reload the 
      french_words.csv when empty"""

import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.resizable(False, False)

try:
    data = pandas.read_csv('data/review_words.csv')
    if data.empty:
        raise ValueError
except:
    data = pandas.read_csv('data/french_words.csv')
    
words_no = data.index.tolist()

wrong_words = {
            'French': [],
            'English': []
        }

def generate_word():
    global words_no, data
    
    if len(words_no) == 0:
        try:
            data = pandas.read_csv('data/review_words.csv')
            if data.empty:
                raise ValueError
        except:
            data = pandas.read_csv('data/french_words.csv')
        words_no = data.index.tolist()
        
    word_no = random.choice(words_no)
    
    flashcard = tk.Canvas(window, bg=BACKGROUND_COLOR, height=526, width=800, highlightthickness=0)
    card_front = tk.PhotoImage(file='images/card_front.png')
    flashcard.card_front_img = card_front
    flashcard_image = flashcard.create_image(0, 0, anchor='nw', image=card_front)
    flashcard_title = flashcard.create_text(400, 150, text=data.columns[0], font=('Arial', 40, 'italic'))
    flashcard_word = flashcard.create_text(400, 263, text=data['French'][word_no], font=('Arial', 60, 'bold'))
    flashcard.grid(row=0, column=0, columnspan=2)


    def right_answer():
        words_no.remove(word_no)
        generate_word()
        
        
    def wrong_answer():
        wrong_words['French'].append(data['French'][word_no])
        wrong_words['English'].append(data['English'][word_no])
        generate_word()
        
    
    def done():
        if len(wrong_words['French']) > 0:
            pandas.DataFrame.from_dict(wrong_words).to_csv('data/review_words.csv', index=False)
        else:
            open('data/review_words.csv', 'w').close()
        quit()
    
    
    wrong_image = tk.PhotoImage(file='images/wrong.png')
    wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=wrong_answer)
    wrong_button.image = wrong_image
    wrong_button.grid(row=1, column=0)
    
    right_image = tk.PhotoImage(file='images/right.png')
    right_button = tk.Button(image=right_image, highlightthickness=0, command=right_answer)
    right_button.image = right_image
    right_button.grid(row=1, column=1)
    
    right_button = tk.Button(text='Quit', highlightthickness=0, bg=BACKGROUND_COLOR, width=10, command=done)
    right_button.place(x=375, y=530)
    
    
    def translate():
        card_back = tk.PhotoImage(file='images/card_back.png')
        flashcard.card_back_img = card_back
        flashcard.itemconfig(flashcard_image, image=card_back)
        flashcard.itemconfig(flashcard_title, text=data.columns[1])
        flashcard.itemconfig(flashcard_word, text=data['English'][word_no])
        
    window.after(5000, translate)

generate_word()

    
window.mainloop()