from tkinter import *
from forward import *
from viterbi import *
from nltk import word_tokenize
from utility import *


# Executes a version of either the Forward or Viterbi Algorithm based on what the user has selected
def execute():
    # If there is no sentence input, asks for a sentence input
    if len(sentence_input.get()) == 0:
        canvas.delete("all")
        canvas.create_text(375, 50, text="Please Enter a Sentence")
    # If there is an illegal word in the input, tells the user
    elif len(sentence_in_corpus(word_tokenize(sentence_input.get()))) > 0:
        canvas.delete("all")
        canvas.create_text(375, 50, text="Found an Illegal Word")
    # If the user has selected "Forward Algorithm", it shows the results of running the Forward
    # Algorithm on the entire sentence with only the most likely part of speech shown
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
    # If the user has selected "Viterbi Algorithm", it shows the results of running the Viterbi
    # Algorithm on the entire sentence
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
    # If the user has selected "Forward with All Parts of Speech", then it shows a trellis diagram for
    # all the parts of speech
    elif v.get() == "3":
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
    # If the user has selected "Show All Progressions for Forward", it shows the step progression after each word
    # is added
    elif v.get() == "4":
        canvas.delete("all")
        new_sentence = word_tokenize(sentence_input.get())
        for i in range(1, len(new_sentence) + 1):
            non_normalized_result = forward(set(pos_tags), new_sentence[:i], transition_matrix, emission_matrix)
            result = normalize(non_normalized_result)
            top_results = {}
            for j in range(len(new_sentence[:i])):
                highest = 0.0
                best_pos = None
                for pos in set(pos_tags):
                    if result[j][pos] >= highest:
                        best_pos = pos
                        highest = result[j][pos]
                top_results[new_sentence[j]] = best_pos, highest
            new_len = 100 * len(result[0])
            new_height = 60 * len(result) + 100
            if new_len > 750 or new_height > 750:
                canvas.config(height=new_height, width=new_len)
            for k in range(len(result)):
                canvas.create_rectangle(10 + 100 * k, 25, 100 + 100 * k, 75, fill="white")
                canvas.create_text(55 + 100 * k, 50, text=new_sentence[k])
                canvas.create_rectangle(10 + 100 * k, 30 + 60 * i, 100 + 100 * k, 75 + 60 * i, fill="lightblue")
                val = top_results[new_sentence[k]][0] + ": " + "{0:.4f}".format(top_results[new_sentence[k]][1])
                canvas.create_text(55 + 100 * k, 52 + 60 * i, text=val)
    # If the user has selected "Show All Progressions for Viterbi", it shows the step progression after each word
    # is added to the algorithm
    elif v.get() == "5":
        canvas.delete("all")
        new_sentence = word_tokenize(sentence_input.get())
        for i in range(1, len(new_sentence) + 1):
            result = viterbi(set(pos_tags), new_sentence[:i], transition_matrix, emission_matrix)
            new_len = 100 * len(result["predicted_tags"])
            new_height = 750
            if new_len > 750 or new_height > 750:
                canvas.config(height=new_len, width=new_len)
            for j in range(len(new_sentence[:i])):
                canvas.create_rectangle(10 + 100 * j, 25, 100 + 100 * j, 75, fill="white")
                canvas.create_text(55 + 100 * j, 50, text=new_sentence[j])
                canvas.create_rectangle(10 + 100 * j, 30 + 60 * i, 100 + 100 * j, 75 + 60 * i, fill="lightblue")
                canvas.create_text(55 + 100 * j, 52 + 60 * i, text=result["predicted_tags"][j + 1])


# Create the tkinter root and canvas to draw on
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
          "Show All Parts of Speech for Forward": "3",
          "Show All Progressions for Forward Algorithm": "4",
          "Show All Progressions for Viterbi Algorithm": "5"}

for (text, value) in values.items():
    Radiobutton(root, text=text, variable=v, value=value).pack()

sentence_input.pack()
test_button.pack()
canvas.pack()

root.mainloop()
