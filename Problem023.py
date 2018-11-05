'''
#-------------problem-------------
자신을 제외한 약수(진약수)를 모두 더하면 자기 자신이 되는 수를 완전수라고 합니다.
예를 들어 28은 1 + 2 + 4 + 7 + 14 = 28 이므로 완전수입니다.
또, 진약수의 합이 자신보다 작으면 부족수, 자신보다 클 때는 초과수라고 합니다.

12는 1 + 2 + 3 + 4 + 6 = 16 > 12 로서 초과수 중에서는 가장 작습니다.
따라서 초과수 두 개의 합으로 나타낼 수 있는 수 중 가장 작은 수는 24 (= 12 + 12) 입니다.

해석학적인 방법을 사용하면, 28123을 넘는 모든 정수는 두 초과수의 합으로 표현 가능함을 보일 수가 있습니다.
두 초과수의 합으로 나타낼 수 없는 가장 큰 수는 실제로는 이 한계값보다 작지만, 해석학적인 방법으로는 더 이상 이 한계값을 낮출 수 없다고 합니다.

그렇다면, 초과수 두 개의 합으로 나타낼 수 없는 모든 양의 정수의 합은 얼마입니까?
#-------------solution-------------
1. 1부터 28123까지의 숫자중에서 약수인 숫자를 구한다.
2. 약수 중에서 초과수인 약수만 추출한다.
3. 초과수 두개의 합으로 표현가능한 숫자를 구한다.
4. 1부터 28123까지의 숫자중 초과수 두개의 합으로 구할 수 없는 숫자만 골라서 합한다.
#-------------code-------------
# #솔루션 1번 진행 약수 구하기 from 1 to 28122
abundant_number_list = []
number = 1
while number < 28123:
    number_list = []
    if number % 2 == 0:
        a = int(number / 2) + 1
        for j in range(1, a):
            if number % j == 0:
                number_list.append(j)
    if number % 2 != 0:
        a = int(number + 1 / 2)
        for j in range(1, a):
            if number % j == 0:
                number_list.append(j)
                
    #check abundant_number(솔루션 2번 진행 초과수 구하기)
    if sum(number_list) > number :
        abundant_number_list.append(number)
    number += 1
abundant_number_sum_list = []

#(솔루션 3번 진행 초과수로 표현가능한 숫자 구하기)
for i in abundant_number_list :
    for j in abundant_number_list :
        abundant_number_sum_list.append(i+j)

#(솔루션 4번 진행 1부터 28123 중 초과수로 표현불가능한 숫자 구하고 더하기)
number_list = []
for i in range(1,28123) :
    number_list.append(i)
number_list = list(set(number_list) - set(abundant_number_sum_list))
print(sum(number_list))


#-------------spending time-------------
# 28.37362289428711 seconds ---
