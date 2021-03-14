#野怪
class Mons():
    def __init__(self,name,level,atk,_def):
        self.Name = name
        self.Level = level
        self.Hp = level*10
        self.Atk = atk
        self.Def = _def
    def attribute(self):
        print (self.Name +'的屬性:','等級:',self.Level,'攻擊:',self.Atk ,'防禦:',self.Def)
def show(mons_n):
    print(mons_n.attribute())
#-------------新增野怪區--------------------------------------------------------
mons_1 = Mons('法式烤雞',10,18,30)
mons_2 = Mons('阿雞米德',20,50,50)
#-------------------------------------------------------------------------------
   
mons_1.attribute()#列印屬性
show(mons_2)


