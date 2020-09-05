from bs4 import BeautifulSoup
import requests
import os

BASE_DIR = os.getcwd() + '/populateDBCode/v003/wb1913_{}.html'


def applyBeautifulSoup():
    list_of_files = []
    lisf_of_chars = [chr(x) for x in range(ord('a'), ord('b') + 1)]

    for char in lisf_of_chars:
        file_name = BASE_DIR.format(char)
        list_of_files.append(file_name)
    print(list_of_files)

    list_of_soup = []
    for file in list_of_files:
        f = open(file, 'r', encoding='latin1')
        s = f.read()
        soup = BeautifulSoup(s, features="html.parser")
        list_of_soup.append(soup)

    list_of_words = []
    for soup in list_of_soup[:1]:
        for para in soup.find_all('p'):
            word = ''.join(e for e in para.find_all('b')[0].text if e.isalnum() or e == ' ').capitalize()
            partsOfSpeech = para.find_all('i')[0].text
            meaning = para.text

            if len(word) != 1:
                if partsOfSpeech:
                    list_of_words.append((word, partsOfSpeech, meaning))
                else:
                    list_of_words.append((word, "", meaning))

    # print(list_of_words[:10])
    return list_of_words[:10]
