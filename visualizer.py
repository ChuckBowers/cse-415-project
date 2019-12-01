from tkinter import *
from forward import *
import random


def execute():
    if len(sentence_input.get()) == 0:
        canvas.delete("all")
        canvas.create_text(375, 50, text="Please Enter a Sentence")
    elif v.get() == "1":
        canvas.delete("all")
        for i in range(len(probs[0])):
            canvas.create_rectangle(10 + 100 * i, 25, 100 + 100 * i, 75, fill="white")
            canvas.create_text(55 + 100 * i, 50, text=possible_observations[observed[i]])
            for j in range(len(probs)):
                color = None
                if probs[j][i] > 0.8:
                    color = "#98fa7a"
                elif probs[j][i] <= 0.8 and probs[j][i] > 0.6:
                    color = "#f5f242"
                else:
                    color = "#ff8f8f"
                val = str(possible_states[j]) + ": " + "{0:.3f}".format(probs[j][i])
                canvas.create_rectangle(10 + 100 * i, 90 + 50 * j, 100 + 100 * i, 135 + 50 * j, fill=color)
                canvas.create_text(55 + 100 * i, 112 + 50 * j, text=val)
    elif v.get() == "2":
        canvas.delete("all")


root = Tk()
root.geometry("750x750")
root.title("Hidden Markov Model for Part-of-Speech Tagging")
sentence_input = Entry(root)
canvas = Canvas(root, bd=0, height=750, width=750)

test_button = Button(root, text="Run With These Settings", command=lambda: execute())

Label(root, text="Choose Which Algorithm You Want To Run").pack()
v = StringVar(root, "1")
values = {"Forward": "1",
          "Viterbi": "2"}

for (text, value) in values.items():
    Radiobutton(root, text=text, variable=v, value=value).pack()


Label(root, text="Choose How Many Words From the Corpus You Would Like to Use").pack()
v2 = StringVar(root, "1")
values = {"100": "1",
          "500": "2",
          "1000": "3",
          "5000": "4"}

for (text, value) in values.items():
    Radiobutton(root, text=text, variable=v2, value=value).pack()

Label(root, text="Choose How Many of the Top Results You Would Like to See").pack()
v3 = StringVar(root, "1")
values = {"1": "1",
          "5": "2",
          "10": "3",
          "15": "4"}
for (text, value) in values.items():
    Radiobutton(root, text=text, variable=v3, value=value).pack()

sentence_input.pack()
test_button.pack()
canvas.pack()

root.mainloop()