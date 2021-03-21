#-----------------------------Test import chicken------------------------------
'''
class Chicken():
    def __init__(self,name,bp,hunger,state):
        self.Name = name
        self.BP = bp
        self.Hunger = hunger
        self.State = state
    def show_2(self):
        print('行動值:',chicken.BP,'飽食度:',chicken.Hunger,'心情:',chicken.State,end = '')
        input(':')
chicken = Chicken('肯德雞',30,50,40)'''
#-----------------------------------倉庫----------------------------------------

class Bag():        #####倉庫類別#####
    def __init__(self,money,diamond,food,cake,cookies,hamburger):
        self.Money = money           #金幣
        self.Diamond = diamond       #鑽石
        self.Food = food             #雞飼料
        self.Cake = cake             #蛋糕
        self.Cookies = cookies       #餅乾
        self.Hamburger = hamburger   #特大麥香雞
    
    def show(self):     #列出資源
        print('金幣:',chicken_bag.Money,'鑽石:',chicken_bag.Diamond,'有機雞飼料:',chicken_bag.Food,'生乳酪蛋糕:',chicken_bag.Cake,'餅乾:',chicken_bag.Cookies,'特大麥香雞',chicken_bag.Hamburger)

#-------------------------------##增減##函式--------------------------------------

    def add_money(self,add):
        self.Money = self.Money + add
    
    def add_diamond(self,add):
        self.Diamond = self.Diamond + add

    def add_food(self,add):
        self.Food = self.Food + add

    def add_cake(self,add):
        self.Cake = self.Cake + add

    def add_cookies(self,add):
        self.Cookies = self.Cookies + add

    def add_hamburger(self,add):
        self.Hamburger = self.Hamburger + add
#--------------------------------##進食##函式---------------------------------------
    def Eat(self,_id,Chicken):
        if _id == 1:
            Chicken._BP(5)      #能力值增加
            Chicken._Hunger(5)
            self.add_food(-1)    #食物減少
            print(Chicken._Name,'吃了有機雞飼料 ! ! ',end = '')
            input(':')
            print('')
            print(Chicken._Name,'的行動值增加 5 ,飽食度增加 5 ',end = '')
            input(':')
        if _id == 2:
            Chicken._BP(3)
            Chicken._Hunger(30)
            Chicken._State(15)
            self.add_cake(-1)
            print(Chicken.Name,'一臉滿足的吃下了生乳酪蛋糕 ',end = '')
            input(':')
            print('')
            print(Chicken.Name,'的行動值增加 3 ,飽食度增加 30 ,心情增加 15 ',end = '')
            input(':')
        if _id == 3:
            Chicken._BP(10)
            Chicken._Hunger(15)
            self.add_cookies(-1)
            print('喀滋喀滋...',Chicken.Name,'優雅的吃完餅乾了 ',end = '')
            input(':')
            print('')
            print(Chicken.Name,'的行動值增加 10 ,飽食度增加 15 ',end = '')
            input(':')
        if _id == 4:
            Chicken._BP(50)
            Chicken._Hunger(50)
            Chicken._State(40)
            self.add_hamburger(-1)
            print('吧唧吧唧...',Chicken.Name,'含著眼淚吃完了特大麥香雞... ',end = '')
            input(':')
            print('')
            print(Chicken.Name,'的行動值增加 50 ,飽食度增加 50 ,心情減少 40 ',end = '')
            input(':')
  
chicken_bag = Bag(100,5,10,10,10,19)    #倉庫初始值          

#------------------------------------商店--------------------------------------------

class Shop():   #####商店類別#####
    def __init__(self,food_money,cake_money,cookies_money,hamburger_money):
        self.Food_money = food_money
        self.Cake_money = cake_money
        self.Cookies_money = cookies_money
        self.Hamburger_money = hamburger_money
#--------------------------------##購物##函式---------------------------------------
    def Buy(self,Chicken):
        chicken_bag.show()      #購物前資源
        while True:
            print('--------------------------------------------------------------------------------')
            print('這位勇敢的',Chicken._Name,'你想買些什麼東西呢 ?')
            print('')
            print(' 1. 有機雞飼料 :',shop.Food_money,'金幣/袋')
            print('')
            print(' 2. 生乳酪蛋糕 :',shop.Cake_money,'金幣/塊')
            print('')
            print(' 3. 鴨子造型餅乾 :',shop.Cookies_money,'金幣/包')
            print('')
            print(' 4. 特大麥香雞 :',shop.Hamburger_money,'金幣/個')
            print('')
            shop_id = int(input('請輸入想買的物品編號 : '))
            print('')
            num_id = int(input('請輸入購買的個數 : '))
            print('')
        
            if shop_id == 1:
                chicken_bag.add_money( (-1) * (num_id) * (shop.Food_money) )        #減少自身金幣
                chicken_bag.add_food( (num_id) * 1)                                 #購買物品增加至倉庫
                print('獲得了',num_id,'個有機雞飼料 ! ! ',end = '')                
                input(':')
                print('--------------------------------------------------------------------------------')
                chicken_bag.show()            
            if shop_id == 2:
                chicken_bag.add_money( (-1) * (num_id) * (shop.Cake_money) )
                chicken_bag.add_cake( (num_id) * 1)
                print('獲得了',num_id,'個生乳酪蛋糕 ! ! ',end = '')
                input(':')
                print('--------------------------------------------------------------------------------')
                chicken_bag.show()
            if shop_id == 3:
                chicken_bag.add_money( (-1) * (num_id) * (shop.Cookies_money) )
                chicken_bag.add_cookies( (num_id) * 1)
                print('獲得了',num_id,'個鴨子造型餅乾 ! ! ',end = '')
                input(':')
                print('--------------------------------------------------------------------------------')
                chicken_bag.show()
            if shop_id == 4:
                chicken_bag.add_money( (-1) * (num_id) * (shop.Hamburger_money) )
                chicken_bag.add_hamburger( (num_id) * 1)
                print('獲得了',num_id,'個特大麥香雞 ! ! ',end = '')
                input(':')
                print('--------------------------------------------------------------------------------')
                chicken_bag.show()  #購物後資源                     
            if shop_id == 777:
                break
            

shop = Shop(5,30,15,50)     #商品價格
            
#------------------------------------Test--------------------------------------
#chicken_bag.Eat(4)
#shop.Buy()

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
'''
