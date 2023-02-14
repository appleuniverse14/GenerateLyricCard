import requests
from bs4 import BeautifulSoup
import time


# Get phonetic symbol of the word given as an argument
def wordToPhoneticSymbol(word):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
    req = requests.get(
        "https://dictionary.cambridge.org/us/dictionary/english/" + word, headers=headers)
    req_soup = BeautifulSoup(req.content, "html.parser")
    try:
        pron = req_soup.find(
            'span', attrs={'class': ['ipa', 'dipa', 'lpr-2', 'lpl-1']}).text
        return pron
    except AttributeError:
        print('Failed to get phonetic symbol')
        return ''


def parseText(filename):  # Parse the text file(separete to words and '\n')
    words = []
    f = open(filename, 'r')
    texts = f.readlines()
    for text in texts:
        for word in text.split(' '):
            if word[-1] == '\n':
                words.append(word[:-1])
                words.append('\n')
            else:
                words.append(word)
    f.close()
    return words


def generatePhoneticDict(filename):  # Generate dict of word and phonetic symbol
    words = parseText(filename)
    word_phonetic = []
    for word in words:
        print(word)
        if word == '\n':
            word_phonetic.append(('\n', '\n'))
        elif word == '':
            pass
        elif '-' in word:
            words_hyphen = word.split('-')
            for i, word_hyphen in enumerate(words_hyphen):
                if i < len(words_hyphen) - 1:
                    word_hyphen += '-'
                phonetic = wordToPhoneticSymbol(word_hyphen)
                word_phonetic.append((word_hyphen, phonetic))
                time.sleep(0.5)
        else:
            if "'s" in word:
                phonetic = wordToPhoneticSymbol(word[0:word.find("'")])
                word_phonetic.append((word, phonetic))
            else:
                phonetic = wordToPhoneticSymbol(word)
                word_phonetic.append((word, phonetic))
            time.sleep(0.1)
    return word_phonetic
