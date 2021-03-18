#-----------------------------Test import chicken------------------------------

class Chicken():
    def __init__(self,name,bp,hunger,state):
        self.Name = name
        self.BP = bp
        self.Hunger = hunger
        self.State = state
    def show_2(self):
        print('行動值:',chicken.BP,'飽食度:',chicken.Hunger,'心情:',chicken.State,end = '')
        input(':')
chicken = Chicken('雷抗雞',30,50,40)
#---------------------------------檢視資源-------------------------------------

class Bag():
    def __init__(self,money,diamond,food,cake,cookies,hamburger):
        self.Money = money           #金幣
        self.Diamond = diamond       #鑽石
        self.Food = food             #雞飼料
        self.Cake = cake             #蛋糕
        self.Cookies = cookies       #餅乾
        self.Hamburger = hamburger   #特大麥香雞
    
    def show(self):
        print('金幣:',chicken_bag.Money,'鑽石:',chicken_bag.Diamond,'雞飼料:',chicken_bag.Food,'蛋糕:',chicken_bag.Cake,'餅乾:',chicken_bag.Cookies,'特大麥香雞',chicken_bag.Hamburger,end = '')
        input(':')

    def add_money(add):
        self.Money = self.Money + add
    
    def add_diamond(add):
        self.Diamond = self.Diamond + add

    def add_food(self,add):
        self.Food = self.Food + add

    def add_cake(self,add):
        self.Cake = self.Cake + add

    def add_cookies(self,add):
        self.Cookies = self.Cookies + add

    def add_hamburger(self,add):
        self.Hamburger = self.Hamburger + add
#-----------------------------------進食---------------------------------------
    def Eat(self,_id):
        if _id == 1:
            chicken.BP += 5 
            chicken.Hunger += 5
            self.add_food(-1)
            print(chicken.Name,'吃了雞飼料 ! ! ',end = '')
            input(':')
            print(chicken.Name,'的行動值增加 5 ,飽食度增加 5 ',end = '')
            input(':')
        if _id == 2:
            chicken.BP += 3
            chicken.Hunger += 25
            chicken.State += 15
            self.add_cake(-1)
            print(chicken.Name,'一臉滿足的吃下了蛋糕 ',end = '')
            input(':')
            print(chicken.Name,'的行動值增加 3 ,飽食度增加 25 ,心情增加 15 ',end = '')
            input(':')
        if _id == 3:
            chicken.BP += 10
            chicken.Hunger += 15
            self.add_cookies(-1)
            print('喀滋喀滋...',chicken.Name,'優雅的吃完餅乾了 ',end = '')
            input(':')
            print(chicken.Name,'的行動值增加 10 ,飽食度增加 15 ',end = '')
            input(':')
        if _id == 4:
            chicken.BP += 50
            chicken.Hunger += 50
            chicken.State -= 40
            self.add_hamburger(-1)
            print('吧唧吧唧...',chicken.Name,'含著眼淚吃完了特大麥香雞... ',end = '')
            input(':')
            print(chicken.Name,'的行動值增加 50 ,飽食度增加 50 ,心情減少 40 ',end = '')
            input(':')
  
#chicken_bag = Bag(100,5,10,10,10,19)  #test        

#------------------------------------商店--------------------------------------

def shop(shop_id):
    print('這位勇敢的',chicken.Name,'你想買些什麼東西呢 ? ',end = (''))
    input('有機雞飼料:',)
    
    if shop_id == 1:
        print('獲得了雞飼料 ! ! ',end = '')
        input = (':')
    
            
#------------------------------------Test--------------------------------------
shop(1)

'''
chicken.show_2()
chicken_bag.show()
chicken_bag.Eat(1)
chicken.show_2()
chicken_bag.show()
chicken_bag.Eat(2)
chicken.show_2()
chicken_bag.show()
chicken_bag.Eat(3)
chicken.show_2()
chicken_bag.show()
chicken_bag.Eat(4)
chicken_bag.show()
chicken.show_2()
