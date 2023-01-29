from tinydb import TinyDB, Query
import time
game_file = TinyDB('data/game_file.json')
App = Query()
import sys,time,random
from os import system, name
from colorama import Fore, Back, Style


monster_data_one = TinyDB('data/monster_data_lvl_one.json')
monster_data_two = TinyDB('data/monster_data_lvl_two.json')











def kill_player(monster_name, monster_health, player_health, xp_health, results):
  if player_health <=0:
    print("You have been killed!")
    
  else:
    dealing_damage = random.randint(1,6)
    player_health = player_health - dealing_damage
    print(Fore.RED)
    print(f"The {monster_name} has done {dealing_damage} damage to you. You have {player_health} health left.")
    print(Style.RESET_ALL)
    time.sleep(1)
    if player_health <= 0:
      print(Fore.RED)
      print("You have died")
      print(Style.RESET_ALL)
      xp_given = results[0]['xp'] - 5
      game_file.update({'xp': xp_given}, App.pin == results[0]['key'])
      print(Fore.RED)
      print(f"You have lost {xp_given} XP")
      print(Style.RESET_ALL)
      input("| ENTER TO CONTINUE |")
      clear()
    else:
      kill_monster(monster_name, monster_health, player_health, xp_health, results)
      
    


def kill_monster(monster_name, monster_health, player_health, xp_health, results):
  if monster_health <=0:
    print(f"The {monster_name} has been killed!")
    
  else:
    dealing_damage = random.randint(1,6)
    monster_health = monster_health - dealing_damage
    print(Fore.GREEN)
    print(f"You have done {dealing_damage} damage to the {monster_name}. It has {monster_health} health left.")
    print(Style.RESET_ALL)
    time.sleep(1)
    if monster_health <= 0:
      print(Fore.GREEN)
      print(f"The {monster_name} has died!")
      print(Style.RESET_ALL)
      xp_given = xp_health * 0.5 + results[0]['xp']
      game_file.update({'xp': xp_given}, App.key == results[0]['key'])
      print(Fore.GREEN)
      print(f"You now have {xp_given} XP")
      print(Style.RESET_ALL)
      
      input("| ENTER TO CONTINUE |")
      clear()
    else:
      kill_player(monster_name, monster_health, player_health, xp_health, results)
      
  
  
def healing(max_player_health, player_health):
  if player_health != max_player_health:
    time.sleep(5)
    player_health = player_health + 2
    new_health = player_health
    print(f"You have healed 2 JP. HP: {new_health} HP")
    if player_health != max_player_health:
        healing(max_player_health, new_health)
    else:
        return new_health


def type(t, typing_speed):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    









knight = 1
mage = 2
thief = 3

def main(game_code):
  results = game_file.search(App.key == game_code)
  strength = results[0]['strength']
  dexterity = results[0]['dexterity']
  intelligence = results[0]['intelligence']
  wisdom = results[0]['wisdom']
  level = results[0]['level']
  xp = results[0]['xp']
  print(f"| STATS |\n Strength: {strength}\n Dexterity: {dexterity}\n Intelligence: {intelligence}\n Wisdom: {wisdom}\n XP: {xp}")
  input("| ENTER TO CONTINUE |")


  def check1():
    print("What would you like to do?")
    print("1. Fight")
    print("2. Explore")
    print("3. Shop")


  
  #print(type("In a realm called Aurielia, magic flowed freely and mythical beasts roamed the land. The kingdom was ruled by a mighty wizard queen, who held the power to control the elements with her command. But a great darkness began to spread throughout the land, as an ancient evil, long sealed away, started to regain its strength and threatens to engulf the kingdom in chaos. As a brave adventurer, you have been called upon to gather a group of warriors and embark on a perilous journey to defeat this darkness and restore peace to Aurielia.", 200))
  
  input("| ENTER TO CONTINUE |")
  clear()
  check1()


  check1sel = int(input(""))

  if check1sel == 1:
    # ------------------------------------ START MONSTER FIGHT ---------------------------------------------
    print("You chose to fight!")
    time.sleep(1)
    clear()
    
    if level == 1:
      monster = monster_data_one
      monster_list = ['Goblin', 'Skeleton', 'Zombie', 'Gravemonster']

    elif level == 2:
      monster = monster_data_two
      
    
    clear()
    choice = random.sample(monster_list, 1)
    choice_a = str(choice)[2:-2]

    results = monster.search(App.name == choice_a)
    monster_name = results[0]['name']
    print(f"You are going against a {monster_name}!")
    strength = results[0]['strength']
    dexterity = results[0]['dexterity']
    intelligence = results[0]['intelligence']
    wisdom = results[0]['wisdom']
    health = results[0]['health']


    
    print(f"| {monster_name} STATS |\n Strength: {strength}\n Dexterity: {dexterity}\n Intelligence: {intelligence}\n Wisdom: {wisdom}\n Health: {health}")
    input("| ENTER TO CONTINUE |")
    clear()

    results = game_file.search(App.key == game_code)
    kill_monster(monster_name, health, results[0]['health'], results[0]['health'], results)
    #------------------------------------------------------------ END FIGHT ----------------------------------------
    clear()
    check1()

    
    
    # ---------------------------------------------------- START EXPLORING --------------------------------------------
  elif check1sel == 2:
    print("You chose to explore!")

    # ----------------------------------------------------- END EXPLORING ------------------------------------------------
    # ------------------------------------------------------ START SHOP ------------------------------------------------
  elif check1sel == 3:
    print("Welcome to the shop :)")
    # ----------------------------------------------------------- END SHOP ----------------------------------------------

  else: 
    check1()



