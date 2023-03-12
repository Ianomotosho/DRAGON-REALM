print("you  are in a land full of dragons.In front of you,you see two caves.In two cave,the dragon is friendly and will share it's treasure with you.But in the two caves the dragons will gobble you up and eat you")

while True:
  choice=input('which cave do you want to go to(1/2/3/4)')
  if choice in ('1','2','3','4'):
    if choice=='1':
      print('you were right that is correct now you have a lot of loot to give to your freinds')
    elif choice=='2':
      print('you approach the cave and it is dark and spooky and a dragon jumps out and goobles in one bite,oh no you died')
    elif choice=='3':
      print('you were right that is correct now you have a lot of loot to give to your freinds')
    elif choice=='4':
      print('you approach the cave and it is dark and spooky and a dragon jumps out and goobles in one bite,oh no you died')
      
    PlayAgain= input('want to play again(yes/no)')
    if PlayAgain == ('no'):
     break
  else:
    print('invalid input')
    
    