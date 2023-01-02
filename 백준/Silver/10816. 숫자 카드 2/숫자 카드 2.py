import sys
from collections import Counter

card_num = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
test_num = int(sys.stdin.readline())
test = list(map(int,sys.stdin.readline().split()))

cnt = Counter(num)

for i in range(test_num) :
    if test[i] in cnt :
        print(cnt[test[i]],end=' ')
    else :
        print(0,end=' ')