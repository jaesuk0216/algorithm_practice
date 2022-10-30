test_case = int(input())


for i in range(test_case) :
    cn = 0
    score_list = list(map(int,input().split()))
    avg = sum(score_list[1:]) / score_list[0] #여기까지는 문제 x 평균 잘 구함
    for j in range(1,score_list[0]+1) :
        if score_list[j] > avg :
            cn+=1


    per = "{:.3f}".format((cn / score_list[0]) * 100)
    print(str(per)+"%")

            



    

