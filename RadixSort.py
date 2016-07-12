import urllib.request
from collections import Counter


a = urllib.request.urlopen("http://courses.prometheus.org.ua/c4x/KPI/Algorithms101/asset/anagrams.txt").read()
a = a.decode("utf-8")
b = a.split()
n = Counter(a)


def counting_sort(l, d):
    letters = [chr(i) for i in range(97, 123)]
    sort_l = list()
    for letter in letters:
        for keyword in l:
            if letter == keyword[d]:
                sort_l.append(keyword)
    return sort_l


def radix_sort(l, d):
    for i in range(d+1):
        l = counting_sort(l, d-i)
    return l

w = radix_sort(b, 2)
print(w)

