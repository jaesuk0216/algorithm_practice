kg = int(input())
cnt = 0

while kg >= 0 :
    if kg %5 ==0 :
        cnt +=(kg//5)
        print(cnt)
        break
    kg -=3
    cnt +=1
else :
    print(-1)
