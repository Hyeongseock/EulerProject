'''
10001st prime
Problem 7
'''

'''
English version
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

#Setting prime list
prime_list = [2,3,5,7,11,13]

#Setting the initial number of the roop 
i = 14

#loof until prime list's length is equal with 10001 
while len(prime_list < 10001) :
    remainder_list = []
    for prime in prime_list :
        remainder = i % prime
        remainder_list.append(remainder)
        
    if min(remainder_list) != 0: 
        prime_list.append(i) #if the minimum number of the remainder list is not zero, it would be prime.
    i += 1

#answer
print(prime_list[10000])



#time spent : 63.67 seconds     



'''
Korean version
소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.
이 때 10,001번째의 소수를 구하세요.
'''


#소수 리스트 셋팅
prime_list = [2,3,5,7,11,13]

#반복문 최초 시작값 셋팅
i = 14

#소수 리스트가 10001이 될 때까지 반복하기 
while len(prime_list < 10001) :
    remainder_list = []
    for prime in prime_list :
        remainder = i % prime
        remainder_list.append(remainder)
        
    if min(remainder_list) != 0: 
        prime_list.append(i) #만약 나머지의 최소 값이 0이 아닌 경우, 소수라도 판단할 수 있을 것이다(가정). 
    i += 1

#정답
print(prime_list[10000])



#걸린 시간 : 63.67 seconds     
