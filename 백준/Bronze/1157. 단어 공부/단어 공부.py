word = input().lower()
word_list = list(set(word))
cn = []

for i in word_list :
    count = word.count(i)
    cn.append(count)

if cn.count(max(cn)) >= 2 :
    print("?")

else :
    print(word_list[(cn.index(max(cn)))].upper())