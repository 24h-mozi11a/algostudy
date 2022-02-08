### Webex Python 08 OOP part1

pokemon 폴더에 Pikatchu.py 생성

pokemon 폴더에 wiki 폴더 생성

wiki 폴더에 Pokemon.py 생성



``` python
@Pokemon.py

class Pokemon:
    info = '푸키먼'
    population = 0

    #새 포켓몬이 태어난다면
    def __init__(self, name, lv=0):
        self.name = name 
        self.lv = lv +1
        self.skill = '몸통박치기'
        self.info = Pokemon.info + '피카츄'
     
    def attack(self):
        return self.skill

pika = Pokemon('피카츄',5)
print(pika.lv, pika.name, pika.info) #6 피카츄 푸키먼피카츄
print(Pokemon.info) #푸키먼
print(pika.attack()) #몸통박치기

meta = Pokemon('메타몽')
print(meta.lv, meta.name, meta.info) #1 메타몽 푸키먼피카츄
print(meta.attack()) #몸통박치기

# 메타몽한테도 피카츄가 나오는데 그렇게 하고 싶지 않고 개별 값을 주고싶다면?
# 몸통박치기 말고 개별 스킬을 주고싶다면?
# 상속 이용
```



### @classmethod 데코레이터를 이용해 인구 증가시키기

``` python
class Pokemon:
    info = '푸키먼'
    population = 0

    #새 포켓몬이 태어난다면
    def __init__(self, name, lv=0):
        self.name = name 
        self.lv = lv +1
        self.skill = '몸통박치기'
        self.increase()

    #classmethod를 이용해 population을 1씩 증가
    @classmethod
    def increase(cls):
        cls.population += 1
        
if __name__ == '__main__'
	pika = Pokemon('피카츄',5)
	print(pika.lv, pika.name, pika.info) #6 피카츄 푸키먼
	print(Pokemon.population) #1

	meta = Pokemon('메타몽')
	print(meta.lv, meta.name, meta.info) #1 메타몽 푸키먼
	print(Pokemon.population) #2
```



### wiki 폴더 밖의 Picktchu에서 Pokemon을 상속받자

``` python
@Pikatchu.py

from wiki.pokemon import Pokemon

class Pikatchu(Pokemon):
    no = 25

    def __init__(self, name, lv=5):
        #상위 class와 중복되는 값 가져오기
        super().__init__(name, lv)
        self.skill = '전기 충격'

pika = Pikatchu('피카츄')
print(pika.name, pika.lv, pika.skill) 
#피카츄 6 전기 충격
# Pokemon 클래스에서 self.lv = lv + 1 값 가져옴
```

``` python
def __init__(self, name, lv=5):
        #상위 class와 중복되는 값 가져오기
        self.skill = '전기 충격'
        super().__init__(name, lv)
        
#super값과 위치가 바뀐다면?      
#피카츄 6 몸통박치기
#오버라이드 시 순서 주의하기       
```



### 피카츄의 .attack()을 바꿔보자

``` python
from wiki.pokemon import Pokemon

class Pikatchu(Pokemon):
    no = 25

    def __init__(self, name, lv=5):
        #상위 class와 중복되는 값 가져오기
        super().__init__(name, lv)
        self.skill = '전기 충격'

    def attack(self):
        return '찌릿 찌릿'
    
    def walk(self):
        return '뚜벅 뚜벅'

pika = Pikatchu('피카츄')
print(pika.name, pika.lv, pika.skill, pika.attack(), pika.walk()) 
피카츄 6 전기 충격 찌릿 찌릿 뚜벅 뚜벅
# Pokemon 클래스에서 self.lv = lv + 1 값 가져옴

print(pika.no)
25
```



### 메타몽도 고유 skill을 가지고 싶어!

``` python
from wiki.pokemon import Pokemon

class Pikatchu(Pokemon):
    no = 25

    def __init__(self, name, lv=5):
        #상위 class와 중복되는 값 가져오기
        super().__init__(name, lv)
        self.skill = '전기 충격'

    def attack(self):
        return '찌릿 찌릿'
    
    def walk(self):
        return '뚜벅 뚜벅'



class Metamong(Pokemon):
    no = 132  

    def __init__(self, name, lv = 5):
        super().__init__(name, lv)
        self.skill = '변신' 

    def eat(self):
        return '냠냠'    

pika = Pikatchu('피카츄')
print(pika.name, pika.lv, pika.skill, pika.attack(), pika.walk()) 
# 피카츄 6 전기 충격 찌릿 찌릿
# Pokemon 클래스에서 self.lv = lv + 1 값 가져옴

meta = Metamong('메타몽')
print(meta.no, meta.attack())
#132 변신
```



### class Child(Pikatchu, Metamong) : [다중상속] 피카츄와 메타몽이 자식을 낳았다!

``` python
from pickle import PickleBuffer
from wiki.pokemon import Pokemon

class Pikatchu(Pokemon):
    no = 25

    def __init__(self, name, lv=5):
        #상위 class와 중복되는 값 가져오기
        super().__init__(name, lv)
        self.skill = '전기 충격'

    #class의 .attack()은 self.skill
    #피카츄가 오버라이드 하는 중
    def attack(self):
        return '찌릿 찌릿'
    
    def walk(self):
        return '뚜벅 뚜벅'



class Metamong(Pokemon):
    no = 132  

    def __init__(self, name, lv = 5):
        super().__init__(name, lv)
        self.skill = '변신' 

    def eat(self):
        return '냠냠'    

class Child(Pikatchu, Metamong):
    pass

class Brother(Metamong, Pikatchu):
    pass

c = Child('피카츄애기')
print(c.no) #25 #피카츄 번호
print(c.eat())#냠냠 #메타몽 냠냠

b = Brother('메타몽애기')
print(b.no) #132 #메타몽 번호
print(b.eat())#냠냠 #메타몽 냠냠

#그런데.....
print(b.attack(), b.skill) #찌릿 찌릿 변신

#메타몽의 attack()은 정의된 적이 없으니 Pokemon의 attack()인 skill 명이 반환되어야 하는 것 아닌가..?
#왜 '변신 변신'이 아니지..?
#우선순위는 앞에 오는게 빠르다면서요...
#메타몽과 피카츄의 attack()을 살펴보자 
#피카츄는 오버라이드를 통해 attack을 변형, 우선순위가 더 높아짐
```



