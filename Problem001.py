'''
Multiples of 3 and 5
Problem 1
'''

'''
English version
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

#Setting 
three_list = []
five_list = []
i = 1

#Make multiples list of 3 
while 3*i < 1000 :
    a = 3*i
    three_list.append(a)
    i += 1
    i = 1

#Make multiples list of 3
while 5 * i < 1000 :
    a = 5 * i
    five_list.append(a)
    i += 1

#Add two lists
all_list = three_list + five_list

#Deduplication
all_list = set(all_list)

#Sum all elements in list
sum = 0
for i in all_list:
    sum = sum + i

#answer
print(sum)

#time spent : 0.0009975433349609375 seconds





'''
Korean version
10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고, 이것을 모두 더하면 23입니다.
1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?
'''

#초기값 셋팅
three_list = []
five_list = []
i = 1

#3의 배수 리스트 만들기 
while 3*i < 1000 :
    a = 3*i
    three_list.append(a)
    i += 1
    i = 1

#5의 배수 리스트 만들기
while 5 * i < 1000 :
    a = 5 * i
    five_list.append(a)
    i += 1

#두 리스트 합치기
all_list = three_list + five_list

#중복숫자 제거하기
all_list = set(all_list)

#모든 숫자 합치기
sum = 0
for i in all_list:
    sum = sum + i

#정답
print(sum)

#계산에 걸린 시간 : 0.0009975433349609375 seconds
