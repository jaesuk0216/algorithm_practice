x,y,w,h = map(int,input().split())
num_list = [x,y,(w-x),(h-y)]
print(min(num_list))
