# kattis-accepted
R = int(input())
lo, hi = 0, R+1
day = 0
response = ""
while response != "exact":
    day += 1
    mid = (lo + hi) // 2
    print(mid * day, flush=True)
    response = input()
    if response == "less":
        hi = mid
    elif response == "more":
        lo = mid
