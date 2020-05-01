'''
This is the main file of python
magic is array containning various kinds of spells to attack
'''
from Classes.Game import Person,bcolors
from Classes.Magic import Spell
from Classes.Inventory import Items
import random


#Creating Black Magic
Fire=Spell("Fire",25,600,"Black")
Thunder=Spell("Thunder",30,550,"Black")
Blizzard=Spell("Blizzard",45,780,"Black")
Meteor=Spell("Meteor",60,900,"Black")
Quack=Spell("Quack",70,550,"Black")

#Creating White Magic
Cure=Spell("Cure",30,500,"White")
Cura=Spell("Cura",45,750,"White")
Curene=Spell("Curene",50,5000,"White")

#Creating Some Items
Potion=Items("Potion","Potion","Heals about 50 hp",100)
Hipotion=Items("Hipotion","Hipotion","Heals 100 hp",500)
Superpotion=Items("Superpotion","Superpotion","Heals 500hp",1000)
Grenade=Items("Grenade","Attack","Deals 500 Dmg",500)

enemy_magic=[Fire,Meteor,Cure]
player_magic=[Fire,Thunder,Blizzard,Meteor,Cure,Cura]
player_item=[{"item":Potion,"quantity":15},{"item":Hipotion,"quantity":5},
             {"item":Superpotion,"quantity":5},{"item":Grenade,"quantity":5}]

player1=Person("Mehul  ",4160,140,300,34,player_magic,player_item)
player2=Person("Mukesh ",3090,177,325,34,player_magic,player_item)
player3=Person("Agarwal",1100,120,280,34,player_magic,player_item)

enemy1=Person("Kumar ",11000,205,520,34,enemy_magic,[])
enemy2=Person("Thanos",1300,130,560,324,enemy_magic,[])
enemy3=Person("Rocket",1300,205,560,324,enemy_magic,[])

players=[player1,player2,player3]
enemies=[enemy1,enemy2,enemy3]
running=True
i=0
print(bcolors.BOLD+ bcolors.FAIL+ "ENEMY ATTACKS"+ bcolors.ENDC) #GIves different styles to the text

while running:
       print("================================================================")
       print("\n\n")
       print("Name                           HP                                   MP")
       for player in players:
              player.get_Stats()
       print("\n")
       for enemy in enemies:
              enemy.get_Enemy_Stats()
       for player in players:

              player.choose_Action()
              choice =int(input("Enter your Action "))
              index = int(choice)-1
              # as the index starts from 0 and we gave the values from 1 to get it correct we need to change vlue and reduce by 1

              # The Enemy is being attacked in the below code
              if index == 0:
                     dmg = player.generate_dmg()
                     enemy=player.choose_Target(enemies)
                     enemies[enemy].takenDmg(dmg)  # enemy takes the damage
                     print("You have Attacked "+enemies[enemy].name+" for "+str(dmg))
                     if enemies[enemy].get_Hp()==0:
                            print("Enemy"+enemies[enemy].name.name.replace(" ","")+" is dead")
                            del enemies[enemy]

              # We have the magic code here
              elif index == 1:
                     player.choose_Magic()
                     magic_choice = int(input("Enter the Magic u want: ")) - 1
                     '''
                     magic_dmg=player.generate_SpellDmg(magic_choice)
                     spell=player.get_Spellname(magic_choice)
                     cost=player.get_SpellMpcost(magic_choice)
                     '''
                     if magic_choice == -1:
                            continue
                     spell = player.magic[magic_choice]
                     magic_dmg = spell.generate_Dmg()
                     current_mp = player.get_Mp()
                     if spell.cost > current_mp:
                            print(bcolors.FAIL + "\nYou dont have enough MP\n" + bcolors.ENDC)
                            continue
                     player.reduce_Mp(spell.cost)

                     if spell.type == "White":
                            player.heal(magic_dmg)
                            print(bcolors.OKBLUE + "Player used ", spell.name + " and heals for ",
                                  str(magic_dmg) + bcolors.ENDC)
                     elif spell.type == "Black":
                            enemy = player.choose_Target(enemies)
                            enemies[enemy].takenDmg(dmg)

                            print(bcolors.OKBLUE + "\n" + spell.name + " deals " + str(magic_dmg) + bcolors.ENDC+"to"+enemies[enemy].name)
                            if enemies[enemy].get_Hp() == 0:
                                   print("Enemy" + enemies[enemy].name.name.replace(" ","")+ " is dead")
                                   del enemies[enemy]
              # We have Items Code
              elif index == 2:
                     player.choose_Item()
                     item_choice = int(input("Choose and item ")) - 1
                     if item_choice == -1:
                            continue
                     item = player.items[item_choice]["item"]

                     if player.items[item_choice]["quantity"] == 0:  # Quantity ==0
                            print(bcolors.FAIL + "Item Quantity=0 Choose `Another" + bcolors.ENDC)
                            continue
                     player.items[item_choice]["quantity"] -= 1  # Quantity of item will be modified here.

                     if item.type == "Potion":
                            player.heal(item.prop)
                            print("Player is healed for" + str(item.prop))
                     elif item.type == "Attack":
                            enemy = player.choose_Target(enemies)
                            enemies[enemy].takenDmg(item.prop)

                            print("Enemy"+enemies[enemy].name+" is attacked for " + str(item.prop) + "points")
                            if enemies[enemy].get_Hp() == 0:
                                   print("Enemy" + enemies[enemy].name.replace(" ","") + " is dead")
                                   del enemies[enemy]

