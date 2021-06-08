import random
from tkinter import *
round_time = 60
n_chars = 50
w, h = 1000, 700
words = []
with open("4000words.csv", "r") as file:
    words = [w[:-1] for w in file.readlines()]
    random.shuffle(words)

def game(tk):
    text = ""
    i = 0
    while len(text) < n_chars:
        text += words[i] + " "
        i += 1
    t = Text(tk, bg="gray", width=30, height=3)
    t.config(font=("Arial", 30))
    t.insert(END, "some text", fc)
    t.place(x=w//2, y=h//2, anchor=CENTER)

def restart_game(tk):
    for s in tk.grid_slaves():
        s.destroy()

if __name__ == "__main__":
    tk = Tk()
    tk.geometry("1000x700")
    restart_game(tk)
    game(tk)
    tk.mainloop()