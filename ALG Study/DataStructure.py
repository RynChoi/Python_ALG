  # 배열 원소의 최댓값을 구하는 함수 구현하기

# from typing import Any, Sequence

# def max_of(a: Sequence) -> Any:
#      """시퀀스형 a 원소의 최댓값을 반환"""
#      maximum = a[0]
#      for i in range(1,len()):
#          if a[i] > maximum:
#              maximum = a[i]
#      return maximum

# if __name__ == '__main__':
#      print('배열의 최댓값을 구합니다.')
#      num = int(input('원소 수를 입력하세요.: '))
#      x = [None] * num #원소 수가 num인 리스트를 생성
#      for i in range(num):
#          x[i] = int(input(f'x[{i}]값을 입력하세요.: '))
  
#      print(f'최댓값은 {max_of}입니다.')

    
#배열 원소의 최댓값을 구해서 출력하기(원솟값을 입력받음)

# from test import max_of

# print('배열의 최댓값을 구합니다.')
# print('주의: "End"를 입력하면 종료합니다.')

# number = 0
# x = []

# while True:
#     s = input(f'x[{number}]값을 입력하세요.: ')
#     if s == 'End':
#         break
#     x.append(int(s))
#     number += 1

# print(f'{number}개를 입력했습니다.')
# print(f'최댓값은 {max_of(x)}입니다.')


  #배열 원소의 최댓값을 구해서 출력하기(원솟값을 난수로 생성)



# import random
# from DataStructure import max_of

# print('난수의 최댓값을 구합니다.')
# num = int(input('난수의 개수를 입력하세요.: '))
# lo = int(input('난수의 최솟값을 입력하세요.: '))
# hi = int(input('난수의 최댓값을 입력하세요.: '))
# x = [None] * num

# for i in range(num):
#     x[i] = random.randint(lo, hi)

# print(f'{(x)}')
# print(f'이 가운데 최댓값은 {max_of}입니다.')




# 각 배열 원소의 최댓값을 구해서 출력하기(튜플, 문자열, 문자열 리스트)

# from DataStructure import max_of

# t = (4, 7, 5.6, 2, 3.14, 1)
# s = 'string'
# a = ['DTS', 'AAC', 'FLAC']

# print(f'{t}의 최댓값은 {max_of(t)}입니다.')
# print(f'{s}의 최댓값은 {max_of(s)}입니다.')
# print(f'{a}의 최댓값은 {max_of(a)}입니다.')




# 뮤터블 시퀀스 원소를 역순으로 정렬

# from typing import Any, MutableSequence

# def reverse_array(a: MutableSequence) -> None:
#   """뮤터블 시퀀스 a의 원소를 역순으로 정렬"""
#   n = len(a)
#   for i in range(n // 2):
#     a[i], a[n - i - 1] = a[n - i - 1], a[i]

# if __name__ == '__main__':
#   print('배열 원소를 역순으로 정렬합니다.')
#   nx = int(input('원소 수를 입력하세요.: '))
#   x = [None] * nx #원소 수가 nx인 리스트를 생성

#   for i in range(nx):
#     x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

#   reverse_array(x) #x를 역순으로 정렬

#   print('배열 원소를 역순으로 정렬했습니다.')
#   for i in range(nx):
#     print(f'x[{i}] = {x[i]}')





# 10진수 정숫값을 입력받아 2~36진수로 변환하여 출력하기

# def card_conv(x: int, r: int) -> str:
#   """정숫값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""

#   d = '' #변환 후의 문자열
#   dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#   while x > 0:
#     d += dchar[x % r]
#     x //= r
  
#   return d[::-1]


# if __name__ == '__main__':
#   print('10진수를 n진수로 변환합니다.')

#   while True:
#     while True: #음이 아닌 정수를 입력받음
#       no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요.: '))
#       if no > 0:
#         break
    
#     while True : #2~36진수의 정숫값을 입력받음
#       cd = int(input('어떤 진수로 변환할까요?: '))
#       if 2 <= cd <= 36:
#         break
    
#     print(f'{cd}진수로는 {card_conv(no,cd)}입니다.')

#     retry = input("한 번 더 변환할까요?(Y ... 예 / N ... 아니요): ")
#     if retry in {'N','n'}:
#       break




# 리스트에서의 임의의 원솟값을 업데이트하기

# def change(lst, idx, val):
#   """lst[idx]의 값을 val로 업데이트"""
#   lst[idx] = val

# x = [11, 22, 33, 44, 55]
# print('x= ', x)

# index = int(input('업데이트할 인덱스를 선택하세요.: '))
# value = int(input('새로운 값을 입력하세요.: '))

# change(x, index, value)
# print(f'x = {x}')





# # 1,000 이하의 소수를 나열하기

# counter = 0 #나눗셈 횟수를 카운트

# for n in range(2, 1001):
#   for i in range(2, n):
#     counter += 1
#     if n % i == 0: # 나누어 떨어지면 소수가 아님
#       break
  
#   else: #끝까지 나누어 떨어지지 않으면 다음을 수행
#     print(n)
# print(f'나눗셈을 실행한 횟수: {counter}')



# # 1,000 이하의 소수를 나열하기 (알고리즘 개선 1)

# counter = 0             #나눗셈 횟수를 카운트
# ptr = 0                 #이미 찾은 소수의 개수
# prime = [None] * 500    #소수를 저장하는 배열

# prime[ptr] = 2          #2는 소수이므로 초깃값으로 지정
# ptr += 1

# for n in range(3, 1001, 2): #홀수만을 대상으로 설정
#   for i in range(1, ptr):   #이미 찾은 소수로 나눔
#     counter += 1
#     if n % prime[i] == 0:   #나누어 떨어지면 소수가 아님
#       break                 #반복 중단
    
#   else:
#     prime[ptr] = n          #소수로 배열에 등록
#     ptr += 1

# for i in range(ptr):        #ptr의 소수를 출력
#   print(prime[i])
# print(f'나눗셈을 실행한 횟수: {counter}')





# 1,000 이하의 소수를 나열하기 (알고리즘 개선 2)

counter = 0             #나눗셈 횟수를 카운트
ptr = 0                 #이미 찾은 소수의 개수
prime = [None] * 500    #소수를 저장하는 배열

prime[ptr] = 2
ptr += 1

prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):
  i = 1
  while prime[i] * prime[i] <= n:
    counter += 2
    if n % prime[i] == 0:
      break
    i += 1
  else:
    prime[ptr] = n
    ptr += 1
    counter += 1

for i in range(ptr):
  print(prime[i])
print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')