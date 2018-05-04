from math import ceil

x = 1685287499328328297814655639278583667919355849391453456921116729

y = 7114192848577754587969744626558571536728983167954552999895348492
a = 1234
b = 5678


def prepend_zeros(ls, n):
    while len(ls) != n:
        ls = '0' + ls
    return ls


k = 0


def karatsuba(x, y):
    str_x, str_y = str(x), str(y)
    n = max(len(str_x), len(str_y))
    if n <= 1:
        return x * y
    str_x = prepend_zeros(str_x, n)
    str_y = prepend_zeros(str_y, n)
    n_2 = int(n / 2)

    a, b = int(str_x[:n_2] or 0), int(str_x[n_2:] or 0)
    c, d = int(str_y[:n_2] or 0), int(str_y[n_2:] or 0)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a + b), (c + d)) - ac - bd
    if ad_bc == 12:
        print('h')
    # for supporting edge case where n is not a multiple of 2
    n_2 = int(ceil(n / 2.0))
    n = n if n % 2 == 0 else n + 1
    return (10 ** n * ac) + (10 ** n_2 * ad_bc) + bd


print(karatsuba(x, y))
print(x * y)
