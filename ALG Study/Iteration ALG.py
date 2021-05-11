### 1부터 n까지 정수의 합 구하기

## 1부터 n까지 정수의 합 구하기 1(while 문)

# print('1부터 n까지의 정수의 합을 구합니다.')
# n = int(input('n값을 입력하세요: '))

# sum = 0
# i = 1

# while i <= n:
#     sum += i
#     i += 1

# print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
# print(f'i값은 {i}입니다.')






## 1부터 n까지 정수의 합 구하기 2(for)문

# print('1부터 n까지 정수의 합을 구합니다.')
# n = int(input('n값을 입력하세요: '))

# sum = 0
# for i in range(1, n + 1):
#     sum += i

# print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')




### 연속하는 정수의 합을 구하기 위해 값 정렬하기




## a부터 b까지 정수의 합 구하기(for 문)

# print('a부터 b까지 정수의 합을 구합니다.')
# a = int(input('정수 a를 입력하세요: '))
# b = int(input('정수 b를 입력하세요: '))

# if a > b:
#     a, b = b, a

# sum = 0
# for i in range(a, b + 1):
#     sum += i
# print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')




### 반복 과정에서 조건 판단하기



## a부터 b까지 정수의 합 구하기 1

# print('a부터 b까지 정수의 합을 구합니다.')
# a = int(input('정수 a를 입력하세요: '))
# b = int(input('정수 b를 입력하세요: '))

# if a > b:
#     a, b = b, a

# sum = 0
# for i in range(a, b + 1):
#     if i < b:
#         print(f'{i} + ', end='')
#     else:
#         print(f'{i} = ', end='')
#     sum += i

# print(sum)


# 깃 추가 테스트


## a부터 b까지 정수의 합 구하기 2

# print('a부터 b까지 정수의 합을 구합니다.')
# a = int(input('정수 a를 입력하세요: '))
# b = int(input('정수 b를 입력하세요: '))

# if a > b:
#     a, b = b, a

# sum = 0

# for i in range(a, b):
#     print(f'{i} + ', end='')
#     sum += i

# print(f'{b} = ', end='')
# sum += b

# print(sum)




## +와 -를 번갈아 출력하기 1

# print('+와 -를 번갈아 출력합니다.')
# n = int(input('몇 개를 출력할까요?: '))

# for i in range(n):
#     if i % 2:
#         print('-', end='')
#     else:
#         print('+', end='')
    
# print()





## +와 -를 번갈아 출력하기 2

# print('+와 -를 번갈아 출력합니다.')
# n = int(input('몇 개를 출력할까요?: '))

# for _ in range(n // 2): #//를 이용하여 몫만 나타낸다.
#     print('+-', end='') #+-를 n // 2개의 출력

# if n % 2:
#     print('+', end='') #n이 홀수일 때만 +를 출력

# print()
