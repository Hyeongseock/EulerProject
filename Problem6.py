'''
Sum square difference
Problem 6
'''

'''
English version
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''


a = 0    #The sum of the Square
b = 0    #The Square of the sum

#loof from 1 to 100
#Pyhton range 1 to 100 is actually 1 to 99. So plus 1 the last number
for i in range(1,101) :
    a += i*i
    b += i
answer = b * b - a  #The Square of the sum - The sum of the Square
print(answer)
        

#time spent : 0.0 seconds      




'''
Korean version
1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같습니다 (제곱의 합).
12 + 22 + ... + 102 = 385
1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같습니다 (합의 제곱).
(1 + 2 + ... + 10)2 = 552 = 3025
따라서 1부터 10까지 자연수에 대해 "합의 제곱"과 "제곱의 합" 의 차이는 3025 - 385 = 2640 이 됩니다.
그러면 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는 얼마입니까?
'''


a = 0    #제곱의 합
b = 0    #합의 제곱

#1부터 100까지 반복
#파이썬의 경우 range 1부터 100은 실제로는 1부터 99이다. 그래서 마지막 숫자에 1을 더해야한다.
for i in range(1,101) :
    a += i*i
    b += i
answer = b * b - a  #합의 제곱 - 제곱의 합
print(answer)
        

#걸린 시간 : 0.0 seconds  
