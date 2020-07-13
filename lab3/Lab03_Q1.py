def remove_letters(text, letters):
    """ Removes given letters from given string and returns the new string

    |
    | Parameters:
    | text (str): A string to remove letters
    | letters (str): List of letters, as string, to remove from text
    |
    | Returns:
    | str: Returns the modified string
    """

    for c in letters:
        text = text.replace(c, "")

    return text


def get_code(char):
    """ Get integer representation of a character according to the table:

    | 1: b,f,p,v
    | 2: c,g,j,k,q,s,x,z
    | 3: d,t
    | 4: l
    | 5: m,n
    | 6: r
    |
    | Parameters:
    | char (str): Character to get its integer representation
    |
    | Returns:
    | int: Integer representation of char if char is in table, -1 if given
    string is not a character or not in table
    """

    # Assuming length of char is exactly one, skipping length check
    if char in "bfpv":
        return 1
    elif char in "cgjkqsxz":
        return 2
    elif char == "d" or char == "t":
        return 3
    elif char == "l":
        return 4
    elif char == "m" or char == "n":
        return 5
    elif char == "r":
        return 6
    else:
        return -1


def remove_duplicates(text):
    """ Remove all consecutive duplicates and keep the leading character

    |
    | Parameters:
    | text (str): String to modify
    |
    | Returns:
    | str: Return modified string
    """

    if text == "":
        return text

    result = text[0]

    for i in range(1, len(text)):
        if text[i] != result[-1]:
            result += text[i]

    return result


def get_soundex(word):
    """ Get soundex encoding of a word

    | Parameters:
    | word (str): A string to encode with soundex encoding
    |
    | Returns:
    | str: Returns encoded string or returns None if word contains any
    non-alphabetical characters
    """

    # only check first character since other characters will implicitly be
    # checked when get_code returns -1
    if not word[0].isalpha():
        return None

    # keep the first letter and then lower the word
    soundex = word[0]
    word = word[1:].lower()

    # remove vowels
    word = remove_letters(word, "aeiouhwy")

    # remove consecutive characters
    word = remove_duplicates(word)

    # encode other characters
    for i in range(len(word)):
        code = get_code(word[i])
        if code == -1:
            return None
        soundex += str(code)

    # via str.ljust
    return soundex.ljust(4, "0")

    # via string format
    # return "{:<04}".format(soundex)

    # via str.zfill
    # return soundex[::-1].zfill(4)[::-1]


soundex = get_soundex(input("Enter a word: "))
if soundex is not None:
    print(soundex)
else:
    print("Word contains invalid characters")
