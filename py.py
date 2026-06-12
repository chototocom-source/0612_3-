user = {
    'name' : '홍길동',
    'age' : 25,
    'skills' : ['Ptython', 'Git']
}

# 1. 대괄호 사용(가장 일반적)
print(user['name']) # 출력: 홍길동

# 2. get() method 사용(안전함)
print(user.get('age')) # 출력: 25

user['name'] = '스티브잡스'
print(user['name'],'은 나이가', user['age'], '먹었습니다.')

mart = {
    'apple' : 1000,
    'banana' : 2500,
    'orange' : 1500
}

mart['apple'] = 5000
print(mart)
print(mart.keys()) # 결과 list
print(mart.values()) # 결과 list
print(mart.items()) # items : Key와 Value를 튜플로 모아서 가져오기: 수정은 불가!, 결과 tuple

for fruit, price in mart.items():
    print(f'{fruit}의 가격은 {price}원 입니다.')

for key in mart.keys():
    print(f'mart 딕셔너리의 key값은 {key}가 있습니다.')


mart2 = {'apple' : 1000, 'banana' : 2500}

print('apple' in mart2) # True
print('grape' in mart2) # False

my_tuple = (1, 2, 3) # Tuple 인증같은 곳에 사용: 모두 충족해야함, 수정 불가
another_tuple = 10, 20, 30 # Tuple: 소괄호 생략 가능

my_list = [1, 2, 3]
my_list[0] = 99 # [99, 2, 3]으로 정상 변경

# 리스트와 튜플의 결정적 차이 (중요!)
# 리스트 []: 데이터 변경 가능. 수정, 추가, 삭제가 마음대로 가능합니다.
# 튜플 (): 데이터 변경 불가능. 한번 생성되면 절대 바꿀 수 없습니다.


numbers = (0, 1, 2, 3, 4, 5)
print(numbers[1 : 3 + 1]) # (1, 2, 3) -> index 1부터 3까지

a = (1, 2)
b= (3, 4)

print(a + b) # (1, 2, 3, 4) -> 새로운 튜플 형성
print(a * 3) # (1, 2, 1, 2, 1, 2) -> 3번 반복

# 1. 패킹
info = ('Tom', 20, 'Seoul')

# 2. 언패킹(튜플의 개수와 변수의 개수가 같아야 합니다.)
name, age, city = info

print(name) # Tom
print(age) # 20
print(city) # Seoul

x = 10
y = 20

# 두 값을 서로 바꾸기(튜플 언패킹 원리)
x, y = y, x
print(x) # 20
print(y) # 10


sample = (1, 2, 3, 2, 4, 2)
print(sample.count(2))
print(sample.index(3))

# 마음의 다짐을 함