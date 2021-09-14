import re
import pieltk.phonology.xcl.xcl as phon
from pieltk.alphabet import xcl

from itertools import accumulate


def syllabify(string: str) -> list[str]:
    clean_string = string

    #  Remove punctuations
    for punct in xcl.PUNCTUATION:
        clean_string = clean_string.replace(punct, "")

    #  Remove multiple spaces if there are any
    clean_string = re.sub(r"\ +", " ", clean_string)
    words = clean_string.split(" ")

    #  Initialize the output
    split_words = []

    for word in words:
        #  Split the word keeping diphthongs as a single entry in the list
        letters = split_str(word)
        syllables: list[str] = []

        #  Generates a list of the possible syllables in a given word using
        #  the letters in reversed order [::-1], joining them one by one in the
        #  right order (lambda function).
        acc = list(accumulate(letters[::-1], func=lambda x, y: str(y)+str(x)))

        #  Loops until all the possible syllables are selected. When a syllable
        #  is selected, itself and its components are removed from the accumulated
        #  list and its effects on other syllables are cleaned with str.replace().
        #
        #  The syllable is selected by its score produced by the rules hard coded
        #  in syllab_score. It is possible to generalize the function with a
        #  dictionary, but it works for the moment.

        while acc:
            scores = dict(zip(acc, list(map(syllab_score, acc))))
            best_scorer = max(scores, key=scores.get)  # type: ignore
            syllables.insert(0, best_scorer)
            acc = acc[acc.index(best_scorer)+1:]
            for i in range(len(acc)):
                acc[i] = acc[i].replace(best_scorer, "")

        split_words.append(".".join(syllables))

    return(split_words)


def syllab_score(syllab: str) -> int:
    score = 0
    syllab_split = split_str(syllab)
    if len(syllab_split) <= 4:
        mapped = "".join(list(map(char_type, syllab_split)))
        if mapped in ["CRVR"]:
            score = 7
        elif mapped in ["CVR", "RVC", "RVR", "CVC"]:
            score = 6
        elif mapped in ["CRV"]:
            score = 5
        elif mapped in ["CV", "RV", "CR"]:
            score = 4
        elif mapped in ["VR", "VC"]:
            score = 3
        elif mapped in ["V"]:
            score = 2
        elif mapped == "C":
            score = 1
        else:
            pass
    else:
        # Impossible syllable
        pass

    return score


def split_str(string: str) -> list[str]:
    letters = []
    poss_diph = ""
    for letter in string:
        if letter in phon.CONSONANTS:
            if poss_diph:
                letters.append(poss_diph)
            poss_diph = ""
            letters.append(letter)
        elif letter in phon.MONOPHTONGS:
            poss_diph += letter

    return(letters)


def char_type(char: str) -> str:
    if char in phon.VOWELS:
        return("V")
    elif char in phon.RESONANTS:
        return("R")
    else:
        return("C")


if __name__ == '__main__':
    string = "Զինչ օգտիցի մարդ՝ եթէ զաշխարհս ամենայն շահեսցի եւ զանձն իւր տուժեսցի կամ զինչ տացէ      մարդ փրկանս ընդ անձին իւրում"
    teste = syllabify(string)
    for x in teste:
        print(x)
