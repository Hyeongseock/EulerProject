'''
Counting Sundays
Problem 19
'''
'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

monday = ["화요일","수요일","목요일","금요일","토요일","일요일","월요일"]
month = [1,2,3,4,5,6,7,8,9,10,11,12]
day = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,29],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,29,30],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,29,30,31]]
#1901년 1월 1일은 화요일
thirty_month = [4, 6, 9, 11]
thirtyone_month=[1,3,5,7,8,10,12]
answer_list = []
answer_dic = {}
for i in range(1901, 2001) :
    for j in month :
        if thirty_month.count(j) == 1 :
            month_days = day[2]
        elif thirtyone_month.count(j) == 1 :
            month_days = day[3]
        else :
            month_days = day[0]
            if i%4 == 0 :
                month_days = day[1]
        for k in month_days :
            answer_list.append([i,j,k])
for i in range(len(answer_list)) :
    namerji = (i)%7
    answer_dic[i] = monday[namerji]
count_number = 0
for i in range(len(answer_dic)) :
    if answer_dic[i] == "일요일" :
        temp = answer_list[i]
        if temp[2] == 1:
            count_number += 1
print(count_number)

#------ 0.016000986099243164 seconds ---
