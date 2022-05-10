# # 양의 정수 n의 팩토리얼 구하기


# def factorial(n: int) -> int:
#     """양의 정수 n의 팩토리얼값을 재귀적으로 구함"""
#     if n > 0:
#         return n * factorial(n - 1)
#     elif n < 0:
#         return None
#     else:
#         return 1


# if __name__ == '__main__':
#     n = int(input('출력할 팩토리얼값을 입력하세요.: '))
#     print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')




# # 유클리드 호제법으로 최대 공약수 구하기

# def gcd(x: int, y: int) -> int:
#     """정숫값 x와 y의 최대 공약수를 반환"""
#     if y == 0:
#         return x
#     else:
#         return gcd(y, x % y)

# if __name__ == '__main__':
#     print('두 정숫값의 최대 공약수를 구합니다.')
#     x = int(input('첫 번째 정수값을 입력하세요.: '))
#     y = int(input('두 번째 정수값을 입력하세요.: '))

#     print(f'두 정숫값의 최대 공약수는 {gcd(x,y)}입니다.')




# # 순수한 재귀 함수 구현하기

# def recur(n: int) -> int:
#     """순수한 재귀 함수 recur의 구현"""
#     if n > 0:
#         recur(n - 2)
#         print(n)
#         recur(n - 1)

# x = int(input('정숫값을 입력하세요.: '))

# recur(x)




# # 비재귀적으로 재귀 함수 구현하기(꼬리 재귀를 제거)

# def recur(n: int) -> int:
#     """꼬리 재귀를 제거한 recur() 함수"""
#     while n > 0:
#         recur(n - 1)
#         print(n)
#         n = n - 2

# x = int(input('정숫값을 입력하세요.: '))

# recur(x)




# 스택으로 재귀 함수 구현하기(재귀를 제거)

