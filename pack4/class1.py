'''
Created on 2016. 10. 25.

class
'''
class TestClass: #클래스 이름은 대문자로 시작
    aa = 1 #멤버 변수 -- proto type
    def __init__(self):
        print('생성자')
    def __del__(self):
        print('소멸자') #자바엔 없고 c에만 있음. 사용하던 메모리 해제 자바는 가비지 콜렉터가 있음. 소멸자 필요 없.
        #접근 지정자 없고 무조건 public.
        #콜백 
    def printMessage(self):
        name='한국인' #지역변수
        print(name)
        print(self.aa)
        
        
TestClass() #생성자 호출
print(TestClass.aa)
print(TestClass)
#TestClass.printMessage()
Test = TestClass()
print(Test.aa)
print(id(Test))
print(Test)
print('*'*20)
Test.printMessage( ) #bound method call
TestClass.printMessage(Test) #unbound method call
print('*'*20)

print(isinstance(Test, TestClass))
print(type(1))
print(type(Test))
print('종료')
        
        
 