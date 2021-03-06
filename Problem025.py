'''
#-------------problem-------------
피보나치 수열은 아래와 같은 점화식으로 정의됩니다.
Fn = Fn-1 + Fn-2  (단, F1 = 1, F2 = 1).
이에 따라 수열을 12번째 항까지 차례대로 계산하면 다음과 같습니다.
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
수열의 값은 F12에서 처음으로 3자리가 됩니다.
피보나치 수열에서 값이 처음으로 1000자리가 되는 것은 몇번째 항입니까?
#-------------solution-------------
1. 피보나치 수열을 구하는 식을 만든다.
2. 수열을 구할 때마다 +1씩 증가하는 변수 i를 만든다.
3. 수열의 값 길이가 1000과 같아질 때까지 피보나치 수열을 구한다.
4. 1000과 같아졌을 때의 i를 프린트한다.
#-------------code-------------
#최초의 값 설정하기
a = 1
b = 0
sum = 0
i = 1
#수열의 값 길이가 1000과 같아질 때까지 피보나치 수열을 구하기
while len(str(sum)) < 1000 :
    i += 1
    sum = a + b
    b = a
    a = sum
print(i)
#-------------spending time-------------
# 0.0330 seconds ---
