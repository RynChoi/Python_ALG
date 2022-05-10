#while 문으로 작성한 선형 검색 알고리즘

from copy import copy
from select import select
from typing import Any, Sequence

# def seq_search(a: Sequence, key: Any) -> int:
#     """시퀀스 a에서 key와 값이 같은 원소를 선형 검색(while 문)"""
#     i = 0

#     while True:
#         if i == len(a):
#             return -1   #검색에 실패하여 -1을 반환
#         if a[i] == key:
#             return i    # 검색에 성공하여 현재 검사한 배열의 인덱스를 반환
#         i += 1

# if __name__ == '__main__':
#     num = int(input('원소 수를 입력하세요.: '))         #num값을 입력받음
#     x = [None] * num                                  #원소 수가 num인 배열을 생성

#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))

#     ky = int(input('검색할 값을 입력하세요.: '))        #검색할 키 ky를 입력받음

#     idx = seq_search(x, ky)                           #ky와 값이 같은 원소를 x에서 검색

#     if idx == -1:
#         print('검색값을 갖는 원소가 존재하지 않습니다.')
#     else:
#         print(f'검색값은 x[{idx}]에 있습니다.')





# for 문으로 작성한 선형 검색 알고리즘

# def seq_search(a: Sequence, key: Any) -> int:
#     """시퀀스 a에서 key와 값이 같은 원소를 선형 검색(while 문)"""
#     for i in range(len(a)):
#         if a[i] == key:
#             return i    #검색 성공(인덱스를 반환)
#     return -1           #검색 실패(-1을 반환)


# #seq_search()함수를 사용하여 실수 검색하기

# print('실수를 검색합니다.')
# print('주의: "End"를 입력하면 종료합니다.')

# number = 0
# x = []                                              #빈 리스트 x를 생성

# while True:
#     s = input(f'x[{number}]: ')
#     if s == 'End':
#         break
#     x.append(float(s))                              #배열 맨 끝에 원소를 추가
#     number += 1

# ky = float(input('검색할 값을 입력하세요.: '))        #검색할 키 ky를 입력받기

# idx = seq_search(x, ky)                             #ky와 값이 같은 원소를 x에서 검색
# if idx == -1:
#     print('검색값을 갖는 원소가 존재하지 않습니다.')
# else:
#     print(f'검색값은 x[{idx}]에 있습니다.')




#seq_search() 함수를 사용하여 특정 인덱스 검색하기

# t = (4, 7, 5.6, 2, 3.14, 1)
# s = 'string'
# a = ['DTS', 'AAC', 'FLAC']

# print(f'{t}에서 5.6의 인덱스는 {seq_search(t,5.6)}입니다.')
# print(f'{s}에서 "n"의 인덱스는 {seq_search(s,"n")}입니다.')
# print(f'{a}에서 "DTS"의 인덱스는 {seq_search(a,"DTS")}입니다.')






# 선형 검색 알고리즘을 보초법으로 수정

# import copy

# def seq_search(seq: Sequence, key: Any) -> int:
#     """시퀀스 seq에서 key와 일치하는 원소를 선형 검색(보초법)"""
#     a = copy.deepcopy(seq)      #seq를 복사
#     a.append(key)               #보조 key를 추가

#     i = 0
#     while True:
#         if a[i] == key:
#             break               #검색에 성공하면 while 문을 종료
#         i += 1
#     return -1 if i == len(seq) else i

# if __name__ == '__main__':
#  num = int(input('원소 수를 입력하세요.: '))         #num값을 입력받음
#  x = [None] * num                                  #원소 수가 num인 배열을 생성

#  for i in range(num):
#      x[i] = int(input(f'x[{i}]: '))

#  ky = int(input('검색할 값을 입력하세요.: '))        #검색할 키 ky를 입력받음

#  idx = seq_search(x, ky)                           #ky와 값이 같은 원소를 x에서 검색

#  if idx == -1:
#      print('검색값을 갖는 원소가 존재하지 않습니다.')
#  else:
#      print(f'검색값은 x[{idx}]에 있습니다.')





# 이진 검색 알고리즘

# from typing import Any, Sequence

# def bin_search(a: Sequence, key: Any) -> int:
#     """시퀀스 a에서 key와 일치하는 원소를 이진 검색"""
#     pl = 0                      #검색 범위 맨 앞 원소의 인덱스
#     pr = len(a) - 1             #검색 범위 맨 끝 원소의 인덱스

#     while True:
#         pc = (pl + pr) // 2     #중앙 원소의 인덱스
#         if a[pc] == key:
#             return pc           #검색 성공
#         elif a[pc] < key:
#             pl = pc + 1         #검색 범위를 뒤쪽 절반으로 좁힘
#         else:
#             pr = pc - 1         #검색 범위를 앞쪽 절반으로 좁힘
#         if pl > pr:
#             break
#     return -1                   #검색 실패


# if __name__ == '__main__':
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num                            #원소 수가 num인 배열을 생성

#     print('배열 데이터을 오름차순으로 입력하세요.')

#     x[0] = int(input('x[0]: '))

#     for i in range(1, num):
#         while True:
#             x[i] = int(input(f'x[{i}]: '))
#             if x[i] >= x[i-1]:                  #바로 직전에 입력한 원솟값보다 큰 값을 입력
#                 break

    
#     ky = int(input('검색할 값을 입력하세요.: '))  #검색할 키 값 ky를 입력

