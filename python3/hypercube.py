D, a, b = input().split()
D = int(D)

def get_gray_index(s):
    count = ''
    switch = False
    for bit in s:
        if bit == '1':
            if switch:
                count += '0'
            else:
                count += '1'
            switch = not switch
        else:
            if switch:
                count += '1'
            else:
                count += '0'
    return int(count, 2)

agray = get_gray_index(a)
bgray = get_gray_index(b)
print(bgray - agray - 1)