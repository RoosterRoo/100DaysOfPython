import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


rock_paper_scissors = [rock, paper, scissors]

my_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
if my_choice >= 3 or my_choice < 0:
    print('Invalid input, you lose')

else:
    print(rock_paper_scissors[my_choice])

    computer_choice = random.randint(0, len(rock_paper_scissors) - 1)
    print(rock_paper_scissors[computer_choice])

    decision = (my_choice - computer_choice) % len(rock_paper_scissors)

    if decision == 1:
        print('You win!')
    elif decision == 0:
        print('It\'s a draw')
    else:
        print('You lose!')

