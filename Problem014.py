'''
Longest Collatz sequence
Problem 14
'''

'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
value = 100000 #I just guessed the answer is more than 100000 
answer = []
number_list = []
while value < 1000000 :
    number_list = []
    number = value
    number_list.append(number)
    while number > 2 :
        if number%2 == 0 :
            number = number/2
            number_list.append(number)
        else :
            number = 3*number + 1
            number_list.append(number)
    if len(number_list) > len(answer) :
        answer = number_list               
    value += 1
    print(answer[0])
    
#time spent : 32.96388530731201 seconds
 
 
 
'''
Korean version
양의 정수 n에 대하여, 다음과 같은 계산 과정을 반복하기로 합니다.

n → n / 2 (n이 짝수일 때)
n → 3 n + 1 (n이 홀수일 때)

13에 대하여 위의 규칙을 적용해보면 아래처럼 10번의 과정을 통해 1이 됩니다.

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
아직 증명은 되지 않았지만, 이런 과정을 거치면 어떤 수로 시작해도 마지막에는 1로 끝나리라 생각됩니다. 
(역주: 이것은 콜라츠 추측 Collatz Conjecture이라고 하며, 이런 수들을 우박수 hailstone sequence라 부르기도 합니다)

그러면, 백만(1,000,000) 이하의 수로 시작했을 때 1까지 도달하는데 가장 긴 과정을 거치는 숫자는 얼마입니까?

참고: 계산 과정 도중에는 숫자가 백만을 넘어가도 괜찮습니다.
'''

value = 100000 # 정답이 10만은 넘을 것으로 예상하여 시작값을 10만으로 셋팅
answer = []
number_list = []
while value < 1000000 :
    number_list = []
    number = value
    number_list.append(number)
    while number > 2 :
        if number%2 == 0 :
            number = number/2
            number_list.append(number)
        else :
            number = 3*number + 1
            number_list.append(number)
    if len(number_list) > len(answer) :
        answer = number_list               
    value += 1
    print(answer[0])

#걸린 시간 : 32.96388530731201 seconds
