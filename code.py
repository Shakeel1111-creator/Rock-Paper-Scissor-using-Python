import random
options=('rock','paper','scissor')
player=input('enter your choice (rock.paper,scissor):')
if player not in options:
    player=input('enter your choice (rock.paper,scissor):')

print('Your choice:',player)
computer=random.choice(options)
print('Computer choice:',computer)

if computer==player:
    print('Game is Tie')
elif player=='rock' and computer=='scissor':
    print("You win")
elif player=='paper' and computer=='rock':
    print("You win")
elif player=='scissor' and computer=='paper':
    print("You win")
else:
    print("You lose")


