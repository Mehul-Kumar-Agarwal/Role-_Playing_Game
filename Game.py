import random
from .Magic import Spell
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class Person:
    def __init__(self,name,hp,mp,atk,df,magic,items):
        self.name = name
        self.max_hp=hp
        self.hp=hp
        self.max_mp=mp
        self.mp =mp
        self.atkl =atk-10
        self.atkh=atk+10
        self.df=df
        self.magic=magic
        self.items=items
        self.action=["Attack","Magic","Items"]
    def generate_dmg(self):
        return random.randrange(self.atkl,self.atkh)

    def takenDmg(self,dmg):
        self.hp -= dmg
        if self.hp<0:
            self.hp = 0
        return self.hp

    def heal(self,dmg):
        self.hp += dmg
        if self.hp>self.max_hp:
            self.hp = self.max_hp
        return self.hp

    def get_Hp(self):
        return self.hp

    def get_MaxHp(self):
        return self.max_hp

    def get_Mp(self):
        return self.mp

    def get_MaxHp(self):
        return self.max_mp

    def reduce_Mp(self,cost):
        self.mp-=cost

    def choose_Action(self):
        i = 1
        print("\n"+bcolors.BOLD+bcolors.OKGREEN+self.name+bcolors.ENDC+"\nACTIONS")
        for item in self.action:
            print("      ",str(i) + ":" + item)
            i += 1

    def choose_Magic(self):
        i = 1
        print("         MAGIC")
        for spell in self.magic:
            print("      ",str(i) + ":" + spell.name, "(Cost:", str(spell.cost) + ")")
            i += 1

    def choose_Item(self):
        i=1;
        print("         ITEMS")
        for item in self.items:
            print("      ",str(i)+":",item["item"].name+":",item["item"].description,"(Quantity is "+str(item["quantity"])+")")
            i+=1
    def choose_Target(self,enemies):
        i=1
        print("    Target")
        for enemy in enemies:
            if enemy.get_Hp()!=0:
                print("         "+str(i)+"."+enemy.name)
                i+=1
        ch=int(input("          Choose Target"))-1
        return ch



    def get_Enemy_Stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.max_hp) * 100 / 2
        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        while len(hp_bar) < 50:
            hp_bar += " "
        hp_str=str(self.hp)+"/"+str(self.max_hp)
        curhp=""
        if len(hp_str)<11:
            dec=11-len(hp_str)

            while dec>0:
                curhp+=" "
                dec-=1;
            curhp+=hp_str
        else:
            curhp=hp_str

        print("                              __________________________________________________")
        print(bcolors.BOLD + self.name + "           " + curhp + "|" +
              bcolors.FAIL + hp_bar + bcolors.ENDC+"|")

    def get_Stats(self):

        hp_bar=""
        bar_ticks=(self.hp/self.max_hp)*100/4
        # assume max hit point as 200...hit point as 50...divide 50/200=0.25..then 0.25*100=25 and then 25/4=6.25 means we need to add 6 blocks
        mp_bar=""
        mp_ticks=(self.mp/self.max_mp)*100/10


        while bar_ticks>0:
            hp_bar+="█"
            bar_ticks-=1
        while len(hp_bar)<25:
            hp_bar+=" "

        while mp_ticks>0:
            mp_bar+="█"
            mp_ticks-=1
        while len(mp_bar)<10:
            mp_bar+=" "

        hp_str=str(self.hp)+"/"+str(self.max_hp)
        curhp=""
        if len(hp_str)<9:
            dec=9-len(hp_str)

            while dec>0:
                curhp+=" "
                dec-=1;
            curhp+=hp_str
        else:
            curhp=hp_str


        mp_str=str(self.mp)+"/"+str(self.max_mp)
        curmp=""
        if len(mp_str)<7:
            dec=7-len(mp_str)

            while dec>0:
                curmp+=" "
                dec-=1;
            curmp+=mp_str
        else:
            curmp=mp_str

        print("                            _________________________               ____________")
        print(bcolors.BOLD + self.name+"           " +curhp+"|" +
              bcolors.OKGREEN +hp_bar+ bcolors.ENDC +
              bcolors.BOLD + "|      "+curmp+" |" + bcolors.OKBLUE +mp_bar+ bcolors.ENDC + "|")
    def choose_Enemy_Spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_Dmg()
        percent=self.hp/self.max_hp*100

        if self.mp < spell.cost or spell.type=="White" and percent>50 :
            self.choose_Enemy_Spell()
        else:
            return spell,magic_dmg

'''The below 2 fuctions are deleted
    def get_Spellname(self,i):
        return self.magic[i]["name"]

    def get_SpellMpcost(self, i):
        return self.magic[i]["cost"]
        
    def generate_SpellDmg(self,i):
        mgl=self.magic[i]["dmg"]-5
        mgh=self.magic[i]["dmg"]+5
        return random.randrange(mgl,mgh)
    
'''


