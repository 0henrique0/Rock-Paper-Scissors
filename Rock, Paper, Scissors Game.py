

def game():
    
    def win():
       nonlocal x
       print(' vs ')
       print(pc)
       print('')
       print('You won!')
       print('')
       x = input('Do you want to play again? (Yes/No)')
       if x == 'Yes':
            print('')
            game()
       elif x == 'No':
            return
               
    def lose():
       nonlocal x
       print(' vs ')
       print(pc)
       print('')
       print('You lost!')
       print('')
       x = input('Do you want to play again? (Yes/No)')
       if x == 'Yes':
            print('')
            game()
       elif x == 'No':
            return
       
    import random
    user = input('Rock, Paper or Scissors?\n ')
    pc = random.choice(['Rock', 'Paper', 'Scissors'])


    if user == pc:
        print(' vs ')
        print(pc)
        print('')
        print('That\'s a tie!')
        print('')
        x = input('Do you want to play again? (Yes/No)')
        if x == 'Yes':
            print('')
            game()
        elif x == 'No':
            return
        
    elif (user == 'Rock') and (pc == 'Paper'):
        lose()

    elif (user == 'Rock') and (pc == 'Scissors'):
        win()

    elif (user == 'Paper') and (pc == 'Rock'):
        win()

    elif (user == 'Paper') and (pc == 'Scissors'):
        lose()

    elif (user == 'Scissors') and (pc == 'Rock'):
        lose()
            
    elif (user == 'Scissors') and (pc == 'Paper'):
        win()
        

print('Welcome to this Rock, Paper, Scissors game!')
print('Type start to begin a game.')
y = input()
if y == 'start':
    game()




    
