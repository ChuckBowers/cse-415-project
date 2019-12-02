"""
Authors:
    kjmasumo
    bowerw2
This is our implementation of the forward algorithm for part of speech tagging.
"""

def forward(states, observations, transition_prob, emission_prob):
    probabilities = []
    for i in range(len(observations)):
        probabilities.append({})
    for state in states:
        probabilities[0][state] = emission_prob[state].prob(observations[0].lower())
    for i in range(1, len(observations)):
        for t2 in states:
            probability = 0.0
            for t1 in states:
                probability += probabilities[i - 1][t1] * transition_prob[t1].prob(t2)
            probabilities[i][t2] = probability * emission_prob[t2].prob(observations[i].lower())
    return probabilities
'''def forward(states, observations, transition_prob, emission_prob):
    probabilities = []
    for i in range(len(states)):
        row = []
        for j in range(len(observations)):
            row.append(0.0)
        probabilities.append(row)
    counter = 0
    for state in states:
        probabilities[counter][0] = emission_prob[state].prob(observations[0].lower())
        counter += 1
    for i in range(1, len(observations)):
        t1_counter = 0
        for t1 in states:
            probability = 0
            t2_counter = 0
            for t2 in states:
                probability += probabilities[t2_counter][i - 1] * transition_prob[t1].prob(t2)
                t2_counter += 1
            probabilities[t1_counter][i] = probability * emission_prob[t1].prob(observations[i].lower())
            t1_counter += 1
    return probabilities'''


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

'''def normalize(result):
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
            t = totals[j]
            if t == 0:
                t = 1
            normalized_row.append(result[i][j] / t)
        normalized_result.append(normalized_row)
    return normalized_result'''


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


#format(normalize(forward(observed, states_i, transitions, emissions)), possible_states, states_i)
# probs = normalize(forward(observed, states_i, transitions, emissions))
# print(probs)