#---------------------------------外部import------------------------------------
class Chicken():
    def __init__(self,name,bp,hunger,state):
        self.Name = name
        self.Bp = bp
        self.Hunger = hunger
        self.State = state
chicken = Chicken('雷抗雞',30,50,40)

#---------------------------------檢視資源--------------------------------------
Money = 0 
Diamond = 0
Exp = 0
Point = 0
class Bag():
    def __init__(self,money,diamond,exp,point):
        self.Money = money
        self.Diamond = diamond
        self.Exp = exp
        self.Point = point
def show():
    print('金幣:',Money,'鑽石:',Diamond,'經驗值:',Exp,'屬性點數:',Point)

myself = Bag(Money,Diamond,Exp,Point)

#------------------------------------進食---------------------------------------
def Eat(_id):
    if _id == 1:
        chicken.Bp = chicken.Bp + 5 
        chicken.Hunger = chicken.Hunger + 5
        print(chicken.Name,'吃了雞飼料 ! !')
        print(chicken.Name,'的行動值增加5,飽食度增加5')
    if _id == 2:
        chicken.Bp = chicken.Bp + 3
        chicken.Hunger = chicken.Hunger + 25
        chicken.State = chicken.State + 15
        print(chicken.Name,'一臉滿足的吃下了蛋糕')
        print(chicken.Name,'的行動值增加 3 ,飽食度增加 25 ,心情增加 15 ')
    if _id == 3:
        chicken.Bp = chicken.Bp + 10
        chicken.Hunger = chicken.Hunger + 15
        print('喀滋喀滋...',chicken.Name,'優雅的吃完餅乾了')
        print(chicken.Name,'的行動值增加 10 ,飽食度增加 15')
        
        
#---------------------金幣#鑽石#經驗值#屬性點數(增減函式)-----------------------

def add_money(add):
    global Money
    Money = Money + add
    
def add_diamond(add):
    global Diamond
    Diamond = Diamond + add
     
def add_exp(add):
    global Exp
    Exp = Exp + add
 
def add_point(add):
    global Point
    Point = Point + add
    
#-------------------------------------Test--------------------------------------
Eat(1)
Eat(2)
Eat(3)
'''#-------------初始值----------------
print('初始值')
print()
show()
#--------------增加-----------------
add_money(200)
add_diamond(5)
add_exp(20)
add_point(7)
#--------------減少-----------------
add_money(-50)
add_diamond(-2)
add_point(-2)
print()
#--------------結果-----------------
print('結果')
print()
show()
#-------------------------------------main--------------------------------------
print('~~雷抗雞的倉庫~~~')
print()
show()'''



















