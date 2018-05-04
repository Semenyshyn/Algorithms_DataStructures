import urllib.request

test = urllib.request.urlopen(
    "http://courses.prometheus.org.ua/c4x/KPI/Algorithms101/asset/input_1000_5.txt", ).readlines()

test2 = urllib.request.urlopen(
    "http://courses.prometheus.org.ua/c4x/KPI/Algorithms101/asset/input_1000_100.txt").readlines()


def two_user(us1, us2):
    data1 = test2[us1].decode("utf-8")
    a = data1.split()
    a.remove(a[0])
    data2 = test2[us2].decode("utf-8")
    b = data2.split()
    b.remove(b[0])
    a, b = (list(map(int, a)), list(map(int, b)))

    return a, b


def mergeSort(alist, bList):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        lhf_b = bList[:mid]
        rhf_b = bList[mid:]
        mergeSort(lefthalf, lhf_b)
        mergeSort(righthalf, rhf_b)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                bList[k] = lhf_b[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                bList[k] = rhf_b[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            bList[k] = lhf_b[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            bList[k] = rhf_b[j]
            j = j + 1
            k = k + 1
        return bList


def count_inversion(list):
    c = 0
    i = 0
    while i < len(list):
        for j in range(i, len(list)):
            if list[i] > list[j]:
                c += 1
        i += 1
    return c


'''
list = two_user(863, 29)
print(list)

p = mergeSort(list[0], list[1])
print(p)
print(count_inversion(p))
'''
list2 = two_user(951, 178)
r = mergeSort(list2[0], list2[1])
print(count_inversion(r))
