#!/usr/bin/python3

import requests
import sys
from urllib.parse import urljoin

def brute(url, wordlist_file):
    with open(wordlist_file, 'r') as file:
        wordlist = file.readlines()

    try:
        for word in wordlist:
            word = word.strip()
            urlfinal = urljoin(url, word)
            try:
                response = requests.get(urlfinal)
                code = response.status_code

                if code != 404:
                    print('{}: {} {}'.format(urlfinal, word, code))
            except requests.exceptions.RequestException as e:
                print("Erro ao conectar-se à URL:", e)
    except KeyboardInterrupt:
        sys.exit('User cancelled the program.')
    except:
        pass

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python3 script.py <url> <arquivo_de_lista_de_palavras>")
        sys.exit(1)

    url = sys.argv[1]
    wordlist_file = sys.argv[2]

    brute(url, wordlist_file)

