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

#-------------初始值----------------
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



