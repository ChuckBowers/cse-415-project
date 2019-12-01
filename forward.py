"""
Authors:
    kjmasumo
    bowerw2
This is our implementation of the forward algorithm for part of speech tagging.
"""


possible_states = ['sunny', 'rainy']
states_i = [0, 1]
possible_observations = ['umbrella', 'no umbrella']
observed = [0, 0, 1, 1, 0]
emissions = [[0.2, 0.8], [0.9, 0.1]]  # [state][observation]
transitions = [[0.7, 0.3], [0.3, 0.7]]  # [state 1][state 2]
initial = [0.5, 0.5]  # initial observations


def forward(observations, states, initial_prob, transition_prob, emission_prob):
    probabilities = []

    # Create a results tables populated with 0.0
    for i in range(len(states)):
        row = []
        for j in range(len(observations)):
            row.append(0.0)
        probabilities.append(row)

    # Populate the first observation with the initial probability * the probability given the obs
    for state in states:
        probabilities[state][0] = initial_prob[state] * emission_prob[state][observations[0]]

    # Populate the rest of the observations with the forward algorithm
    for i in range(1, len(observations)):
        for t1 in states:
            probability = 0
            for t2 in states:
                probability += probabilities[t2][i - 1] * transition_prob[t1][t2]
            probabilities[t1][i] = probability * emission_prob[t1][observations[i]]
    return probabilities


def normalize(result):
    totals = []
    normalized_result = []
    for i in range(len(result[0])):
        total = 0
        for j in range(len(result)):
            total += result[j][i]
        totals.append(total)
    for i in range(len(result)):
        normalized_row = []
        for j in range(len(result[0])):
            normalized_row.append(result[i][j] / totals[j])
        normalized_result.append(normalized_row)
    return normalized_result


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


format(normalize(forward(observed, states_i, initial, transitions, emissions)), possible_states, states_i)
value = normalize(forward(observed, states_i, initial, transitions, emissions))
print(value)