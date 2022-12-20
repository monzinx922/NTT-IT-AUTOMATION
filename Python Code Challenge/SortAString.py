# This function will separate word to words by spacific character
# input  : (string) word
# output : (list) list of words
def separate_word(word,separator):
    separated_word = ''
    list_separated_word = []
    for c in word:
        if c != separator:
            separated_word +=c
        else:
            list_separated_word.append(separated_word)
            separated_word = ''
    list_separated_word.append(separated_word)
    return list_separated_word

# This function will get list of word and sort it by ignore case
# input  : (list) word
# output : (string) word
def sort_words(word):

    # Separate the word into list
    list_separated_word = separate_word(word,' ')

    # Make list of separated word in lower case
    list_separated_word_lowercase = []
    for w in list_separated_word:
        lower_w = w.lower()
        list_separated_word_lowercase.append(lower_w)

    # Sort word in lower case list
    sorted_list_separated_word = sorted(list_separated_word_lowercase)

    # The answer is here, set it empty word
    sorted_word = ''

    # Check each word in list which has been sort in lower case
    for w in sorted_list_separated_word:
        # if the word is also in original word then add to answer and plus the separator, here is ' '
        if w in list_separated_word:
            sorted_word += w
            sorted_word += ' '
        # if the word is not in original word, use the word find its position in separate lower case list
        # then we get position of the word, use the position for the index of original list of word
        # and put it to answer string plus the separator ' '
        else:
            # get index of finding word
            w_index = list_separated_word_lowercase.index(w)
            # get number of word in list
            w_n = len(list_separated_word)
            sorted_word += list_separated_word[w_index]
            # if the index is not last position, answer can add separator
            if w_index != w_n-1:
                sorted_word += ' '

    return sorted_word

print(sort_words('banana ORANGE apple Mango Strawberry Lemon grape'))