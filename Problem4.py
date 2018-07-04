'''
Largest palindrome product
Problem 4
'''

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

#Make empty list to add number
number_list = []

#the first number is 100 because of 3-digit number
for i in range(100, 999) :
    for j in range(100, 999) :
        number = i * j
        number = str(number)    #transforming from integer to string for checking each digit number 
        if len(number) == 6 :   #check number's lenth 
            if number[0]==number[5] and number[1]==number[4] and number[2]==number[3] :   #check whether the number is palindrome
                number_list.append(int(number))
print(max(number_list)) 


#time spent : 0.312 seconds      






'''
Korean version
앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.
두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.
세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?
'''

#숫자를 넣어줄 리스트를 생성
number_list = []

#세 자리 수 두개를 곱해야 하므로 최초의 값은 100
for i in range(100, 999) :
    for j in range(100, 999) :
        number = i * j
        number = str(number)    #각각의 자리수에 어떤 숫자가 있는지 체크하기 위해 integer에서 string으로 타입 변환
        if len(number) == 6 :   #6자리인지 체크
            if number[0]==number[5] and number[1]==number[4] and number[2]==number[3] :   #대칭수인지 체크
                number_list.append(int(number))
print(max(number_list)) 


#걸린 시간 : 0.312 seconds      

