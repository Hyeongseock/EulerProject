'''
Special Pythagorean triplet
Problem 9
'''

'''
English version
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''



a = 0
b = 0
c = 0
#i == a and i is the smallest number among 3 numbers.
#So, i's max number is 332.(a < b < c ==> 332 < 333 < 335)
for i in range(1,333):    
    a = i
    b = 1000 - a
    for j in range(2, b) : #j == b and j is the secondary biggest number among 3 number. So, j's min number is 2 because j is bigger than i
        c = 1000 - i - j   # c number depends on a and b(i and j)
        square_a = a*a
        square_b = j*j
        square_c = c*c
        if square_a + square_b == square_c : #check Pythagorean triplet
            print(a, j, c)
            print(a * j * c) #answer
            break 


#time spent : 0.069 seconds     



'''
Korean version
세 자연수 a, b, c 가 피타고라스 정리 a2 + b2 = c2 를 만족하면 피타고라스 수라고 부릅니다 (여기서 a < b < c ).
예를 들면 32 + 42 = 9 + 16 = 25 = 52이므로 3, 4, 5는 피타고라스 수입니다.
a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?
'''


a = 0
b = 0
c = 0
#i는 a이고 i는 a,b,c중에 가장 작은 값이다.
#그러므로 i의 최대값은 332이다.(a<b<c이며 최대값은 332<333<335의 경우를 따른다.)
for i in range(1,333):    
    a = i
    b = 1000 - a
    for j in range(2, b) : #j는 b이며 a,b,c중에 두번째로 크다. 그러므로 j의 최소값은 i보다 커야하므로 2이다.
        c = 1000 - i - j   # c 숫자는 a와 b에 따라 달라진다.
        square_a = a*a
        square_b = j*j
        square_c = c*c
        if square_a + square_b == square_c : #피타고라스 함수인지 확인하기
            print(a, j, c)
            print(a * j * c) #
            break 


#걸린 시간 : 0.069 seconds     
