import nltk
from nltk.corpus import brown

# Define global set of words in corpus
corpus_words = set(brown.tagged_words())
print(corpus_words)
unique_corpus_words = [word.lower() for word, tag in corpus_words]

# Returns the transition probability matrix and the emission probability matrix based upon all words
# from the Brown Corpus. Return value is a dictionary with two keys, 'transition' with the value being the
# transition probability matrix and 'emission' with the value veing the emission probability matrix.
def probability_matrices():
    # Modify the POS tags by using only the first two letters of a tag,
    # which represent the broad class of POS tags in the Brown corpus.
    # Also switch the order of word tag pairs to be tag word to conform
    # with transition and emission probabilities. Add a leading period
    # to give the first sentence in the corpus a starting transition
    # probability.
    tagged_corpus = [(".", ".")]
    for sentence in brown.tagged_sents():
        tagged_corpus.extend([(tag[:2], word.lower()) for (word, tag) in sentence])

    # Create the transition probability matrix
    # Transition probability: P(xt | x{t-1})
    pos_tags = [tag for (tag, word) in tagged_corpus]
    transition_cond_freq_dist = nltk.ConditionalFreqDist(nltk.bigrams(pos_tags))
    transition_matrix = nltk.ConditionalProbDist(transition_cond_freq_dist, nltk.MLEProbDist)

    # Create the emission probability matrix
    # Emission probability: P(yt | xt)
    emission_cond_freq_dist = nltk.ConditionalFreqDist(tagged_corpus)
    emission_matrix = nltk.ConditionalProbDist(emission_cond_freq_dist, nltk.MLEProbDist)

    return {"transition": transition_matrix, "emission": emission_matrix, "tags": pos_tags}


# Returns True if word exists in Brown Corpus, False if not
def _word_in_corpus(input_word):
    global unique_corpus_words
    for word in unique_corpus_words:
        if word == input_word.lower():
            return True
    return False


# Returns [] if all words exist in Brown Corpus, otherwise words contained in list were words from the input_sentence
# that do not exist in the Brown Corpus
def sentence_in_corpus(input_sentence):
    dont_exist = []
    for word in input_sentence:
        if not _word_in_corpus(word):
            dont_exist.append(word)
    return dont_exist
