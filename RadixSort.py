import urllib.request
from itertools import product
from string import ascii_lowercase

a = urllib.request.urlopen("http://courses.prometheus.org.ua/c4x/KPI/Algorithms101/asset/anagrams.txt").read()
a = a.decode("utf-8")
b = a.split()


def counting_sort(l, d):
    letters = [chr(i) for i in range(97, 122)]
    keywords = [''.join(i) for i in product(ascii_lowercase, repeat=3)]
    items = dict()
    for letter in letters:
        items[letter] = 0
    for item in l:
        d_item = item[2:]
        items[d_item] += 1
    sort_l = list()
    for letter in letters:
        sort_l.extend(letter * items[letter])
    return sort_l


def radix_string_sort(l, i):
    if len(l) <= 1:
        return l
    done_bucket = []
    buckets = [[] for x in range(27)]
    for s in l:
        if i >= len(s):
            done_bucket.append(s)
        else:
            buckets[ord(s[i]) - ord('a')].append(s)
    buckets = [radix_string_sort(b, i + 1) for b in buckets]
    return done_bucket + [b for blist in buckets for b in blist]

o = ['abc', 'dcb', 'abb']
print(radix_string_sort(o, 1))



