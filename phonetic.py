import requests
from bs4 import BeautifulSoup


def textToPhoneticSymbol(text):
    req = requests.get("https://eow.alc.co.jp/search?q=" + text)
    req_soup = BeautifulSoup(req.content, "html.parser")
    pron = req_soup.find('span', class_='pron').text[:-1]
    print(pron)


# test
if __name__ == '__main__':
    textToPhoneticSymbol("something")
