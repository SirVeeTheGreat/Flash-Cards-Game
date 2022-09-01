import random
from tkinter import *
from tkinter import Canvas

import pandas

e_word = ''
card = ''
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.geometry('1000x700')
window.config(bg=BACKGROUND_COLOR, pady=50, padx=101)
cards = []
try:
    data = pandas.read_csv('data/words_to_learn.csv')
    data_dic = data.to_dict(orient='records')
    cards = data_dic
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
    data_dic = data.to_dict(orient='records')
    cards = data_dic


def get_card():
    global e_word, flip_timer, card
    window.after_cancel(flip_timer)
    card = random.choice(data_dic)
    f_word = card['French']
    e_word = card['English']
    canvas.itemconfig(card_word, fill='black', text=f_word)
    canvas.itemconfig(card_title, fill='black', text='French')
    canvas.itemconfig(front_card, image=old_image)
    flip_timer = window.after(3000, change_image)


def words_to_learn():
    get_card()
    cards.remove(card)
    print(len(cards))
    new_dic = pandas.DataFrame(cards)
    new_dic.to_csv('data/words_to_learn.csv', index=False, mode='w')


def change_image():
    canvas.itemconfig(card_word, fill='white', text=e_word)
    canvas.itemconfig(card_title, fill='white', text='English')
    canvas.itemconfig(front_card, image=new_image)


flip_timer = window.after(3000, change_image)

canvas: Canvas = Canvas(width=800, height=528)
old_image = PhotoImage(file='images/card_front.png')
new_image = PhotoImage(file='images/card_back.png')

front_card = canvas.create_image(400, 269, image=old_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

button_right_image = PhotoImage(file='images/right.png')
button_right = Button(image=button_right_image, borderwidth=0, highlightthickness=0, command=words_to_learn)
button_right.grid(column=1, row=1)

button_left_image = PhotoImage(file='images/wrong.png')
button_left = Button(image=button_left_image, borderwidth=0, highlightthickness=0, command=get_card)
button_left.grid(column=0, row=1)

canvas2 = Canvas()
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))

get_card()

window.mainloop()
