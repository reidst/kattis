# kattis-unsolved
# TODO time limit exceeded (even though it's 11 seconds)
from dataclasses import dataclass
from collections import deque


@dataclass
class Trie:
    children: dict[str, 'Trie']
    mark: bool

    def add(self, word: str):
        follow = self
        for letter in word:
            if letter not in follow.children:
                follow.children[letter] = Trie(children={}, mark=False)
            follow = follow.children[letter]
        follow.mark = True

    def subtrie(self, word: str):
        follow = self
        for letter in word:
            if letter in follow.children:
                follow = follow.children[letter]
            else:
                return None
        return follow

    def contains(self, word: str) -> bool:
        return self.subtrie(word) is not None

    def contains_marked(self, word: str) -> bool:
        sub = self.subtrie(word)
        if sub is not None:
            return sub.mark
        else:
            return False


def score_word(word):
    size = len(word)
    if 3 <= size <= 4:
        return 1
    elif size == 5:
        return 2
    elif size == 6:
        return 3
    elif size == 7:
        return 5
    elif size == 8:
        return 11
    else:
        return 0


def next_heads(pathlist, pathset):
    head = pathlist[-1]
    for delta in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
        newr = head[0] + delta[0]
        newc = head[1] + delta[1]
        newpos = (newr, newc)
        if newpos not in pathset and 0 <= newr < 4 and 0 <= newc < 4:
            yield newpos


def solve_board(words):
    board = []
    for _ in range(4):
        board.append(input())
    queue = deque()
    for r in range(4):
        for c in range(4):
            letter = board[r][c]
            if letter in words.children:
                queue.append(([(r,c)], {(r,c)}, board[r][c], words.children[letter]))
    max_score = 0
    longest_word_len = 0
    longest_word = ""
    found_words = set()
    while len(queue) > 0:
        ulist, uset, word, utrie = queue.popleft()
        for newr, newc in next_heads(ulist, uset):
            newchar = board[newr][newc]
            subtrie = utrie.children.get(newchar)
            if subtrie is not None:
                newword = word + newchar
                queue.append(([*ulist, (newr, newc)], {*uset, (newr, newc)}, newword, subtrie))
                if subtrie.mark and newword not in found_words:
                    found_words.add(newword)
                    newword_len = len(uset) + 1
                    if newword_len > longest_word_len or newword_len == longest_word_len and newword < longest_word:
                        longest_word = newword
                        longest_word_len = newword_len
                    max_score += score_word(newword)
    print(max_score, longest_word, len(found_words))


def main():
    words = Trie(children={}, mark=False)
    for _ in range(int(input())):
        words.add(input())
    input()
    problems = int(input())
    solve_board(words)
    for i in range(problems - 1):
        input()
        solve_board(words)


if __name__ == "__main__":
    main()
