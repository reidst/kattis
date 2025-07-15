# kattis-accepted
ops = ('+', '-', '*', '//')
a, b, c = map(int, input().split())

results = []

for opa in ops:
    if opa == '//' and a % b != 0:
        continue
    for opb in ops:
        if opb == '//' and eval(f"({a} {opa} {b})") % c != 0:
            continue
        result = eval(f"({a} {opa} {b}) {opb} {c}")
        if result >= 0:
            results.append(result)

print(min(results))
