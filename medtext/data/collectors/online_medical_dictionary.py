import bs4
import requests
import os
import string
import time

from bs4 import BeautifulSoup


def read_terms_from_omd():
    url_format = 'https://www.online-medical-dictionary.org/glossary/{{}}.html'

    words = []
    for l in list(string.ascii_lowercase) + ['~']:
        url = url_format.replace('{{}}', l)

        result = requests.get(url)
        status_code = result.status_code
        content = result.content

        if status_code < 200 or status_code >= 300:
            # We failed, so don't return any results
            return None

        soup = BeautifulSoup(content, 'html5lib')
        word_list_tag = soup.find(id='listing')
        word_tags = word_list_tag.find_all('li')

        words.extend([w.get_text().strip() for w in word_tags])

    return words


def store_omd_terms(directory):
    filename = f'online_medical_dictionary_{time.strftime("%Y-%m-%d")}.txt'
    all_terms = read_terms_from_omd()
    with open(os.path.join(directory, filename), 'w') as webmd_file:
        for line in all_terms:
            print(line, file=webmd_file)

