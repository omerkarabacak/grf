import sys
from googlesearch import search, get_random_user_agent

if len(sys.argv) != 8:
    print("Usage : pythnon3 {} <search_keyword> <country> <tld> <lang> <num> <stop> <pause>".format(
        sys.argv[0]))
    print("Example : pythnon3 {} \"web hosting\" Turkey com.tr tr 50 99 3".format(
        sys.argv[0]))
    exit()

if __name__ == "__main__":
    search_keywords = sys.argv[1]
    country = sys.argv[2]
    tld = sys.argv[3]
    lang = sys.argv[4]
    num = int(sys.argv[5])
    stop = int(sys.argv[6])
    pause = int(sys.argv[7])

    rank = 1
    search_result = search(search_keywords, tld=tld, num=num, stop=stop,
                           pause=pause, country=country, lang=lang, user_agent=get_random_user_agent())
    for url in search_result:
        print("SIRA: {} - SITE: {}".format(rank, url))
        rank += 1
