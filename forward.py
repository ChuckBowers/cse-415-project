"""
Authors:
    kjmasumo
    bowerw2
This is our implementation of the forward algorithm for part of speech tagging.
"""


# Takes in a list of all possible states, all of the observations, and a transition and emission probability matrices
# and returns a list of dictionaries that represents the results of the forward algorithm
def forward(states, observations, transition_prob, emission_prob):
    probabilities = []
    # Create a list of dictionaries that contain the results
    for i in range(len(observations)):
        probabilities.append({})
    # Populate the first observation (word) with the emission values
    for state in states:
        probabilities[0][state] = emission_prob[state].prob(observations[0].lower())
    # Populate the rest of the table with values from the forward algorithm
    for i in range(1, len(observations)):
        for t2 in states:
            probability = 0.0
            for t1 in states:
                probability += probabilities[i - 1][t1] * transition_prob[t1].prob(t2)
            probabilities[i][t2] = probability * emission_prob[t2].prob(observations[i].lower())
    return probabilities


# Takes in a result that is a list of dictionaries and normalizes all of the probabilities in the result table
def normalize(result):
    totals = []
    normalized = []
    for i in range(len(result)):
        total = 0.0
        for tag in result[i]:
            total += result[i][tag]
        totals.append(total)
    for i in range(len(result)):
        normalized_dict = {}
        for tag in result[i]:
            normalized_dict[tag] = result[i][tag] / totals[i]
        normalized.append(normalized_dict)
    return normalized


# Formats the result into a nice-looking print-out
def format(result, poss_states, states_index):
    print("\t", end="")
    for i in range(len(result[0])):
        print("\t", end="")
        print("Obs", end="")
        print(i + 1, end="")
    print("")
    for index in states_index:
        print(poss_states[index], end="")
        for i in range(len(result[0])):
            print("\t", end="")
            print("{0:.4f}".format(result[index][i]), end="")
        print("")
