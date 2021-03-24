from tkinter import *
import pandas
from random import randint
from csv import writer, reader

data = pandas.read_csv("data/japanese.csv")

# -----------------

FONT = "Bahnschrift"
BACKGROUND_COLOR = "#B1DDC6"


class Card:
    def front(self):
        card.itemconfig(card_image, image=image_front)
        card.itemconfig(language, text="Japanese", fill="black")
        card.itemconfig(word, text=self.new_kana, fill="black")
        card.itemconfig(expression, text=self.new_expression, fill="black")

    def back(self):
        card.itemconfig(card_image, image=image_back)
        card.itemconfig(language, text="English", fill="white")
        card.itemconfig(word, text=self.new_meaning, fill="white")
        card.itemconfig(expression, text="")

    def new_card(self):
        self.i = randint(0, 6000)
        self.new_kana = data.kana[self.i]
        self.new_expression = data.expression[self.i]
        self.new_meaning = data.meaning[self.i]
        self.learned_words = [
            str(self.i),
            self.new_expression,
            self.new_kana,
            self.new_meaning,
        ]
        with open("data/learned.csv", encoding="utf-8") as f:
            dt = reader(f)
            learned_list = list(dt)
            print(learned_list)
            print(f"\n\n{self.learned_words}")
            if self.learned_words in learned_list:
                self.new_card()
                print("deu certo")
            else:
                self.front()
                

    def save_csv(self):
        with open("data/learned.csv", "a+", newline="", encoding="utf-8") as write_obj:
            csv_writer = writer(write_obj)
            csv_writer.writerow(self.learned_words)
        self.new_card()


window = Tk()
window.config(padx=100, pady=100, bg=BACKGROUND_COLOR)
window.title("Japanese Flash Cards")

image_front = PhotoImage(file="images/card_front.png")
image_back = PhotoImage(file="images/card_back.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = card.create_image(400, 263)
language = card.create_text(400, 50, font=(FONT, 30))
word = card.create_text(400, 250, font=(FONT, 60, "bold"), width=700)
expression = card.create_text(400, 430, font=(FONT, 40, "bold"))
new = Card()
new.new_card()
card.grid(column=1, row=1, columnspan=3)

flip_button = Button()
flip_button.config(text="Flip Card", width=20, command=new.back)
flip_button.grid(column=2, row=2)

right_button = Button()
right_button.config(
    image=right_image,
    width=100,
    height=100,
    highlightthickness=0,
    command=new.save_csv,
)
right_button.grid(column=3, row=2)

wrong_button = Button()
wrong_button.config(
    image=wrong_image,
    width=100,
    height=100,
    highlightthickness=0,
    command=new.new_card,
)
wrong_button.grid(column=1, row=2)


window.mainloop()
