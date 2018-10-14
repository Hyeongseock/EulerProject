'''
#-------------problem-------------
n! 이라는 표기법은 n × (n − 1) × ... × 3 × 2 × 1을 뜻합니다.
예를 들자면 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800 이 되는데,
여기서 10!의 각 자리수를 더해 보면 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27 입니다.
100! 의 자리수를 모두 더하면 얼마입니까?

#-------------solution-------------
1. 100!의 값을 구한다. 즉 반복문으로 1~100까지를 곱한다.
2. 100!의 값을 str타입으로 변환한다. 
3. str으로 변환된 100!의 값을 100!의 첫 번째부터 마지막 자리까지 반복문을 활용하여 더해준다. 
'''

#-------------code-------------
number = 1 #100!이 될 변수로 초기값을 1로 셋팅한다.
answer = 0 #정답이 될 변수로 초기값은 0으로 셋팅한다.
for i in range(1,101) :
    number *= i

number = str(number)
for i in range(0, len(number)) : 
    temp = int(number[i])
    answer += temp
print(answer)

#-------------spending times-------------
# 0.0 seconds