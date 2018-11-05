'''
#-------------problem-------------
어떤 대상을 순서에 따라 배열한 것을 순열이라고 합니다. 예를 들어 3124는 숫자 1, 2, 3, 4로 만들 수 있는 순열 중 하나입니다.
이렇게 만들 수 있는 모든 순열을 숫자나 문자 순으로 늘어놓은 것을 사전식(lexicographic) 순서라고 합니다.
0, 1, 2로 만들 수 있는 사전식 순열은 다음과 같습니다.
012   021   102   120   201   210
0, 1, 2, 3, 4, 5, 6, 7, 8, 9로 만들 수 있는 사전식 순열에서 1,000,000번째는 무엇입니까?
#-------------solution-------------
1. 0-9로 이루어진 셋을 만든다.
2. 0123456789, 0123456798 처럼 오름차순으로 숫자를 만들고 리스트에 담는다.
3. 1,000,000번째 숫자를 구한다.
#-------------code-------------
#솔루션 1번 0-9로 이루어진 셋을 만든다.
number_set = set([0,1,2,3,4,5,6,7,8,9])
answer_list = []
#솔루션 2번 0123456789, 0123456798 처럼 오름차순으로 숫자를 만들고 리스트에 담는다. --> 더쉽게 코딩하는 방법이 있을 것 같은데..
for i in number_set :
    temp1 = [i]
    for j in number_set-set(temp1):
        temp2 = [j]
        for k in number_set-set(temp1)-set(temp2) :
            temp3 = [k]
            for l in number_set-set(temp1)-set(temp2)-set(temp3) :
                temp4 = [l]
                for m in number_set - set(temp1) - set(temp2) - set(temp3) - set(temp4):
                    temp5 = [m]
                    for n in number_set - set(temp1) - set(temp2) - set(temp3) - set(temp4) - set(temp5):
                        temp6 = [n]
                        for o in number_set - set(temp1) - set(temp2) - set(temp3) - set(temp4) - set(temp5) - set(temp6):
                            temp7 = [o]
                            for p in number_set - set(temp1) - set(temp2) - set(temp3) - set(temp4) - set(temp5) - set(temp6) - set(temp7):
                                temp8 = [p]
                                for q in number_set - set(temp1) - set(temp2) - set(temp3) - set(temp4) - set(temp5) - set(temp6) - set(temp7) - set(temp8):
                                    temp9 = [q]
                                    for r in number_set - set(temp1) - set(temp2) - set(temp3) - set(temp4) - set(temp5) - set(temp6) - set(temp7) - set(temp8) - set(temp9):
                                        answer_list.append(str(i) + str(j) + str(k) + str(l) + str(m) + str(n) + str(o) + str(p) + str(q) + str(r))
answer_list.sort()

#솔루션 3번 1,000,000번째 숫자를 구한다.
print(answer_list[999998:1000002])

#-------------spending time-------------
# 32.4438 seconds ---
