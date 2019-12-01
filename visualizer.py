from tkinter import *
from forward import *
import random

'''class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        # setting the initial size of the widget
        self.master.geometry("500x500")

        # changing the title of our master widget
        self.master.title("Hidden Markov Model for Part-of-Speech Tagging")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quit_button = Button(self, text="Hello")

        # placing the button on my window
        quit_button.place(x=0, y=0)'''


def test():
    print("TEST")


def test2():
    print("TEST2")


def test3(inp):
    print(inp)


def test4():
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    canvas.create_rectangle(x - 15, y - 15, x + 15, y + 15, fill="white")
    canvas.create_text(x, y, text=sentence_input.get())
    print(sentence_input.get())


def execute():
    for i in range(len(probs[0])):
        canvas.create_rectangle(10 + 100 * i, 25, 100 + 100 * i, 75, fill="white")
        canvas.create_text(55 + 100 * i, 50, text=possible_observations[observed[i]])
        for j in range(len(probs)):
            color = None
            if j == 0:
                color = "yellow"
            else:
                color = "green"
            val = str(possible_states[j]) + ": " + "{0:.3f}".format(probs[j][i])
            canvas.create_rectangle(10 + 100 * i, 90 + 50 * j, 100 + 100 * i, 135 + 50 * j, fill=color)
            canvas.create_text(55 + 100 * i, 112 + 50 * j, text=val)


root = Tk()
root.geometry("750x750")
root.title("Hidden Markov Model for Part-of-Speech Tagging")
sentence_input = Entry(root)
canvas = Canvas(root, bg="lightblue", bd=0, height=750, width=750)

test_button = Button(root, text="TEST", command=lambda: execute())

'''menu = Menu(root)
root.config(menu=menu)
algorithm = Menu(menu)
algorithm.add_checkbutton(label="Forward Algorithm", command=test)
algorithm.add_checkbutton(label="Viterbi Algorithm", command=test)
menu.add_cascade(label="Algorithm", menu=algorithm)
words_from_corpus = Menu(menu)
words_from_corpus.add_checkbutton(label="100", command=test2, onvalue=1, offvalue=0)
words_from_corpus.add_checkbutton(label="1000", command=test2, onvalue=1, offvalue=0)
words_from_corpus.add_checkbutton(label="5000", command=test2, onvalue=1, offvalue=0)
words_from_corpus.add_checkbutton(label="10000", command=test2, onvalue=1, offvalue=0)
menu.add_cascade(label="Words From Corpus", menu=words_from_corpus)
top_x_outputs = Menu(menu)
top_x_outputs.add_checkbutton(label="1", command=test)
top_x_outputs.add_checkbutton(label="5", command=test)
top_x_outputs.add_checkbutton(label="10", command=test)
top_x_outputs.add_checkbutton(label="15", command=test)
menu.add_cascade(label="Number of Outputs Shown", menu=top_x_outputs)'''

v = StringVar(root, "1")

# Dictionary to create multiple buttons
values = {"Forward": "1",
          "Viterbi": "2"}

# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(root, text=text, variable=v, value=value).pack(side=TOP, ipady=5)

v2 = StringVar(root, "1")
values = {"100": "1",
          "500": "2",
          "1000": "3",
          "5000": "4"}

for (text, value) in values.items():
    Radiobutton(root, text=text, variable=v2, value=value).pack(side=TOP, ipady=5)

v3 = StringVar(root, "1")
values = {"1": "1",
          "5": "2",
          "10": "3",
          "15": "4"}
for (text, value) in values.items():
    Radiobutton(root, text=text, variable=v3, value=value).pack(side=TOP, ipady=5)

sentence_input.pack()
test_button.pack()
canvas.pack()

root.mainloop()