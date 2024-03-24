"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word: str):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    #print("enter an un- word")
    #word = input()
    #print('un' + word)
    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with
    the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    #print("enter a list ['prefix', 'word1', 'word2']")
    #vocab_words = input()

    vocab_list: list = vocab_words[1:]
    prefix: str = vocab_words[0]

    glue: str = " :: " + prefix
    prefices: str = prefix + glue.join(vocab_list)
    #print(prefices)

    return prefix + " :: " + prefices


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    #print("enter a word ending in -ness")
    #word = input()

    if word[-5: ] == "iness":
        word = word[:len(word) - 5] + "y"
    elif word[-4:] == "ness":
        word = word[:len(word) - 4]
    else:
        word = "your word is not an -ness word."

    #print(word)
    return word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    last = sentence[-1]
    punc_bool = any([last == ".", last =="!", last == "?"])
    if punc_bool:
        sentence = sentence[:-1]
    #print("enter an sentence in quotes, a comma, and a number for where the adjective is.")
    #adj_to_verb_tuple = input()
    #adj_to_verb_tuple_list = adj_to_verb_tuple.split(", ")
    #sentence = adj_to_verb_tuple_list[0]
    #print(sentence)
    sentence_list = sentence.split()
    #print(sentence_list)
    #index = int(adj_to_verb_tuple_list[1])
    #print(index)
    adjective = sentence_list[index]
    #print(adjective)
    verb = adjective + "en"
    return verb
