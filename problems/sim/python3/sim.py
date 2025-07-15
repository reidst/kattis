# kattis-unsubmitted
class DLLNode:
    def __init__(self, left, right, data):
        self.left = left
        self.right = right
        self.data = data


class DLL:
    def __init__(self):
        self.leftmost = None
        self.rightmost = None
        self.cursor = None
        self.length = 0

    def push_cursor(self, data):
        new = DLLNode(None, None, data)
        if self.length == 0:
            self.leftmost = new
            self.rightmost = new
            self.cursor = new
        else:
            new.left = self.cursor
            new.right = self.cursor.right
            self.cursor.right.left = new
            self.cursor.right = new
            self.cursor = new
        self.length += 1

    def pop_cursor(self):
        if self.length == 0:
            exit(1)
        ret = self.cursor
        if self.cursor.left is not None:
            self.cursor.left.right = self.cursor.right
        else:
            self.leftmost = self.cursor.right
        if self.cursor.right is not None:
            self.cursor.right.left = self.cursor.left
        else:
            self.rightmost = self.cursor.left
        self.length -= 1
        return ret.data


def solve(s):
    dll = DLL()
    for char in s:
        if char == '<':
            dll.pop_cursor()
        elif char == '[':
            dll.cursor = dll.leftmost
        elif char == ']':
            dll.cursor = dll.rightmost
        else:
            dll.push_cursor(char)
    step = dll.leftmost
    while step is not None:
        print(step.data, end='')
        step = step.right
    print()


def main():
    for _ in range(int(input())):
        solve(input())


if __name__ == "__main__":
    main()
