# 고정 길이 스택 클래스 FixedStack 구현하기


from re import M
from tkinter import N
from typing import Any

from tenacity import retry

# class FixedStack:
#     """고정 길이 스택 클래스"""

#     class Empty(Exception):
#         """비어 있는 FixedStack에 팝 또는 피크할 때 내보내는 예외 처리"""
#         pass

#     class Full(Exception):
#         """가득 찬 FixedStack에 푸시할 때 내보내는 예외 처리"""
#         pass

#     def __init__(self, capacity: int = 256) -> None:
#         """스택 초기화"""
#         self.stk = [None] * capacity    # 스택 본체
#         self.capacity = capacity        # 스택의 크기
#         self.ptr = 0                    # 스택 포인터

#     def __len__(self) -> int:
#         """스택에 쌓여 있는 데이터 개수를 반환"""
#         return self.ptr
    
#     def is_empty(self) -> bool:
#         """스택이 비어 있는지 판단"""
#         return self.ptr <= 0

#     def is_full(self) -> bool:
#         """스택이 가득 차 있는지 판단"""
#         return self.ptr >= self.capacity

#     def push(self, value: Any) -> None:
#         """스택에 value를 푸시(데이터를 넣음)"""
#         if self.is_full():          # 스택이 가득 차 있는 경우
#             raise FixedStack.Full   # 예외 처리 발생
#         self.stk[self.ptr] = value
#         self.ptr += 1

#     def pop(self) -> Any:
#         """스택에서 데이터를 팝(꼭대기 데이터를 꺼냄)"""
#         if self.is_empty():         # 스택이 비어 있는 경우
#             raise FixedStack.Empty  # 예외 처리 발생
#         self.ptr -= 1
#         return self.stk[self.ptr]
    
#     def peek(self) -> Any:
#         """스택에서 데이터를 피크(꼭대기 데이터를 들여다봄)"""
#         if self.is_empty():         # 스택이 비어 있음
#             raise FixedStack.Empty  # 예외 처리 발생
#         return self.stk[self.ptr - 1]
    
#     def clear(self) -> None:
#         """스택을 비움(모든 데이터를 삭제)"""
#         self.ptr = 0

#     def find(self, value: Any) -> Any:
#         """스택에서 value를 찾아 인덱스를 반환(없으면 -1을 반환)"""
#         for i in range(self.ptr - 1, -1, -1):   # 꼭대기 쪽부터 선형 검색
#             if self.stk[i] == value:
#                 return i        # 검색 성공
#         return -1               # 검색 실패

#     def count(self, value: Any) -> bool:
#         """스택에 있는 value의 개수를 반환"""
#         c = 0
#         for i in range(self.ptr):           # 바닥 쪽부터 선형 검색
#             if self.stk[i] == value:        # 검색 성공
#                 c += 1
#         return c
    
#     def __contains__(self, value: Any) -> bool:
#         """스택에 value가 있는지 판단"""
#         return self.count(value)
    
#     def dump(self) -> None:
#         """덤프(스택 안의 모든 데이터를 바닥까지 꼭대기 순으로 출력)"""
#         if self.is_empty():         # 스택이 비어있음
#             print('스택이 비어 있습니다.')
#         else:
#             print(self.stk[:self.ptr])


# 고정 길이 스택 클래스 구현하기(collections.deque를 사용)
# 165p. 모듈 참고


# from collections import deque

# class Stack:
#     """고정 길이 스택 클래스(collections.deque를 사용)"""

#     def __init__(self, maxlen: int = 256) -> None:
#         """스택 초기화"""
#         self.capacity = maxlen
#         self.__stk = deque([], maxlen)

#     def __len__(self) -> int:
#         """스택에 쌓여 있는 데이터 개수를 반환"""
#         return len(self.__stk)
    
#     def is_empty(self) -> bool:
#         """스택이 비어 있는지 판단"""
#         return not self.__stk

#     def is_full(self) -> bool:
#         """스택이 가득 차 있는지 판단"""
#         return len(self.__stk) == self.__stk.maxlen

#     def push(self, value: Any) -> None:
#         """스택에 value를 푸시(데이터를 넣음)"""
#         self.__stk.append(value)

#     def pop(self) -> Any:
#         """스택에서 데이터를 팝(꼭대기 데이터를 꺼냄)"""
#         return self.__stk.pop()
    
#     def peek(self) -> Any:
#         """스택에서 데이터를 피크(꼭대기 데이터를 들여다봄)"""
#         return self.__stk[-1]
    
#     def clear(self) -> None:
#         """스택을 비움(모든 데이터를 삭제)"""
#         self.__stk.clear()

#     def find(self, value: Any) -> Any:
#         """스택에서 value를 찾아 인덱스를 반환(없으면 -1을 반환)"""
#         try:
#             return self.__stk.index(value)
#         except ValueError:
#             return -1

