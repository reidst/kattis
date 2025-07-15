# kattis-accepted
import math
n = int(input())
print(n if n < 4 else int(math.log(n - 1, 2)) + 2)

# 1 -> 1; s
# 2 -> 2; s,s
# 3 -> 3; s,s,s
# 4 -> 3; p,ss,ss
# 5 -> 4; p,ss,ss,s_
# 6 -> 4; p,ss,ss,ss
# 7 -> 4; p,pp,ssss,sss_
# 8 -> 4; p,pp,ssss,ssss
# 9 -> 5; p,pp,pppp,ssssssss,s_______
# ...
# 16 -> 5; p,pp,pppp,ssssssss,ssssssss
# 17 -> 6;
