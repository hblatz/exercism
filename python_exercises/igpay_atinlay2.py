# def translate(str_phrase: str) -> str:
""" Pig latin logic
"""

print("enter a phrase:")
str_phrase = input()
# print("your starting phrase is " + str_phrase)

"""Remove whitespace and check if strPhrase is empty."""
str_phrase = str_phrase.strip()
if not str_phrase:  # Check for empty inputs.
    print("empty")
    # return str_phrase

"""Initialize output string by setting to empty."""
str_igpay_atinlay: str = ""

"""Parce sentence into words."""
for str_word in str_phrase.split():
    """Initialize for routine variables"""
    str_front_quote: str = ""
    str_punc: str = ""
    str_back_quote: str = ""

    """Check for quotation marks, " or'."""
    bool_front_quote: bool = str_word[0] == '\"' or str_word[0] == "\'"
    if bool_front_quote:
        str_front_quote = str_word[0]  # Saves last character.
        str_word = str_word[1:]  # Shortens word by one character.

    bool_back_quote: bool = str_word[-1] == '\"' or str_word[-1] == "\'"
    if bool_back_quote:
        str_back_quote = str_word[-1]  # Saves last character.
        str_word = str_word[:-1]  # Shortens word removing last letter.

    """ Check for a leading capital letter """
    bool_capitalized: bool = str_word[0].isupper()  # True if first character is capitalized
    # This also making the other characters in the word lower case, as in McCall --> Mccall.

    """Check for punctuation at end of word and save it.
    NOTE this routine checks for the end quote and then punctuation but not 
    punctuation then end quote."""
    char: str = str_word[-1]  # Saves last character of word to variable.

    punc_list = [char == ".", char == "?", char == "!", char == ".", char == ",", char == ";", char == ":"]
    bool_punc: bool = any(punc_list)

    if bool_punc:
        str_punc = char  # Saves last character as punctuation to add back later.
        str_word = str_word[:-1]  # Shortens word by one character.

    """Find first vowel in word, int_lead_vowel."""
    int_word_length: int = len(str_word)
    for i in range(0, int_word_length - 1):
        char = str_word[0]
        vowel_list = [char == "a", char == "e", char == "i", char == "o", char == "u"]
        if not any(vowel_list):
            if char == "q":
                if str_word[1] == "u":
                    str_word = str_word[2:] + str_word[0:2]
                else:
                    str_word = str_word[1:] + char
            elif char == "y":
                if i == 0:
                    if str_word [1] == "t":
                        break
                    else:
                        str_word = str_word[1:] + char
                else:
                    break
            elif str_word[:2] == "xr":
                break
            else:
                str_word = str_word[1:] + char
        else:
            break

    if bool_capitalized:
        str_word = str_word.capitalize()
    """Appends space and new word to output.
    NOTE that the first word has a space to be stripped off."""
    str_igpay_atinlay = str_igpay_atinlay + " " + str_front_quote + str_word + "ay" + str_back_quote + str_punc

"""Strip of leading space.
NOTE - there is a better way to do this."""
str_igpay_atinlay = str_igpay_atinlay.strip()
print(str_igpay_atinlay)
