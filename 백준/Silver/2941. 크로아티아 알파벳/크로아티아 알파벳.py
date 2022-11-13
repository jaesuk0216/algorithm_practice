alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']

word = input()
cn = 0

for i in alpha :
    word = word.replace(i,'*')

print(len(word))
