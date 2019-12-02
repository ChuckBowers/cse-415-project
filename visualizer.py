"""
Authors:
    kjmasumo
    bowerw2
This file contains the code to run the user interface in a new window. To interact with our program, navigate to the
directory that contains this file in the terminal and enter 'python3 visualizer.py'.
"""


from tkinter import *
from forward import *
from viterbi import *
from nltk import word_tokenize
from utility import *
import random
from utility import *
import time


def execute():
    if len(sentence_input.get()) == 0:
        canvas.delete("all")
        canvas.create_text(375, 50, text="Please Enter a Sentence")
    elif len(sentence_in_corpus(word_tokenize(sentence_input.get()))) > 0:
        canvas.delete("all")
        canvas.create_text(375, 50, text="Found an Illegal Word")
    elif v.get() == "1":
        canvas.delete("all")
        new_sentence = word_tokenize(sentence_input.get())
        non_normalized_result = forward(set(pos_tags), new_sentence, transition_matrix, emission_matrix)
        result = normalize(non_normalized_result)
        top_results = {}
        for i in range(len(new_sentence)):
            highest = 0.0
            best_pos = None
            for pos in set(pos_tags):
                if result[i][pos] >= highest:
                    best_pos = pos
                    highest = result[i][pos]
            top_results[new_sentence[i]] = best_pos, highest
        new_len = 100 * len(result[0])
        new_height = 60 * len(result) + 100
        if new_len > 750 or new_height > 750:
            canvas.config(height=new_height, width=new_len)
        for i in range(len(result)):
            canvas.create_rectangle(10 + 100 * i, 25, 100 + 100 * i, 75, fill="white")
            canvas.create_text(55 + 100 * i, 50, text=new_sentence[i])
            canvas.create_rectangle(10 + 100 * i, 90, 100 + 100 * i, 135, fill="lightblue")
            val = top_results[new_sentence[i]][0] + ": " + "{0:.4f}".format(top_results[new_sentence[i]][1])
            canvas.create_text(55 + 100 * i, 112, text=val)
            '''j = 0
            for pos in result[i]:
                val = str(pos) + ": " + "{0:.3f}".format(result[i][pos])
                canvas.create_rectangle(10 + 100 * i, 90 + 50 * j, 100 + 100 * i, 135 + 50 * j, fill="lightblue")
                canvas.create_text(55 + 100 * i, 112 + 50 * j, text=val)
                j += 1
                #color = None
                #if result[j][i] > 0.8:
                #    color = "#98fa7a"
                #elif result[j][i] <= 0.8 and result[j][i] > 0.6:
                #    color = "#f5f242"
                #else:
                #    color = "#ff8f8f"
                #val = str(pos_tags[j]) + ": " + "{0:.3f}".format(result[j][i])
                #canvas.create_rectangle(10 + 100 * i, 90 + 50 * j, 100 + 100 * i, 135 + 50 * j, fill=color)
                #canvas.create_text(55 + 100 * i, 112 + 50 * j, text=val)'''
    elif v.get() == "2":
        canvas.delete("all")
        new_sentence = word_tokenize(sentence_input.get())
        result = viterbi(set(pos_tags), new_sentence, transition_matrix, emission_matrix)
        new_len = 100 * len(result["predicted_tags"])
        new_height = 750
        if new_len > 750 or new_height > 750:
            canvas.config(height=new_height, width=new_len)
        for i in range(len(new_sentence)):
            canvas.create_rectangle(10 + 100 * i, 25, 100 + 100 * i, 75, fill="white")
            canvas.create_text(55 + 100 * i, 50, text=new_sentence[i])
            canvas.create_rectangle(10 + 100 * i, 90, 100 + 100 * i, 135, fill="lightblue")
            canvas.create_text(55 + 100 * i, 112, text=result["predicted_tags"][i + 1])
    elif v.get() =="3":
        canvas.delete("all")
        new_sentence = word_tokenize(sentence_input.get())
        non_normalized_result = forward(set(pos_tags), new_sentence, transition_matrix, emission_matrix)
        result = normalize(non_normalized_result)
        print(result)
        new_len = 100 * len(result)
        new_height = 60 * len(result[0]) + 100
        if new_len > 750 or new_height > 750:
            canvas.config(height=new_height, width=new_len)
        for i in range(len(result)):
            canvas.create_rectangle(10 + 100 * i, 25, 100 + 100 * i, 75, fill="white")
            canvas.create_text(55 + 100 * i, 50, text=new_sentence[i])
            j = 0
            for pos in result[i]:
                val = str(pos) + ": " + "{0:.3f}".format(result[i][pos])
                canvas.create_rectangle(10 + 100 * i, 90 + 50 * j, 100 + 100 * i, 135 + 50 * j, fill="lightblue")
                canvas.create_text(55 + 100 * i, 112 + 50 * j, text=val)
                j += 1


root = Tk()
root.geometry("750x750")
root.title("Hidden Markov Model for Part-of-Speech Tagging")
sentence_input = Entry(root)
canvas = Canvas(root, bd=0, height=750, width=750)

test_button = Button(root, text="Run With These Settings", command=lambda: execute())

Label(root, text="Choose Which Algorithm You Want To Run").pack()
v = StringVar(root, "1")
values = {"Forward": "1",
          "Viterbi": "2",
          "Show All Parts of Speech": "3"}

for (text, value) in values.items():
    Radiobutton(root, text=text, variable=v, value=value).pack()

sentence_input.pack()
test_button.pack()
canvas.pack()

root.mainloop()
