def my_game():
    
   print("welcome to Treasure island \n Your mission is to find the treasure\n You are at cross road.Where do you want to go")
   choice = (input('right or left:'))
   print(choice)
   if choice == 'right':
    print('You fell into a hole. Game Over.')
    return
   elif choice == 'left':
    print("You've come to a lake. There is an island in the middle of the lake")
   else: 
    try:
       raise ValueError("invalid choice .Plz try again")
    except ValueError as a:
       print(a)
    return
   choice2 =input("Type 'wait' to wait for a boat. Type 'swim' to swim across.")

   if choice2 == 'swim':
     print('you are attacked by angry trout.Game over')
     return
   elif choice2 == 'wait':
     print("you reached at the island. There is a house with 3 doors.One red, one yellow and one blue.")
   else: 
    try:
       raise ValueError("invalid choice .Plz try again")
    except ValueError as a:
       print(a)
    return
   choice3 = input("Which color do you choose?")
   if choice3 == "red":
    print("it's a room full of fire.Game over")
    return
   elif choice3 == 'blue':
    print("you entered a room full of breasts .Game over")
   elif choice3 == 'yellow':
    print("you found the treasure. YOU WIN")
   else: 
    try:
       raise ValueError("invalid choice .Plz try again")
    except ValueError as a:
       print(a)
my_game()



