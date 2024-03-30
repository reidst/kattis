words = list(filter(lambda w: "e" in w, input().split()))
if words:
    print(*words, sep=' ')
else:
    print('oh noes')
