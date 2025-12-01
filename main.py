from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_card)
lang_text = canvas.create_text(400, 150, text=f"French", fill="black", justify="center", font=("Arial", 30, "italic"))
lang_word_text = canvas.create_text(400, 250, text=f"Word", fill="black", justify="center", font=("Arial", 30, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()