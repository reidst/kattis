# kattis-partial
def main():
    n = int(input())
    a = list(map(int, input().split()))
    maxi = 0
    st = []
    for i in range(n):
        ca = a[i]
        while st and st[-1][0] <= ca:
            st.pop()
        if st:
            pi = st[-1][1]
            maxi = max(maxi, i - pi)
        st.append((ca, i))
    st = []
    for i in range(n-1, -1, -1):
        ca = a[i]
        while st and st[-1][0] <= ca:
            st.pop()
        if st:
            pi = st[-1][1]
            maxi = max(maxi, pi - i)
        st.append((ca, i))
    print(maxi)


if __name__ == "__main__":
    main()
