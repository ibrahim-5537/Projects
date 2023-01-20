# Note for Abayomi
# The issue I am trying to fix is that when an invalid response is entered, the loop resets from the start. I am trying to add a condition so that after entering an invalid input, the position within the game is maintained until a valid input is entered. 


# Text-Based Python adventure game

# The game has a simple design built around nested if/elif/else conditions.

# Each player decision branches into another loop, with 6 distinct possible ending scenarios. 

#The game also includes options for the user to make choices that affect the outcome of the game, such as opening a chest or using a key to open a door.

# The 'lower' function converts user inputs to lowercase to avoid any errors 

# Begin with asking user to input name
name = input('Welcome to Text Adventure. Please enter your name. ')

# Establish 'while True' loop to account for error handling for invalid inputs,
while True:
    answer = input(f'Hello {name}, Would you like to play a game? (Y/N) ' ).lower()
    
    if answer == 'y':
        print('You awake in a dark corridor. There\'s a door to your right and left.') 
        direction1 = input('Which direction do you choose? (R/L) ' ).lower()

        if direction1 == 'r':
            print('You\'ve entered a large room with a wooden chest in middle.')
            action1 = input('Do you wish to open the chest? (Y/N) ' ).lower()

            if action1 == 'y':
                print('You find a golden key inside and save it for later.')
                action3 = input('There are stairs leading out of the room. Do you go up or down? (up/down) ' )
                
                if action3 == 'up':
                    print('You climb up the stairs and are faced with a locked door.')
                    action4 = input('Do you wish to use the key to open the door? (Y/N) ').lower()

                    if action4 == 'y':
                        print('The door unlocks and you are free. Congratulations. You win!')

                    elif action4 == 'n':
                        print('Gameover! You lost because you are too boring!')

                elif action3 == 'down':
                    print('You walk down the stairs and trip and fall. Game over!')

                else: print('Invalid response.')
                        
            elif action1 == 'n':
                print('You leave the chest alone. There are stairs leading out of the room.')
                action2 = input('Do you go up or down? (up/down) ' ).lower()

                if action2 == 'up':
                    print('You climb up the stairs. There is a locked door but you have no key and it\'s too late. Gameover!')

                elif action2 == 'down':
                    print('You walk down the stairs and trip and fall. Game over!')
                    
                else: print('Invalid response.')
        elif direction1 == 'l':
            print('You open the rusty door and fall into a trap! Game over.')

    elif answer == 'n':
        print('That\'s too bad. Goodbye')
        break

    else: print('Invalid response. Please enter Y or N')
    play_again = input('Would you like to play again? (Y/N) ').lower()
    
    if play_again == 'n':
        print("Thank you for playing!")
        break
