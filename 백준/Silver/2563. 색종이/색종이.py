n = int(input())
area = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n) :
    x,y = map(int,input().split())
    for i in range(x,x+10) :
        for j in range(y,y+10) :
            area[i][j] = 1

ans = 0
for row in area :
    ans += row.count(1)

print(ans)