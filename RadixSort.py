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
    for keyword in keywords:
        items[keyword] = 0
    for item in l:
        items[item] += 1
    sort_l = list()
    for letter in letters:
        for keyword in l:
            if letter == keyword[d]:
                sort_l.extend(keyword * items[keyword])
    sorted_list = [i+j+z for i, j, z in zip(sort_l[::3], sort_l[1::3], sort_l[2::3])]
    return sorted_list


o = ['abc', 'dcb', 'abb']
p = counting_sort(b, 2)
print(counting_sort(p, 1))


