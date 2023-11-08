from tkinter import *
import random
import pandas as pd

# CONSTANTS
BG_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")

# VARIABLES


# -------------------------- GET DATA --------------------------
def get_data():
    data = pd.read_csv("data/french_words.csv")
    return data.to_dict(orient="records")

# -------------------------- CHANGE FRENCH WORD IN THE CARD --------------------------
def random_french_word():
    fr_en_dict = get_data()
    rand_dict = random.choice(fr_en_dict)
    rand_word_fr = rand_dict['French']
    canvas.itemconfig(fr_word, text=rand_word_fr)
    canvas.itemconfig(fr_title, text="French")


# -------------------------- UI SETUP --------------------------
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BG_COLOR)

# CANVAS
canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

back_img = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=back_img)

front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_img)

fr_title = canvas.create_text(400, 150, font=FONT_TITLE)

fr_word = canvas.create_text(400, 263, font=FONT_WORD)

# BUTTONS
right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, bg=BG_COLOR, borderwidth=0, command=random_french_word)
right_btn.grid(row=1, column=1, pady=5)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, bg=BG_COLOR, borderwidth=0, command=random_french_word)
wrong_btn.grid(row=1, column=0, pady=5)

get_data()
random_french_word()

window.mainloop()