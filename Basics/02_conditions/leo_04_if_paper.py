import random
player = int(input('Your action rock (1) / scissors (2) / paper (3): '))

# Computer has random action
computer = random.randint(1, 3)

print('Player: %d, computer: %d' % (player, computer))

# if (()
# or ()
# or ())

# Result
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print('Yeah, you won!!')
elif player == computer:
    print('Tie')
else:
    print("You lost...")
