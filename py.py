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
print(mart.keys())
print(mart.values())
print(mart.items()) # items : Key와 Value를 튜플로 모아서 가져오기: 수정은 불가!

for fruit, price in mart.items():
    print(f'{fruit}의 가격은 {price}원 입니다.')