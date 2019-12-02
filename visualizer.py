from tkinter import *
from forward import *
from viterbi import *
from nltk import word_tokenize
import random


def execute():
    if len(sentence_input.get()) == 0:
        canvas.delete("all")
        canvas.create_text(375, 50, text="Please Enter a Sentence")
    elif v.get() == "1":
        canvas.delete("all")
        new_len = 100 * len(probs[0])
        new_height = 60 * len(probs) + 100
        if new_len > 750 or new_height > 750:
            canvas.config(height=new_height, width=new_len)
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
        new_sentence = word_tokenize(sentence_input.get())
        result = viterbi(distinct_tags, new_sentence, transition_matrix, emission_matrix)
        pos = result["predicted_tags"]
        valid_result = False
        # for i in range(len(pos)):
        #    if pos[i] is not None and pos[i] is not ':-':
        #        valid_result = True
        new_len = 100 * len(result["predicted_tags"])
        new_height = 750
        if new_len > 750 or new_height > 750:
            canvas.config(height=new_height, width=new_len)
        for i in range(len(new_sentence)):
            canvas.create_rectangle(10 + 100 * i, 25, 100 + 100 * i, 75, fill="white")
            canvas.create_text(55 + 100 * i, 50, text=new_sentence[i])
            canvas.create_rectangle(10 + 100 * i, 90, 100 + 100 * i, 135, fill="lightblue")
            canvas.create_text(55 + 100 * i, 112, text=result["predicted_tags"][i + 1])
        '''if not valid_result:
            canvas.delete("all")
            canvas.create_text(375, 50, text="Found an Illegal Word")'''
        print(result)

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
          "5000": "4",
          "All": "5"}

for (text, value) in values.items():
    Radiobutton(root, text=text, variable=v2, value=value).pack()

Label(root, text="Choose How Many of the Top Results You Would Like to See").pack()
v3 = StringVar(root, "1")
values = {"1": "1",
          "5": "2",
          "10": "3"}
for (text, value) in values.items():
    Radiobutton(root, text=text, variable=v3, value=value).pack()

sentence_input.pack()
test_button.pack()
canvas.pack()

root.mainloop()
