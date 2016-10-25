'''
Created on 2016. 10. 25.

module: 응용프로그램의 실행단위. 자원의 재활용을 목적.
표준 모듈, 제3자 모듈, 사용자 정의 모듈


'''

print('do something')
import sys
print('모듈 경로 ' , sys. path)
#sys.exit() 응용프로그램 종료

import math
print(math.pi)
print(math.sin(math.radians(30)))
print(math.sin(math.pi/6))

import calendar
calendar.setfirstweekday(6) #일요일부터 먼저찍음.
calendar.prmonth(2016,10) #달력찍음

import random
print(random.random())
print(random.randrange(1,10))

from random import random
print(random())
from random import randrange
print(randrange(1,10))

#from random import * 권장사항 아님
print()
print('finish')