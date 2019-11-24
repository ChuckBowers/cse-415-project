"""
Authors:
    kjmasumo
    bowerw2
This is our implementation of the forward algorithm for part of speech tagging.
"""


def forward (observations, states, initial_prob, transition_prob, emission_prob):
    probabilities = []
    for i in range(len(states)):
        row = []
        for j in range(len(observations)):
            row.append(0)
        probabilities.append(row)
