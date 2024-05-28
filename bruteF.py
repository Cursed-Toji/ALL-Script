#!/usr/bin/python3

import requests
import sys
import argparse
from urllib.parse import urljoin

def brute_directories(url, wordlist_file):
    try:
        with open(wordlist_file, 'r') as file:
            wordlist = file.readlines()

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

def brute_subdomains(domain, wordlist_file):
    try:
        with open(wordlist_file, 'r') as file:
            wordlist = file.readlines()

        for word in wordlist:
            word = word.strip()
            subdomain = '{}.{}'.format(word, domain)
            try:
                response = requests.get('http://{}'.format(subdomain))
                code = response.status_code

                if code != 404:
                    print('{}: {} {}'.format(subdomain, domain, code))
            except requests.exceptions.RequestException as e:
                print("Erro ao conectar-se à URL:", e)
    except KeyboardInterrupt:
        sys.exit('User cancelled the program.')
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description="Brute force directories or subdomains.")
    parser.add_argument("-d", "--directories", action="store_true", help="Brute force directories")
    parser.add_argument("-s", "--subdomains", action="store_true", help="Brute force subdomains")
    parser.add_argument("target", help="Target URL or domain")
    parser.add_argument("wordlist", help="Wordlist file")

    args = parser.parse_args()

    if args.directories:
        brute_directories(args.target, args.wordlist)
    elif args.subdomains:
        brute_subdomains(args.target, args.wordlist)
    else:
        print("Please specify either -d or -s option.")
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
