import random

l = []

for i in range(25):
    l.append(random.randint(1, 10))

print("List =", l)

s = 0
for i in l:
    s += i

mean = s / len(l)

l.sort()

median = l[len(l) // 2]

mode = l[0]
max_count = 0

for i in l:
    c = 0
    for j in l:
        if i == j:
            c += 1
    if c > max_count:
        max_count = c
        mode = i

print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)