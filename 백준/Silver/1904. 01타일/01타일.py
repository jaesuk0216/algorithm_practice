n = int(input())
tile = [0] * 1000001

tile[1], tile[2] = 1,2

for i in range(3,n+1) :
    tile[i] = (tile[i-2] + tile[i-1]) % 15746
    
print(tile[n])