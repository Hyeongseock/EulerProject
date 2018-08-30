'''
Number letter count
Problem 17
'''

'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

#put the number which is repeate to dic
number_dic ={1 : "one",
               2 : "two",
               3 : "three",
               4 : "four",
               5 : "five",
               6 : "six",
               7 : "seven",
               8 : "eight",
               9 : "nine",
               10 :"ten",
               11: "eleven",
               12: "twelve",
               13: "thirteen",
               14: "fourteen",
               15: "fifteen",
               16: "sixteen",
               17: "seventeen",
               18: "eightteen",
               19: "nineteen",
               20: "twenty",
               30: "thirty",
               40: "forty",
               50: "fifty",
               60: "sixty",
               70: "seventy",
               80: "eighty",
               90: "ninety",
               100: "hundred",
               1000: "thousand",
               "end" : "and"}
               
#위의 사전에 없는 값들은 계속해서 추가해나가는 방식으로 진행할 예정
#1의 자리, 10의 자리, 100의 자리인지 체크하기

for i in range(1,1000) :
    check_exist_number = i in number_dic
    if check_exist_number == False:
        check_digitnumber = len(str(i))
        digitnumber = str(i)          
        #check 10 digit 
        if check_digitnumber == 2 :
            one_number = int(str(digitnumber[1]))
            ten_number = int(str(digitnumber[0]))*10
            number_dic[i] = number_dic[ten_number] + number_dic[one_number]
        #check 100 digit 
        elif check_digitnumber == 3 :
            one_number = int(str(digitnumber[2]))
            ten_number = int(str(digitnumber[1])) * 10
            one_to_ten_number = ten_number + one_number                
            hundred_number = 100                
            infront_hundred_number = int(str(digitnumber[0]))
            if one_to_ten_number == 0 :
                number_dic[i] = number_dic[infront_hundred_number] + number_dic[hundred_number]
            else :
                number_dic[i] = number_dic[infront_hundred_number] + number_dic[hundred_number] + number_dic["end"]+ number_dic[one_to_ten_number]

number_dic[1000] = "onethousand"
number_dic[100] = "onehundred"
del number_dic["end"]
sentecelenth = 0
for i in number_dic:
    print(number_dic[i])
    sentecelenth += len(number_dic[i])
    print(i, sentecelenth) #last sentecelenth is answer
    
 #--- 0.007000446319580078 seconds ---
 
'''
Problem 17

1부터 5까지의 숫자를 영어로 쓰면 one, two, three, four, five 이고,
각 단어의 길이를 더하면 3 + 3 + 5 + 4 + 4 = 19 이므로 사용된 글자는 모두 19개입니다.

1부터 1,000까지 영어로 썼을 때는 모두 몇 개의 글자를 사용해야 할까요?

참고: 빈 칸이나 하이픈('-')은 셈에서 제외하며, 단어 사이의 and 는 셈에 넣습니다.
  예를 들어 342를 영어로 쓰면 three hundred and forty-two 가 되어서 23 글자,
  115 = one hundred and fifteen 의 경우에는 20 글자가 됩니다.
'''


#반복적으로 나오는 숫자들은 딕셔너리 형태로 담아놓는다.
number_dic ={1 : "one",
               2 : "two",
               3 : "three",
               4 : "four",
               5 : "five",
               6 : "six",
               7 : "seven",
               8 : "eight",
               9 : "nine",
               10 :"ten",
               11: "eleven",
               12: "twelve",
               13: "thirteen",
               14: "fourteen",
               15: "fifteen",
               16: "sixteen",
               17: "seventeen",
               18: "eightteen",
               19: "nineteen",
               20: "twenty",
               30: "thirty",
               40: "forty",
               50: "fifty",
               60: "sixty",
               70: "seventy",
               80: "eighty",
               90: "ninety",
               100: "hundred",
               1000: "thousand",
               "end" : "and"}
               
#위의 사전에 없는 값들은 계속해서 추가해나가는 방식으로 진행할 예정
#1의 자리, 10의 자리, 100의 자리인지 체크하기

for i in range(1,1000) :
    check_exist_number = i in number_dic
    if check_exist_number == False:
        check_digitnumber = len(str(i))
        digitnumber = str(i)          
        #check 10 digit 
        if check_digitnumber == 2 :
            one_number = int(str(digitnumber[1]))
            ten_number = int(str(digitnumber[0]))*10
            number_dic[i] = number_dic[ten_number] + number_dic[one_number]
        #check 100 digit 
        elif check_digitnumber == 3 :
            one_number = int(str(digitnumber[2]))
            ten_number = int(str(digitnumber[1])) * 10
            one_to_ten_number = ten_number + one_number                
            hundred_number = 100                
            infront_hundred_number = int(str(digitnumber[0]))
            if one_to_ten_number == 0 :
                number_dic[i] = number_dic[infront_hundred_number] + number_dic[hundred_number]
            else :
                number_dic[i] = number_dic[infront_hundred_number] + number_dic[hundred_number] + number_dic["end"]+ number_dic[one_to_ten_number]

number_dic[1000] = "onethousand"
number_dic[100] = "onehundred"
del number_dic["end"]
sentencelength = 0
for i in number_dic:
    print(number_dic[i])
    sentencelength += len(number_dic[i])
    print(i, sentencelegnth) #last sentencelength is answer
    
 #--- 걸린 시간 : 0.007000446319580078 seconds ---  
    
