import random
import time

def displayIntro():
  print("you are in a land full of dragons.In front of you,you see two caves.In one cave,the dragon is freindly and will share his tresure with you. The other dragon is greeddy and hungry and will eat you on sight")
print()

def choose_cave():
  cave=''
  while cave != '1' and cave != '2':
    print('which cave will you go into? (1 or 2)')
    cave=input()

    return cave



def checkCave(chosenCave):
  print('you approach the cave')
  time.sleep(1)
  print('it is dark and spooky')
  time.sleep(2)
  print('a large dragon jumps in front of you and opens it jaws and')
  print()
  time.sleep(2)

  friendlyCave= random.randint(1,2)
  
  if chosenCave == str(friendlyCave):
   print('gives you his tresure')
  else:
   print('gobbles you down in one bite')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
  displayIntro()
  caveNumber = choose_cave()
  checkCave(caveNumber)

  print('do you want to play again(yes or no)')
  playAgain= input()