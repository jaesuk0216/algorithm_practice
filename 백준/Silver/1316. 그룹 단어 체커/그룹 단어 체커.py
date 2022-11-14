num = int(input())
cn = num



for i in range(num) :
    word = input()
    for j in range(0,len(word)-1) :
        if word[j] == word[j+1] :
            pass
        elif word[j] in word[j+1:] :
            cn -=1
            break

print(cn)