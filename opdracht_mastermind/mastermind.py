import random


def create_code():
    code = ''
    for i in range(0, 4):
        number = random.randint(1, 6)
        code_num = str(number)
        code += code_num

    return code


def game_menu():
    print("""
Welcome to mastermind
Guess the four number code
Each number in the code is between 1 and 6
B = right number in the right spot
W = right number but in the wrong spot
X = number not in the code

Gamemodes:
1. cpu gives a code player guesses
2. player gives code cpu guesses (algorithm 1)
3. player gives code cpu guesses (algorithm 2)
4. player gives code cpu guesses (self made algorithm 3)
    """)

    game = input('Enter your choice: ')
    if game.isdigit():
        if game == '1':
            game_1()
        elif game == '2':
            game_2()


def create_all_answers():
    all_answers = []
    for i in range(1111, 6667):
        answer = str(i)
        if '7' in answer or '8' in answer or '9' in answer or '0' in answer:
            continue
        else:
            all_answers.append(answer)

    return all_answers


def create_feedback(code, guess):
    player_input = input('Give feedback with X, W and B: ')
    player_feedback = []
    feedback = {}
    for i in player_input:
        if i != 'X' and i != 'W' and i != 'B':
            value = ' '
            player_feedback.append(value)
        else:
            value = i
            player_feedback.append(value)
    for i in range(0, 4):
        feedback[guess[i]] = player_feedback[i]

    return feedback


def code_guess(lst):
    code = input('Enter a code: ')
    if not code.isdigit():
        print('Enter a code with numbers between one and six')
    else:
        first_guess = '1234'
        attempts = 1
        lives = 10
        print('Computers first guess: ', first_guess)

        if first_guess == code:
            print('The computer found the correct code in ', attempts, ' attempts')
        else:
            feedback = create_feedback(code, first_guess)
            lives -= 1
            attempts += 1

            for i in feedback:
                if feedback[i] == 'X':
                    print(i, feedback[i])
                    for x in lst:
                        if str(i) in x:
                            print(x)
                            lst.remove(x)


def game_1():

    lives = 10
    code = create_code()

    while lives > 0:
        guess = input("Guess the code: ")
        if not guess.isdigit():
            print('Enter a code with numbers between one and six')
        else:
            if len(guess) != 4:
                print('Enter a four digit code')
            else:
                if code == guess:
                    print('You guessed the code')
                    exit()

                else:
                    feedback = []
                    for i in range(0, len(guess)):
                        if guess[i] == code[i]:
                            feedback.append('B')

                        elif guess[i] in code:
                            feedback.append('W')

                        else:
                            feedback.append('X')
                    lives -= 1

                    feedback = "-".join(feedback)
                    print(feedback)

    if lives == 0:
        print('GAME OVER')
        exit()


def game_2():
    all_answers = create_all_answers()
    code_guess(all_answers)


game_menu()
"""
bronvermeldingen:
"""