#     def count(self, value: Any) -> bool:
#         """스택에 있는 value의 개수를 반환"""
#         return self.__stk.count(value)
    
#     def __contains__(self, value: Any) -> bool:
#         """스택에 value가 있는지 판단"""
#         return self.count(value)
    
#     def dump(self) -> None:
#         """덤프(스택 안의 모든 데이터를 바닥까지 꼭대기 순으로 출력)"""
#         print(list(self.__stk))


    

# # 고정 길이 스택 클래스(FixedStack)를 사용하기

# from enum import Enum

# Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])

# def select_menu() -> Menu:
#     """메뉴 선택"""
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep='  ', end='')
#         n = int(input(': '))
#         if 1 <= n <= len(Menu):
#             return Menu(n)

# s = FixedStack(64)              # 최대 64개를 푸시할 수 있는 스택

# while True:
#     print(f'현재 데이터 개수: {len(s)} / {s.capacity}')
#     menu = select_menu()        # 메뉴 선택

#     if menu == Menu.푸시:       # 푸시
#         x = int(input('데이터를 입력하세요.: '))
#         try:
#             s.push(x)
#         except FixedStack.Full:
#             print('스택이 가득 차 있습니다.')
    
#     elif menu == Menu.팝:       # 팝
#         try:
#             x = s.pop()
#             print(f'팝한 데이터는 {x}입니다.')
#         except FixedStack.Empty:
#             print('스택이 비어 있습니다.')
    
#     elif menu == Menu.피크:     #피크
#         try:
#             x = s.peek()
#             print(f'피크한 데이터는 {x}입니다.')
#         except FixedStack.Empty:
#             print('스택이 비어 있습니다.')
    
#     elif menu == Menu.검색:     # 검색
#         x = int(input('검색할 값을 입력하세요.: '))
#         if x in s:
#             print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.')
#         else:
#             print('검색값을 찾을 수 없습니다.')
    
#     elif menu == Menu.덤프:     # 덤프
#         s.dump()
    
#     else:
#         break

  

# # 고정 길이 스택 클래스(Stack)를 사용하기

# from enum import Enum

# Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])

# def select_menu() -> Menu:
#     """메뉴 선택"""
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep='  ', end='')
#         n = int(input(': '))
#         if 1 <= n <= len(Menu):
#             return Menu(n)

# s = Stack(64)              # 최대 64개를 푸시할 수 있는 스택

# while True:
#     print(f'현재 데이터 개수: {len(s)} / {s.capacity}')
#     menu = select_menu()        # 메뉴 선택

#     if menu == Menu.푸시:       # 푸시
#         x = int(input('데이터를 입력하세요.: '))
#         try:
#             s.push(x)
#         except Stack.Full:
#             print('스택이 가득 차 있습니다.')
    
#     elif menu == Menu.팝:       # 팝
#         try:
#             x = s.pop()
#             print(f'팝한 데이터는 {x}입니다.')
#         except Stack.Empty:
#             print('스택이 비어 있습니다.')
    
#     elif menu == Menu.피크:     #피크
#         try:
#             x = s.peek()
#             print(f'피크한 데이터는 {x}입니다.')
#         except Stack.Empty:
#             print('스택이 비어 있습니다.')
    
#     elif menu == Menu.검색:     # 검색
#         x = int(input('검색할 값을 입력하세요.: '))
#         if x in s:
#             print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.')
#         else:
#             print('검색값을 찾을 수 없습니다.')
    
#     elif menu == Menu.덤프:     # 덤프
#         s.dump()
    
#     else:
#         break






# # 고정 길이 큐 클래스 FixedQueue 구현하기

# from typing import Any

# class FixedQueue:

#     class Empty(Exception):
#         """비어 있는 FixedQueue에서 디큐 또는 피크할 때 내보내는 예외 처리"""
#         pass

#     class Full(Exception):
#         """가득 차 있는 FixedQueue에서 인큐할 때 내보내는 예외 처리"""
#         pass

#     def __init__(self, capacity: int) -> None:
#         """큐 초기화"""
#         self.no = 0                     # 현재 데이터 개수
#         self.front = 0                  # 맨 앞 원소 커서
#         self.rear = 0                   # 맨 끝 원소 커서
#         self.capacity = capacity        # 큐의 크기
#         self.que = [None] * capacity    # 큐의 본체

#     def __len__(self) -> int:
#         """큐에 있는 모든 데이터 개수를 반환"""
#         return self.no
    
#     def is_empty(self) -> bool:
#         """큐가 비어 있는지 판단"""
#         return self.no <= 0

#     def is_full(self) -> bool:
#         """큐가 가득 차 있는지 판단"""
#         return self.no >= self.capacity
    
