import urllib.request
from itertools import product
from collections import Counter
from string import ascii_lowercase

a = urllib.request.urlopen("http://courses.prometheus.org.ua/c4x/KPI/Algorithms101/asset/anagrams.txt").read()
a = a.decode("utf-8")
b = a.split()
n = Counter(a)


def counting_sort(l, d):
    letters = [chr(i) for i in range(97, 123)]
    keywords = [''.join(i) for i in product(ascii_lowercase, repeat=3)]
    items = dict()
    for keyword in keywords:
        items[keyword] = 0
    for item in l:
        items[item] += 1
    sort_l = list()
    for letter in letters:
        for keyword in l:
            if letter == keyword[d]:
                sort_l.append(keyword)
                items[keyword] -= 1
    return sort_l


def radix_sort(l, d):
    for i in range(d+1):
        l = counting_sort(l, d-i)
    return l


w = radix_sort(b, 2)
print(w)
print(sorted(b))
