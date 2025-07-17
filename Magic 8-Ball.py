# import necessary libraries
import random # to generate random numbers
import time # to simulate thinking time

# print welcome message and ASCII art
print('Welcome to the Magic 8-Ball game!')
print('''
       000000000000000000000000000000
                    888
                888    888
            888             888
            888             888
            888             888
                888     888
                    888   
                888    888   
            888             888 
            888             888
            888             888
                888     888
                    888                                                                          
       000000000000000000000000000000\n
''')

# assign the user name
user_name = input('what is your Name? ').strip()

# assign user_name length parameters
user_name_min_length = 2
user_name_max_length = 15

# validate user input for: input, length, numbers, special characters | prompt user to re-enter if invalid
while (
    not user_name 
    or len(user_name) < user_name_min_length 
    or len(user_name) > user_name_max_length
    or not all(char.isalpha() or char == ' ' or char == '-' or char == "'" for char in user_name)
):
  print('''Inputs must:\n 
            Be between 2 and 15 letters\n
            Cannot contain numbers\n
            Only special characters allowed: space, hyphen, and aposterphe\n''')
  user_name = input('What is your Name? \n')
print(f'Hello {user_name}! \n')
time.sleep(1)

# generate a new random answer
answers = [
    'Yes - definitely', 
    'It is decidedly so', 
    'Without a doubt',
    'Reply hazy, try again', 
    'Ask again later', 
    'Better not tell you now',
    'My sources say no', 
    'Outlook not so good', 
    'Very doubtful', 
    'Not a chance'
]
answer = random.choice(answers)

# assign the user question
print('We will draw from the energy of the universe to answer your question with yes, no, or maybe answers. \n')
time.sleep(3)
user_question = input('What is your question? ').strip()

# assign user_question length parameters
user_question_min_length = 10
user_question_max_length = 50

# validate user input for: input, length, no numbers, special characters, ends with a question mark | prompt user to re-enter if invalid
while (
  not user_question
  or len(user_question) < user_question_min_length
  or len(user_question) > user_question_max_length
  or not all (char.isalpha() or char == ' ' or char == '?' for char in user_question)
  or not user_question.strip().endswith('?')
):
  print('Please provide a valid question (10-50 characters, only letters, spaces, and must end with a "?").\n')
  user_question = input('Ask your question. ')

# build some dramatic tension before the answer
time.sleep(1)
print('Accessing the stars...')
time.sleep(2)
print('Consolidating cosmic data...\n')
time.sleep(3)

# print the answer to the user's question
print(f'{answer}\n')

# ask the user if they want to play again
play_again = input('Do you want to ask another question? (yes/no) ').strip().lower()
while play_again not in ['yes', 'no']:
    print('Please answer with "yes" or "no".')
    play_again = input('Do you want to ask another question? (yes/no) ').strip().lower()

# Main game loop to allow the user to ask multiple questions
while play_again == 'yes':
    # ask the user for a new question
    user_question = input('What is your question? ').strip()

    # validate the new question
    while (
        not user_question
        or len(user_question) < user_question_min_length
        or len(user_question) > user_question_max_length
        or not all(char.isalpha() or char == ' ' or char == '?' for char in user_question)
        or not user_question.strip().endswith('?')
    ):
        print('Please provide a valid question (10-50 characters, only letters, spaces, and must end with a "?").\n')
        user_question = input('Ask your question. ')

    # generate a new random answer
    answer = random.choice(answers)

    # build some dramatic tension before the new answer
    time.sleep(1)
    print('Accessing the stars...')
    time.sleep(2)
    print('Consolidating cosmic data...\n')
    time.sleep(3)

    # print the new answer to the user's question
    print(f'{answer}\n')

    # ask if they want to play again
    play_again = input('Do you want to ask another question? (yes/no) ').strip().lower()
time.sleep(1)

# thank the user for playing
print('\nThank you for playing the Magic 8-Ball game! Goodbye!\n')
# end of the game

