'''
Largest prime factor
Problem 3
'''

'''
English version
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

#Setting initial value 
number = 600851475143

#Finding prime factor
#It is a formula for getting prime factor
#If you don't use this formular, you will divide target number to all value which is less than it.
for x in range(1,number) :
    if number%x == 0 :
        print(x)
        number /= x
        print(number)
        if number == 1 :
            break
            
            
#time spent : 0.001 seconds            
        






'''
Korean version
어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고, 이 소수들을 그 수의 소인수라고 합니다.
예를 들면 13195의 소인수는 5, 7, 13, 29 입니다.
600851475143의 소인수 중에서 가장 큰 수를 구하세요.
'''

#초기값 설정
number = 600851475143

#소인수분해하기
#이것은 소인수를 구하는 공식입니다.
#이 공식을 쓰지 않을 경우, number 값을 number 값보다 작은 모든 값으로 나누어줘야 합니다.
for x in range(1,number) :
    if number%x == 0 :
        print(x)
        number /= x
        print(number)
        if number == 1 :
            break


#걸린 시간 : 0.001 seconds           
