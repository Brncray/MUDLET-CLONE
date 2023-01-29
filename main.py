from tinydb import TinyDB, Query
import time
game_file = TinyDB('data/game_file.json')
App = Query()
import sys,time,random
from os import system, name
class_selection = None
import random
from playing import *
from colorama import Fore, Back, Style

#from playing import main


def y_n(one):
  if one == 1:
    return one
  elif one == 2:
    return one




def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')










def class_switch(entry):
    if entry == 1:
        print("Knight Selected\n")
        class_selection = 1
        return class_selection
    elif entry == 2:
        print("Mage Selected\n")
        class_selection = 2
        return class_selection
    elif entry == 3:
        print("Thief selected\n")
        class_selection = 3
        return class_selection
    else:
        print("Invalid entry.")



#typing_speed = 50 #wpm
def type(t, typing_speed):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')


print("""\

 _      _     ____  _     _____ _____    ____  _     ____  _      _____
/ \__/|/ \ /\/  _ \/ \   /  __//__ __\  /   _\/ \   /  _ \/ \  /|/  __/
| |\/||| | ||| | \|| |   |  \    / \    |  /  | |   | / \|| |\ |||  \  
| |  ||| \_/|| |_/|| |_/\|  /_   | |    |  \__| |_/\| \_/|| | \|||  /_ 
\_/  \|\____/\____/\____/\____\  \_/    \____/\____/\____/\_/  \|\____\

                    """)

def menu():
    string = type("Welcome to MUDLET. A clone written by Brncray & SSpzcee:)", 100)
    print("")
    print("1. Continue a game.. (game key required)")
    time.sleep(.1)
    print("2. Create a game")
    time.sleep(.1)
    print("3. Exit")
    time.sleep(.1)
    choice = int(input("Enter your choice: "))
    clear()
    if choice == 1:
        option1()
    elif choice == 2:
        option2()
    elif choice == 3:
        exit()
    else:
        print("Invalid choice. Please try again.")
        clear()
        menu()

def option1():
    game_key = int(input("Enter your game key.\n"))
    result = game_file.search(App.key == game_key)
    if result == []:
        print("Game not found.\n")
        choice = int(input("1. Go Back. 2. Retry\n"))
        if choice == 1:
          clear()
          menu()
        elif choice == 2:
          clear()
          option1()
        else:
          print("Invalid option\n")
          menu()

        clear()
    else:
      print("Game found!\n")
      clear()
      main(game_key)
    
    

def option2():
    print("Welcome to singleplayer Mudlet Clone!")
    name = input("Enter a character name:\n")
    clear()
    print("Enter a class.")
    print("1. Knight")
    print("2. Mage")
    print("3. Thief")

    
    strength = random.randint(5, 10)
    dexterity = random.randint(5, 10)
    intelligence = random.randint(5, 10)
    wisdom = random.randint(5,10)
    game_code = random.randint(1, 999999)

  
    class_selection = int(input(""))


    if class_selection == 1:
      print("You are a knight! This means you get a +3 strength prof\nYou get -1 intelligence because of this.")
      strength = strength + 3
      intelligence = intelligence -1
    elif class_selection == 2:
      print("You are a Mage! This means you get +3 wisdom\n You get -1 strength because of this\n")
      wisdom = wisdom + 3
      strength = strength -1
    elif class_selection == 3:
      print("You are a thief. Which means you get +3 dexterity\n You get -1 wisdom because of this")
      dexterity = dexterity + 3
      wisdom = wisdom -1
    print(Fore.GREEN)
    print(f"| STATS |\n Strength: {strength}\n Dexterity: {dexterity}\n Intelligence: {intelligence}\n Wisdom: {wisdom}")
    print(Fore.RED)
    print(f"Game code: {game_code}\n REMEMBER THIS CODE! WITHOUT IT YOU CAN NOT CONTINUE YOUR GAME AND MUST RESTART")
    print(Style.RESET_ALL)
      
      
      

    input("| ENTER TO CONTINUE |")
    game_file.insert({
      'name': name, 
      'class': class_selection, 
      'health': 20, 
      'hunger': 100, 
      'weapon': 0, 
      'checkpoint': 0, 
      'strength': strength, 
      'dexterity': dexterity, 
      'intelligence': intelligence, 
      'wisdom': wisdom, 
      'key': game_code, 
      'level': 1,
      'xp':0})
    clear()
    main(game_code)

menu()
