import sys
import requests
from bs4 import BeautifulSoup
import argparse

TO_CRAWL = []
CRAWLED = set()


def request(url):
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
    try:
        response = requests.get(url, headers=header)
        return response.text
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        pass


def get_links(html):
    links = []
    try:
        soup = BeautifulSoup(html, "html.parser")
        tags_a = soup.find_all("a", href=True)
        for tag in tags_a:
            link = tag["href"]
            if link.startswith("http"):
                links.append(link)

        return links
    except:
        pass


def crawl():
    while 1:
        if TO_CRAWL:
            url = TO_CRAWL.pop()

            html = request(url)
            if html:
                links = get_links(html)
                if links:
                    for link in links:
                        if link not in CRAWLED and link not in TO_CRAWL:
                            TO_CRAWL.append(link)

                print("Crawling {}".format(url))

                CRAWLED.add(url)
            else:
                CRAWLED.add(url)
        else:
            print("Done")
            break


def main():
    parser = argparse.ArgumentParser(description="Brute force directories or subdomains and crawl the website.")
    parser.add_argument("-d", "--directories", action="store_true", help="Brute force directories")
    parser.add_argument("-s", "--subdomains", action="store_true", help="Brute force subdomains")
    parser.add_argument("-c", "--crawl", action="store_true", help="Crawl the website")
    parser.add_argument("target", help="Target URL or domain")
    parser.add_argument("wordlist", nargs="?", help="Wordlist file")

    args = parser.parse_args()

    if args.crawl:
        TO_CRAWL.append(args.target)
        crawl()
    elif not args.wordlist:
        print("Please specify the wordlist.")
        parser.print_help()
        sys.exit(1)
    elif args.directories:
        brute_directories(args.target, args.wordlist)
    elif args.subdomains:
        brute_subdomains(args.target, args.wordlist)


if __name__ == '__main__':
    main(

#buscador de links
