# kattis-accepted
N, M = map(int, input().split())
names = input().split()
cheaters = set()
it = set()
it.add(names[0])
for line in range(M):
    tagger, _, tagged = input().split()
    if tagger not in it:
        cheaters.add(tagger)
    else:
        it.remove(tagger)
    it.add(tagged)
print(len(cheaters))
if cheaters:
    print(*sorted(list(cheaters)))
