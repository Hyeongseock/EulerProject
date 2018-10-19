'''
#-------------problem-------------
n의 약수들 중에서 자신을 제외한 것의 합을 d(n)으로 정의했을 때,
서로 다른 두 정수 a, b에 대하여 d(a) = b 이고 d(b) = a 이면
a, b는 친화쌍이라 하고 a와 b를 각각 친화수(우애수)라고 합니다.
예를 들어 220의 약수는 자신을 제외하면 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 이므로 그 합은 d(220) = 284 입니다.
또 284의 약수는 자신을 제외하면 1, 2, 4, 71, 142 이므로 d(284) = 220 입니다.
따라서 220과 284는 친화쌍이 됩니다.
10000 이하의 친화수들을 모두 찾아서 그 합을 구하세요.

#-------------solution-------------
1. 1만 이하의 모든 수의 약수를 구한다.
2. dic형태로 만든다  > 자신(key) : [자신을 제외한 약수](value)
3. key값과 value의 합이 같은 숫자를 찾고 리스트에 넣는다
4. 합친다.

#-------------code-------------
# 1번 solution 진행
num_dic = {}
sum_number = 1
while sum_number < 10001 :
    y_list = []
    if sum_number % 2 == 0:
        a = int(sum_number / 2) + 1
        for j in range(1, a):
            if sum_number % j == 0:
                y_list.append(j)
    if sum_number % 2 != 0:
        a = int(sum_number + 1 / 2)
        for j in range(1, a):
            if sum_number % j == 0:
                y_list.append(j)
    num_dic[sum_number] = sum(y_list) # 2번 solution 진행
    sum_number += 1
    
    
    answer_list = []
#3번 솔루션 
for i in num_dic :
    value = num_dic[i]
    if value == 0 :
        pass
    elif value > sum_number -1 :
        pass
    else :
        check_value = num_dic[value]
        if i == check_value :
            if i != value :
                answer_list.append(i)
                answer_list.append(value)
print(answer_list)
print(sum(answer_list)/2) #4번 솔루션


#-------------spending time-------------
# 3.3271901607513428 seconds 
