'''
Created on 2016. 10. 25.

사용자 정의 모듈
'''

print('사용자 정의 모듈 읽기')
import pack3.mymod1

print(dir(pack3.mymod1))
print(pack3.mymod1.__file__)
print(pack3.mymod1.__name__)
print()
print('mymod1 모듈의 멤버 읽기')
a = 10, 20, 30, 40
b= [1,2,3,4]
pack3.mymod1.dataList(a,b)
print()
if __name__ == '__main__':
    print('최상위 모듈')
    
from pack3 import mymod1
print(mymod1.myage)
mymod1.Kbs()

print()

from pack3.mymod1 import Kbs,Mbc,myage
print(myage)
Kbs()
Mbc()

print('\n같은 package에서 모듈 호출할 때와 동일')
from pack3.mymod2 import Hap,Cha
print(Hap(5,3))
print(Cha(5,3))

print('\n Path가 설정된 폴더의 모듈 읽기')

print('\n 전혀 다른 폴더의 모듈 읽기')
#방법1 : path에 폴더 추가 (권장)


# #방법2
# import sys
# sys.path.append(r'c:/work')
# import mymod4
# print('나누기', mymod4.Hap(5,3))

#그래픽
from turtle import *
p = Pen()
p.color('red','purple')
p.begin_fill()
while True:
    p.forward(200)
    p.left(170)
    if abs(p.pos()) <1:
       break
p.end_fill()   
    
#input()
