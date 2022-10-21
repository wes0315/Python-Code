# Given an array of integers, where all elements but one occur twice, find the unique element.
a = [1, 2, 3, 4, 3, 2, 1]


def lonelyinteger(a):
    sorted_a = sorted(set(a))
    for integer in sorted_a:
        if a.count(integer) == 1:
            return integer


print(lonelyinteger(a))
