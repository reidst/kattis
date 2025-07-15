# kattis-wa
n = int(input())
G = {}
for _ in range(n - 1):
    i, j = map(int, input().split())
    if i in G:
        G[i].append(j)
    else:
        G[i] = [j]
a_freq = [0] * n
b_freq = [0] * n
freq_counter = 0
def new_freq():
    global freq_counter
    freq_counter += 1
    return freq_counter
def dfs(node, parent_freq, parent):
    a_freq[node - 1] = parent_freq
    this_freq = new_freq()
    b_freq[node - 1] = this_freq
    if node in G:
        lending_freqs = [this_freq, parent_freq]
        lfi = 0
        for child in G[node]:
            dfs(child, lending_freqs[lfi], node)
            lfi = 1 - lfi
    else:
        b_freq[node - 1] = a_freq[parent - 1]
dfs(1, new_freq(), 1)
for i in range(n):
    print(a_freq[i], b_freq[i])
