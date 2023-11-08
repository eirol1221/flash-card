from tkinter import *
import random
import pandas as pd

# CONSTANTS
BG_COLOR = "#B1DDC6"
BLACK = "#000000"
WHITE = "#FFFFFF"
EN = "English"
FR = "French"
FONT_TITLE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")

# VARIABLES
rand_dict = {}

# -------------------------- GET RANDOM DATA --------------------------
def get_data():
    try:
        data = pd.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        data = pd.read_csv("data/french_words.csv")
    finally:
        return data.to_dict(orient="records")


# -------------------------- CHANGE FRENCH WORD IN THE CARD --------------------------
def random_french_word():
    global rand_dict

    data = get_data()
    rand_dict = random.choice(data)
    canvas.itemconfig(card_word, text=rand_dict[FR], fill=BLACK)
    canvas.itemconfig(card_title, text=FR, fill=BLACK)
    canvas.itemconfig(card_img, image=img_front)

    window.after(3000, flip_card, rand_dict[EN])


# -------------------------- FLIP CARD --------------------------
def flip_card(en_word):
    canvas.itemconfig(card_word, text=en_word, fill=WHITE)
    canvas.itemconfig(card_title, text=EN, fill=WHITE)
    canvas.itemconfig(card_img, image=img_back)


# -------------------------- REMOVE WORD FROM LIST --------------------------
def remove_card():
    global rand_dict

    new_dict = get_data()
    new_dict.remove(rand_dict)
    pd.DataFrame(new_dict).to_csv("data/words_to_learn.csv", index=False)
    random_french_word()


# -------------------------- UI SETUP --------------------------
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BG_COLOR)

# CANVAS
canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

img_front = PhotoImage(file="images/card_front.png")
img_back = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=img_front)

card_title = canvas.create_text(400, 150, font=FONT_TITLE)
card_word = canvas.create_text(400, 263, font=FONT_WORD)

# BUTTONS
right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, bg=BG_COLOR, borderwidth=0, command=remove_card)
right_btn.grid(row=1, column=1, pady=5)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, bg=BG_COLOR, borderwidth=0, command=random_french_word)
wrong_btn.grid(row=1, column=0, pady=5)

random_french_word()

window.mainloop()