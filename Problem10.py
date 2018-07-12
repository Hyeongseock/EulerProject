'''
Summation of primes
Problem 10
'''

'''
English version
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

#there are 2 ways to solve this problem.
#one is my solution. but It is a little bit slow, so you feel like stupid.
#the other thing get from internet. I think it is a formular for getting prime number.
#It's very fast, but you should understand how to get prime number by using it to apply other things. 



# way
#Setting already known prime_list 
prime_list = [2,3,5,7,11,13]

#Setting first number. it is over than the last number in prime list.
i = 14

#roof until i > 2,000,000
#Getting prime number. ref by Problem7.py
while i <= 2000000 :
    remainer_list = []
    for j in prime_list :
        remainer = i % j
        remainer_list.append(remainer)
        
    if min(remainer_list) != 0: 
        prime_list.append(i)
    i += 1
    if i % 100000 == 0 :
        print(i,"th number passed.")
    print(sum(prime_list)) #answer

#time spent : 0.069 seconds     


#2th way. it's very fast..
end = 2000000
test = list(range(0,end+1))
test[0] = test[1] = 0
def is_prime(num):

    if num is 2 or 3 : return True
    for i in range(2,int(sqrt(num)+1)):
        if num % i is 0 : return False
    return True

start_time = time.time()
for i  in test:
    if i is 0 : continue
    if is_prime(i):
        for j in range(i*2,end+1,i):
            test[j] = 0
print(sum(test)) #answer




'''
Korean version
10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.
이백만(2,000,000) 이하 소수의 합은 얼마입니까?
'''


#문제를 푸는데는 2가지 방법이 있습니다.
#한 가지 방법은 제 방식입니다. 그러나 느립니다. 그래서 바보같이 느낄 수 있습니다.
#다른 방법은 인터넷에서 얻은 겁니다. 이 방식은 소수를 얻는 공식 같습니다.
#매우 빠릅니다. 하지만 소수를 얻는 원리를 다른 곳에 응용하기 위해서는 이 공식을 꼭 이해해야 합니다.


#이미 알고 있는 소수 리스트 셋팅
prime_list = [2,3,5,7,11,13]

#첫번째 숫자 셋팅하기. 소수 리스트의 마지막 숫자보다는 커야한다.
i = 14

#i 가 2000000을 넘을 때까지 돌기
#소수 얻기. Problem7.py 참조
while i <= 2000000 :
    remainer_list = []
    for j in prime_list :
        remainer = i % j
        remainer_list.append(remainer)
        
    if min(remainer_list) != 0: 
        prime_list.append(i)
    i += 1
    if i % 100000 == 0 :
        print(i,"th number passed.")
    print(sum(prime_list)) #정답!

#걸린 시간 : 0.069 seconds     


#두 번째 방법. 매우 빠름
end = 2000000
test = list(range(0,end+1))
test[0] = test[1] = 0
def is_prime(num):

    if num is 2 or 3 : return True
    for i in range(2,int(sqrt(num)+1)):
        if num % i is 0 : return False
    return True

start_time = time.time()
for i  in test:
    if i is 0 : continue
    if is_prime(i):
        for j in range(i*2,end+1,i):
            test[j] = 0
print(sum(test)) #정답
