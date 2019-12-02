

# Implement the Viterbi algorithm.
# Takes in four parameters: 1) a set of unique tags, 2) the provided sentence as a list, 3) a transition probability
# matrix, and 4) an emission probability matrix. Returns a dictionary with the first value 'predicted_tags' being the
# tags predicted for the given sentence and the second 'probability' being the probability that the 'predicted_tags'
# are correct.
def viterbi(tags, sent, transition, emission):
    lower_sent = [word.lower() for word in sent]
    # In the Stanford pseudo-code, tag_probs is 'viterbi' and actual_tags is 'backpointer'
    tag_probs = [{}]
    actual_tags = [{}]

    # Initialization step
    for tag in tags:
        tag_probs[0][tag] = transition["."].prob(tag) * emission[tag].prob(lower_sent[0])
        actual_tags[0][tag] = None

    # Recursion step
    for index in range(1, len(lower_sent)):
        this_tag_prob = {}
        this_actual_tag = {}
        prev_tag_prob = tag_probs[-1]

        for tag in tags:
            best_prev = max(prev_tag_prob.keys(),
                            key=lambda prev_tag: prev_tag_prob[prev_tag] * transition[prev_tag].prob(tag) *
                            emission[tag].prob(lower_sent[index]))
            this_actual_tag[tag] = best_prev
            this_tag_prob[tag] = prev_tag_prob[best_prev] * transition[best_prev].prob(tag) * \
                                 emission[tag].prob(lower_sent[index])

        tag_probs.append(this_tag_prob)
        actual_tags.append(this_actual_tag)

    # Termination step
    prev_tag_prob = tag_probs[-1]
    best_prev = max(prev_tag_prob.keys(),
                    key=lambda prev_tag: prev_tag_prob[prev_tag] * transition[prev_tag].prob("."))
    best_tags_prob = prev_tag_prob[best_prev] * transition[best_prev].prob(".")
    # best_tags is the list of tags or hidden states that will be returned
    best_tags = [".", best_prev]

    # Go backwards through actual_tags to figure out best tag for each word
    # and populate best_tags
    actual_tags.reverse()
    this_best_tag = best_prev
    for tag in actual_tags:
        best_tags.append(tag[this_best_tag])
        this_best_tag = tag[this_best_tag]
    # Reverse best_tags to match pos tags with word order
    best_tags.reverse()

    return {"predicted_tags": best_tags, "probability": best_tags_prob}


