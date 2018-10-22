'''
#-------------problem-------------
여기 5천개 이상의 영문 이름들이 들어있는 46KB짜리 텍스트 파일 names.txt 이 있습니다 (우클릭해서 다운로드 받으세요).
이제 각 이름에 대해서 아래와 같은 방법으로 점수를 매기고자 합니다.
먼저 모든 이름을 알파벳 순으로 정렬합니다.
각 이름에 대해서, 그 이름을 이루는 알파벳에 해당하는 숫자(A=1, B=2, ..., Z=26)를 모두 더합니다.
여기에 이 이름의 순번을 곱합니다.
예를 들어 "COLIN"의 경우, 알파벳에 해당하는 숫자는 3, 15, 12, 9, 14이므로 합이 53, 그리고 정렬했을 때 938번째에 오므로 최종 점수는 938 × 53 = 49714가 됩니다.
names.txt에 들어있는 모든 이름의 점수를 계산해서 더하면 얼마입니까?
#-------------solution-------------
1. 알파벳과 숫자의 쌍을 dict 형태로 만든다(예: a = 1, b = 2... z = 26)
2. names에 있는 이름들을 알파벳 순서로 정렬함으로써 순서 정보(순번)를 획득한다.
3. 이름 내 각 알파벳들을 숫자로 변환하고 더한다.
4. 더한 숫자에 이름의 순번을 곱한다.
5. 모든 이름들에서 3-4번 작업을 진행한 뒤, 모든 값을 더해준다.
#-------------code-------------
#솔루션 1번 진행
alphabet_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
                 "Q","R","S","T","U","V","W","X","Y","Z"]
alphabet_dic = {}
a = 1
for i in alphabet_list :
    alphabet_dic[i] = a
    a += 1

#파일에서 이름 정보 가져오기
with open("Q21_names.txt", 'r') as file :
    names = file.read()
file.close()
names = names.split(",")
name_list = []
for i in names :
    name = i[1:len(i)-1]
    name_list.append(name)
name_list.sort()      #솔루션 2번진행
answer = 0  #솔루션 5번에 사용되는 모든 값을 더할 객체 생성

for name in name_list :
    name_index = name_list.index(name) + 1  #솔루션 2번 순서정보를 구하기
    sum_spell = 0
    for spell in name :
        sum_spell += alphabet_dic[spell]   #솔루션 3번 진행
    answer += name_index*sum_spell    #솔루션 4번과 5번 동시 진행
print(answer)
#-------------spending time-------------
# 0.6230356693267822 seconds 
