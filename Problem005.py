'''
Smallest multiple
Problem 5
'''

'''
English version
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

#Setting initial number
j = 2520 # smallest positive number may be more than 2520
remainder = 0
while remainder == 0: #Loof until remainder is 0
    remainder_list = []
    for i in range(1, 20) :
        remainder_list.append(j%i) #Divide j to i. And add the remainder in list.
    if max(remainder_list) == 0 :  #Check whether can be divided by each of the numbers from 1 to 20.
        remainder = 1
        print(j)
    else :
        remainder = 0
        j += 20           #The smallest number should be divided by 20. That's why + 20 continually
    if j%1000000 == 0 :   #Check process
        print(j,"th passed")
        


#time spent : 32.792 seconds      




'''
Korean version
1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?
'''

#초기값 설정
j = 2520 # 가장 작은 수는 2520보다는 커야한다.
remainder = 0
while remainder == 0: #나머지가 0이 될 때까지 반복
    remainder_list = []
    for i in range(1, 20) :
        remainder_list.append(j%i) #j를 i로 나눈다. 그리고 리스트에 나머지를 넣는다.
    if max(remainder_list) == 0 :  #1부터 20까지의 숫자로 나눠지는지 체크한다.
        remainder = 1
        print(j)
    else :
        remainder = 0
        j += 20           #가장 작은 수는 20으로 나누어져야한다. 그래서 계속 20씩 증가시키는 이유이다.
    if j%1000000 == 0 :   #어떤 숫자를 지나는지 체크
        print(j,"th passed")
        


#걸린 시간 : 32.792 seconds      


