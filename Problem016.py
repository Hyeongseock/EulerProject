'''
Power digit sum
Problem 16
'''

'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?
'''

value = 2**1000
value = str(value)
answer = 0
for i in str(value) :
    answer += int(i)
print(answer)

#time spent : 0.0 seconds



'''
Korean version
215 = 32768 의 각 자리수를 더하면 3 + 2 + 7 + 6 + 8 = 26 입니다.
21000의 각 자리수를 모두 더하면 얼마입니까?
'''


value = 2**1000
value = str(value)
answer = 0
for i in str(value) :
    answer += int(i)
print(answer)

#걸린 시간 : 0.0 seconds