#     idx = bin_search(x, ky)                     #ky 값과 같은 원소를 x에서 검색

# if idx == -1:
#     print('검색값을 갖는 원소가 존재하지 않습니다.')
# else:
#    print(f'검색값은 x[{idx}]에 있습니다.')







# 이진 검색 알고리즘의 실행 과정을 출력

# from typing import Any, Sequence

# def bin_search(a: Sequence, key: Any) -> int:
#     """시퀀스 a에서 key와 일치하는 원소를 이진 검색(실행 과정을 출력)"""
#     pl = 0                      #검색 범위 맨 앞 원소의 인덱스
#     pr = len(a) - 1             #검색 범위 맨 끝 원소의 인덱스

#     print('   |', end='')
#     for i in range(len(a)):
#         print(f'{i : 4}', end='')
#     print()
#     print('---+' + (4*len(a)+2)*'-')

#     while True:
#         pc = (pl + pr) // 2     #중앙 원소의 인덱스

#         print('   |', end='')
#         if pl != pc:            #pl 원소 위에 <-를 출력
#             print((pl*4+1)*' ' + '<-' + ((pc - pl) * 4) * ' ' + '+', end='')
#         else:
#             print((pc*4+1)*' ' + '<+', end='')
#         if pc != pr:            #pr 원소 위에 ->를 출력
#             print(((pr - pc) * 4 - 2) * ' ' + '->')
#         else:
#             print('->')
#         print(f'{pc:3}|', end='')
#         for i in range(len(a)):
#             print(f'{a[i]:4}', end='')
#         print('\n   |')
    
#         if a[pc] == key:
#             return pc           #검색 성공
#         elif a[pc] < key:
#             pl = pc + 1         #검색 범위를 뒤쪽 절반으로 좁힘
#         else:
#             pr = pc - 1         #검색 범위를 앞쪽 절반으로 좁힘
#         if pl > pr:
#             break
#         return -1                   #검색 실패


# if __name__ == '__main__':
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num                            #원소 수가 num인 배열을 생성

#     print('배열 데이터을 오름차순으로 입력하세요.')

#     x[0] = int(input('x[0]: '))

#     for i in range(1, num):
#         while True:
#             x[i] = int(input(f'x[{i}]: '))
#             if x[i] >= x[i-1]:                  #바로 직전에 입력한 원솟값보다 큰 값을 입력
#                 break

    
#     ky = int(input('검색할 값을 입력하세요.: '))  #검색할 키 값 ky를 입력

#     idx = bin_search(x, ky)                     #ky 값과 같은 원소를 x에서 검색

# if idx == -1:
#     print('검색값을 갖는 원소가 존재하지 않습니다.')
# else:
#    print(f'검색값은 x[{idx}]에 있습니다.')





# 체인법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """해시를 구성하는 노드"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """초기화"""
        self.key = key              # 키
        self.value = value          # 값
        self.next = next            # 뒤쪽 노드를 참조

class ChainedHash:
    """체인법으로 해시 클래스 구현"""

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity                # 해시 테이블의 크기를 지정
        self.table = [None] * self.capacity     # 해시 테이블(리스트)을 선언

    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(),16) % self.capacity)

    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key)         # 검색하는 키의 해시값
        p = self.table[hash]                # 노드를 주목

        while p is not None:
            if p.key == key:
                return p.value              # 검색 성공
            p = p.next                      # 뒤쪽 노드를 주목

        return None                         # 검색 실패

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        hash = self.hash_value(key)         # 추가하는 key의 해시값
        p = self.table[hash]                # 노드를 주목

        while p is not None:
            if p.key == key:
                return False                # 추가 실패
            p = p.next                      # 뒤쪽 노드를 주목

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp             # 노드를 추가
        return True                         # 추가 성공
    
    def remove(self, key: Any) -> bool:
        """키가 key인 원소를 삭제"""
        hash = self.hash_value(key)         # 삭제할 key의 해시값
        p = self.table[hash]                # 노드를 주목
        pp = None                           # 바로 앞의 노드를 주목

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True                 # key 삭제 성공
            pp = p
            pp = p.next                     # 뒤쪽노드를 주목
        return False                        # 삭제 실패(key가 존재하지 않음)

    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'   -> {p.key} ({p.value})', end='')
                p = p.next
            print()







# 체인법을 구현하는 해시 클래스 ChainedHash의 사용

from enum import Enum

Menu = Enum('Menu',['추가', '삭제', '검색', '덤프', '종료'])    # 메뉴를 선언

def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, seq = '  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)


hash = ChainedHash(13)              # 크기가 13인 해시 테이블을 생성

while True:
    menu = select_menu()            # 메뉴 선택

    if menu == Menu.추가:            # 추가
        key = int(input('추가할 키를 입력하세요.: '))
        val = input('추가할 값을 입력하세요.: ')
        if not hash.add(key, val):
            print('추가를 실패했습니다!')
    
    elif menu == Menu.삭제:          # 삭제
        key = int(input('삭제할 키를 입력하세요.: '))
        if not hash.remove(key):
            print('삭제를 실패했습니다!')
    
    elif menu == Menu.검색:          # 검색
        key = int(input('검색할 키를 입력하세요.: '))
        t = hash.search(key)
        if t is not None:
            print(f'검색한 키를 갖는 값은 {t}입니다.')
        else:
            print('검색할 데이터가 없습니다.')
    
    elif menu == Menu.덤프:          # 덤프
        hash.dump()
    
    else:                            # 종료
        break