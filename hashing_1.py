test = open('test_06.txt')
f = test.read()
test.close()
values = list(map(int, f.split()))
values = values[:1000]
m = len(values)


def hashfunction(k, i):
    return (k + i) % m


def HashInsert(T, k):
    i = 0
    while i != m:
        j = hashfunction(k, i)
        if T[j] is None:
            T[j] = k
            return j
        else:
            i += 1
    return 'Hash table is full!'


def HashFind(T, k):
    i = 0
    while i != m:
        j = hashfunction(k, i)
        if T[j] == k:
            return True
        else:
            i += 1
    return False


def Counter(values):
    table = [None] * m
    for k in values:
        HashInsert(table, k)
    print(table)
    l = 0
    for s in range(-1000, 1001):
        for x in table:
            if x is not None:
                y = s - x
                if x != y:
                    if HashFind(table, y):
                        print('{0} = {1} + {2}'.format(s, x, y))
                        l += 1
                        break
    return l


print(Counter(values))
