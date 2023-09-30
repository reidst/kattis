from random import shuffle
def make_guess(max_len, guess):
    print(guess[:max_len], flush=True)
    return int(input())
n = int(input())
letters = ['P', 'I', 'Z', 'A']
answer = ''
newletter = 0
while (response := make_guess(n, answer + letters[newletter])) != 2:
    if response == 1:
        answer += letters[newletter]
        newletter = 0
        shuffle(letters)
    elif newletter == 2:
        answer += letters[3]
        newletter = 0
        shuffle(letters)
    else:
        newletter += 1
