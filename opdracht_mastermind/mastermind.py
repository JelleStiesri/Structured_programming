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
        elif game == '3':
            print('hoi')
        elif game == '4':
            game_4()


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
    feedback = {'B': 0, 'W': 0}

    for i in range(0, 4):
        if code[i] == guess[i]:
            feedback['B'] += 1
        elif guess[i] in code:
            if guess.count(guess[i]) == code.count(guess[i]):
                count = 0
                for x in range(0, 4):
                    if x == guess[i]:
                        count += 1
                if count > code.count(guess[i]):
                    feedback['W'] = code.count(guess[i]) - count
                else:
                    feedback['W'] += 1

        else:
            continue

    return feedback


def code_guess(lst):
    code = input('Enter a code: ')
    if not code.isdigit():
        print('Enter a code with numbers between one and six')
    else:
        attempts = 0
        lives = 10
        while lives > 0:
            guess = random.choice(lst)
            feedback = create_feedback(code, guess)
            for i in reversed(lst):
                item_feedback = create_feedback(guess, i)
                if feedback != item_feedback:
                    lst.remove(i)

            lives -= 1
            attempts += 1
            if guess == code:
                print('De computer heeft de code geraden in ', attempts, ' pogingen')
                break
            elif lives == 0:
                print('GAME OVER')


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

                    random.shuffle(feedback)
                    feedback = "-".join(feedback)
                    print(feedback)

    if lives == 0:
        print('GAME OVER')
        exit()


def game_2():
    all_answers = create_all_answers()
    code_guess(all_answers)


def game_4():
    print('hoi')


game_menu()
"""
bronvermeldingen:
"""
