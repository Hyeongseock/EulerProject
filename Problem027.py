'''
#-------------problem-------------
오일러는 다음과 같은 멋진 2차식을 제시했습니다.
n2 + n + 41
이 식의 n에다 0부터 39 사이의 숫자를 넣으면, 그 결과는 모두 소수가 됩니다.
하지만 n = 40일 때의 값 402 + 40 + 41 은 40×(40 + 1) + 41 이므로 41로 나누어지고, n = 41일 때 역시 412 + 41 + 41 이므로 소수가 아닙니다.
컴퓨터의 발전에 힘입어 n2 − 79n + 1601 이라는 엄청난 2차식이 발견되었는데, 이것은 n이 0에서 79 사이일 때 모두 80개의 소수를 만들어냅니다. 
이 식의 계수의 곱은 -79 × 1601 = -126479가 됩니다. 
아래와 같은 모양의 2차식이 있다고 가정했을 때,
n2 + an + b   (단 | a | < 1000, | b | < 1000)
0부터 시작하는 연속된 n에 대해 가장 많은 소수를 만들어내는 2차식을 찾아서, 그 계수 a와 b의 곱을 구하세요.
#-------------solution-------------
1. a와 b를 넣어 만들 수 있는 가장 큰 숫자를 구한다.
2. a와 b를 넣어 만들 수 있는 가장 큰 숫자보다 작은 소수로 이루어진 리스트를 구한다.
3. a(-999~999)와 b(-999~999) 그리고 n( 0 <= n < a)의 범위에서 가장 많은 연속된 소수를 만들어내는 a와 b의 곱을 구한다.
#-------------code-------------
#1.솔루션 1번 최대값 구하기
max_value = 998^2 + 998*999 + 999

#2.솔루션 2번 max_value보다 작은 소수 리스트 구하기
prime_list = [2,3,5,7,11,13]
i = 14
max_prime = prime[-1]
while max_prime < max_value :
    remainder_list = []
    for prime in prime_list :
        remainder = i % prime
        remainder_list.append(remainder)
        
    if min(remainder_list) != 0:
        prime_list.append(i)
        max_prime = i
    i += 1
    
#3. 솔루션 3번 각 범위에서 구할 수 있는 가장 많은 소수를 만들어내는 a와 b의 곱
answer = 0
save_a_b = 0
for a in range(-999,1000) :
    for b in range(-999,1000) :
        n = 0
        value = 2
        while value in prime_list :
            value = n ** 2 + a * n + b
            #print(value)
            if value in prime_list :
                n += 1
        if n > answer :
            answer = n
            save_a_b = (a, b , a*b, n)

    print(save_a_b)

#번외 아래도 사용가능하다고 함
def intersection(a,b) :
    return list(set(a)&set(b))

#-------------spending time-------------
# 969..seconds ---