#checks if all the enemies are defeated
       defeat_player = 0
       defeat_enemy = 0
       for enemy in enemies:
              if enemy.get_Hp() == 0:
                     defeat_enemy += 1
#checks isfplayer has won the battle
       if defeat_enemy == 2:
              print(bcolors.OKGREEN + "YOU WIN" + bcolors.ENDC)
              running = False
#checks if player has lost the battle
       else:
              for player in players:
                     if player.get_Hp() == 0:
                            defeat_player += 1
                     if defeat_player == 2:
                            print(bcolors.FAIL + "YOU LOOSE" + bcolors.ENDC)
                            running = False
       print("\n")
#if enemies are still alive they are attacked from the below code
       for enemy in enemies:
              enemy_choice = random.randrange(0, 2)
              if enemy_choice==0:

                     tar=random.randrange(0,3)
                     enemy_dmg=enemies[0].generate_dmg()

                     players[tar].takenDmg(enemy_dmg)    #player takes the damage
                     print("Enemy attacks for"+str(enemy_dmg))
              elif enemy_choice==1:
                     spell,magic_dmg=enemy.choose_Enemy_Spell()
                     enemy.reduce_Mp(spell.cost)
                     if spell.type == "White":
                            enemy.heal(magic_dmg)
                            print(bcolors.OKBLUE +spell.name+"heals" +enemy.name+ "for ",
                                  str(magic_dmg) + bcolors.ENDC)
                     elif spell.type == "Black":
                            tar = random.randrange(0, 3)
                          #  enemy = enemy.choose_Target(enemies)
                            players[tar].takenDmg(magic_dmg)

                            print(bcolors.OKBLUE + "\n" + enemy.name.replace(" ","") + " deals "+spell.name+" for points "+ str(
                                   magic_dmg) +" to " + players[tar].name+bcolors.ENDC)

                            if players[tar].get_Hp() == 0:
                                   print("Player" + players[tar].name.replace(" ", "") + " is dead")
                                   del players[player]
                     #print("Enemy chose "+spell+" Damage is "+magic_dmg)



'''
player_magic=[{"name":"Fire","cost":10,"dmg":100},
       {"name":"Thunder","cost":10,"dmg":120},
       {"name":"Blizzard","cost":10,"dmg":130}]
'''