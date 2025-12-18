import copy

l = [10, 2, 3, 5, 6, 7]
first, *middle, last = l
t = (first + last, sum(middle))
print(t)
l.pop()
l.append("gg")
l.extend((1, 2))
print(l)
l2 = l.copy()
copy.deepcopy(l)
