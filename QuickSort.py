import urllib.request
import statistics

a = urllib.request.urlopen("http://courses.prometheus.org.ua/c4x/KPI/Algorithms101/asset/input__10000.txt").read()
a = a.decode("utf-8")
b = a.split()
c = list(map(int, b))
c.remove(c[0])

k = []


def quick_sort(mlist, p, r):
    if p < r:
        u = statistics.median_low([mlist[p], mlist[r], mlist[int((p + r) / 2)]])
        y = mlist.index(u)
        mlist[y], mlist[r] = mlist[r], mlist[y]
        q = partition(mlist, p, r)
        quick_sort(mlist, p, q - 1)
        quick_sort(mlist, q + 1, r)
    return mlist


def partition(mlist, p, r):
    k.append(r - p)
    x = mlist[r]
    i = p - 1
    for j in range(p, r):
        if mlist[j] <= x:
            i += 1
            mlist[i], mlist[j] = mlist[j], mlist[i]
    mlist[i + 1], mlist[r] = mlist[r], mlist[i + 1]
    return i + 1


print(quick_sort(c, 0, len(c) - 1))
print(k)
print(sum(k))
