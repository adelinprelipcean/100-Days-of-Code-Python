import tkinter as tk
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.geometry('900x600')
window.config(bg=BACKGROUND_COLOR)

def generate_word():
    flashcard = tk.Canvas(window, bg=BACKGROUND_COLOR, height=520, width=804, highlightthickness=0)
    card_front = tk.PhotoImage(file="images/card_front.png")
    flashcard.card_front_img = card_front
    flashcard.create_image(0, 0, anchor='nw', image=card_front)
    flashcard.place(x=47, y=10)
    
    data = pandas.read_csv('data/french_words.csv')

    language_label = tk.Label(window, text=data.columns[0], bg='white', font=('Arial', 24))
    language_label.place(x=400, y=100)
    
    index = random.randint(0, 100)
    
    word_label = tk.Label(window, text=data['French'][index], bg='white', font=('Arial', 24, 'bold'))
    word_label.place(x=400, y=250)
    
    def translate():
        language_label.config(text=data.columns[1])
        word_label.config(text=data['English'][index])

    window.after(2000, translate)
    
    wrong_image = tk.PhotoImage
    red_button = tk.Button(window, text='Wrong', bg='red', command=generate_word)
    red_button.place(x=700, y=550)
    green_button = tk.Button(window, text='Correct', bg='green', command=generate_word)
    green_button.place(x=150, y=550)

generate_word()

window.mainloop()