#     def enque(self, x: Any) -> None:
#         """데이터 x를 인큐"""
#         if self.is_full():
#             raise FixedQueue.Full       # 큐가 가득 차 있는 경우 예외 처리 발생
#         self.que[self.rear] = x
#         self.rear += 1
#         self.no += 1
#         if self.rear == self.capacity:
#             self.rear = 0

#     def deque(self) -> Any:
#         """데이터를 디큐"""
#         if self.is_empty():
#             raise FixedQueue.Empty      # 큐가 비어 있는 경우 예외 처리 발생
#         x = self.que[self.front]
#         self.front += 1
#         self.no -= 1
#         if self.front == self.capacity:
#             self.front = 0
#         return x

#     def peek(self) -> Any:
#         """큐에서 데이터를 피크(맨 앞 데이터를 들여다봄)"""
#         if self.is_empty():
#             raise FixedQueue.Empty      # 큐가 비어 있는 경우 예외 처리를 발생
#         return self.que[self.front]

#     def find(self, value: Any) -> Any:
#         """큐에서 value를 찾아 인덱스를 반환(없으면 -1을 반환)"""
#         for i in range(self.no):
#             idx = (i + self.front) % self.capacity
#             if self.que[idx] == value:  # 검색 성공
#                 return idx
#         return -1                       # 검색 실패

#     def count(self, value: Any) -> bool:
#         """큐에 있는 value의 개수를 반환"""
#         c = 0
#         for i in range(self.no):        # 큐 데이터를 선형 검색
#             idx = (i + self.front) % self.capacity
#             if self.que[idx] == value:  # 검색 성공
#                 c += 1                  # 들어 있음
#         return c

#     def __contains__(self, value: Any) -> bool:
#         """큐에 value가 있는지 판단"""
#         return self.count(value)
    
#     def clear(self) -> None:
#         """큐의 모든 데이터를 비움"""
#         self.no = self.front = self.rear = 0

#     def dump(self) -> None:
#         """모든 데이터를 맨 앞부터 맨 끝 순으로 출력"""
#         if self.is_empty():             # 큐가 비어 있음
#             print('큐가 비었습니다.')
#         else:
#             for i in range(self.no):
#                 print(self.que[(i + self.front) % self.capacity], end=' ')
#             print()





# # 고정 길이 큐 클래스(FixedQueue)를 사용하기

# from enum import Enum

# Menu = Enum('Menu', ['인큐', '디큐', '피크', '검색', '덤프', '종료'])

# def select_menu() -> Menu:
#     """메뉴 선택"""
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep='  ', end='')
#         n = int(input(': '))
#         if 1 <= n <= len(Menu):
#             return Menu(n)

# q = FixedQueue(64)

# while True:
#     print(f'현재 데이터 개수: {len(q)} / {q.capacity}')
#     menu = select_menu()            # 메뉴 선택

#     if menu == Menu.인큐:       # 인큐
#         x = int(input('인큐할 데이터를 입력하세요: '))
#         try:
#             q.enque(x)
#         except FixedQueue.Full:
#             print('큐가 가득 찼습니다.')

#     elif menu == Menu.디큐:     # 디큐
#         try:
#             x = q.deque()
#             print(f'디큐한 데이터는 {x}입니다.')
#         except FixedQueue.Empty:
#             print('큐가 비어 있습니다.')

#     elif menu == Menu.피크:     # 피크
#         try:
#             x = q.peek()
#             print(f'피크한 데이터는 {x}입니다.')
#         except FixedQueue.Empty:
#             print('큐가 비었습니다.')
    
#     elif menu == Menu.검색:     # 검색
#         x = int(input('검색할 값을 입력하세요.: '))
#         if x in q:
#             print(f'{q.count(x)}개 포함되고, 맨 앞의 위치는 {q.find(x)}입니다.')
#         else:
#             print('검색값을 찾을 수 없습니다.')
    
#     elif menu == Menu.덤프:     # 덤프
#         q.dump()
#     else:
#         break







# 원하는 개수(n)만큼 값을 입력받아 마지막 n개를 저장 [링 버퍼]


n = int(input('정수를 몇 개 저장할까요?: '))
a = [None] * n                      # 입력받은 값을 저장하는 배열

cnt = 0                             # 정수를 입력받은 개수
while True:
    a[cnt % n] = int(input((f'{cnt + 1}번째 정수를 입력하세요.: ')))
    cnt += 1

    retry = input(f'계속 할까요?(Y ... Yes/N ... No): ')
    if retry in {'N', 'n'}:         # N이나 n을 입력하면 더 이상 값을 받지 않음
        break

i = cnt - n
if i < 0: i = 0

while i < cnt:
    print(f'{i + 1}번째 = {a[i % n]}')
    i += 1