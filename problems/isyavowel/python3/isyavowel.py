# kattis-accepted
w, wo = 0, 0
for char in input():
    if char in "aeiouy":
        w += 1
        if char != "y":
            wo += 1
print(wo, w)
