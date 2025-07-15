# kattis-accepted
p = int(input())
planet_map = {}
planets = set()
for _ in range(p):
    planet_name, _, *species_names = input().split()
    planets.add(planet_name)
    for s in species_names:
        planet_map[s] = planet_name
v = int(input())
counter = {p: 0 for p in planets}
for _ in range(v):
    count, species = input().split()
    count = int(count)
    planet = planet_map[species]
    counter[planet] += count
for planet, count in sorted(counter.items()):
    print(planet, count)
