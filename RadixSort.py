import urllib.request
a = urllib.request.urlopen("http://courses.prometheus.org.ua/c4x/KPI/Algorithms101/asset/anagrams.txt").read()
a = a.decode("utf-8")
b = a.split()


def counting_sort(l, d):
    letters = [chr(i) for i in range(97, 122)]
    items = dict()
    for letter in letters:
        items[letter] = 0
    for item in l:

        items[item] += 1
    sort_l = list()
    for letter in letters:
        sort_l.extend(letter * items[letter])
    return sort_l

#def redix_sort(l, d):
#    for i in d:



