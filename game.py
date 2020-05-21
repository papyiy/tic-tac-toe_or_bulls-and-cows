def tictactoe_main():
    ttt_intro()
    ttt_start_game_field()
    move = 0

    while True:
        move, player = ttt_player_moves(move)
        ttt_take_move(move, player)


def ttt_intro():
    """Introduction for user"""
    print("Welcome to TicTacToe game.",
          "For rules use this link: https://en.wikipedia.org/wiki/Tic-tac-toe",
          "Let's begin!",
          sep="\n",
          end="\n\n")

def ttt_start_game_field():
    print(6 * "-")
    i = 1
    while i < 10:
        print(f"{i}",f"{i+1}",f"{i+2}", sep="|")
        print(6 * "-")
        i += 3
    print(25 * "=")

def ttt_player_moves(move = 0):
    move += 1

    if move % 2 != 0:
        player = "o"
    else:
        player = "x"

    return move, player

def ttt_take_move(move, player):
    while True:
        player_choice = input(f"Round {move} - Player {player} use number [1-9] to determine your move: ")
        try:
            if not int(player_choice) in range(1,9):
                print(f"Your value {player_choice} is incorrect. Resetting round...")
            else:
                break
        except ValueError:
            print(f"Your value {player_choice} is incorrect. Resetting round...")

tictactoe_main()

# import random, time
# '''Author = Jan Papousek'''
#
# def bullscows_main():
#     bc_intro()
#     our_number = bc_generate_number()
#     print(our_number)
#     counter = 0
#     start = 0
#     while True:
#         user_guess, counter, start = bc_take_guess(counter, start)
#         if bc_incorrect_guess(user_guess) == False:
#             continue
#         cows, bulls = bc_evaluate(our_number, user_guess)
#         bc_output(cows, bulls)
#         if bulls == 4:
#             end = bc_time(start)
#             print(f"Great job. It took you {counter} tries in {end}")
#             break
#
# def bc_intro():
#     """Introduction for user"""
#     print("Welcome to Bulls&Cows game.",
#           "For rules use this link: https://en.wikipedia.org/wiki/Bulls_and_Cows",
#           "I've generated 4 secret numbers for you.",
#           sep="\n")
#
# def bc_generate_number():
#     return random.randint(1000,4000)
#
# def bc_take_guess(counter, start_time):
#     counter += 1
#     if start_time == 0:
#         start_time = time.time()
#     return input("Please guess a number: "), counter, start_time
#
# def bc_incorrect_guess(value):
#     if not value.isdigit():
#         print(f"ERROR: Your guess is not a number. You must enter a 4-digit integer.")
#         return False
#
#     elif not len(value) == 4:
#         print(f"ERROR: Your guess has {len(value)} digits. You must enter a 4-digit integer.")
#         return False
#
# def bc_evaluate(number, guess):
#     bulls = 0
#     cows = 0
#     number_image = list(str(number))
#     guess_image = list(str(guess))
#     number = list(str(number))
#
#     for index,digit in enumerate(guess):
#         if digit == number[index]:
#             bulls += 1
#             number_image.remove(digit)
#             guess_image.remove(digit)
#
#     for digit in reversed(number_image):
#         if digit in guess_image:
#             cows += 1
#             number_image.remove(digit)
#             guess_image.remove(digit)
#
#     return cows, bulls
#
# def bc_output(cows, bulls):
#     if bulls == 1:
#         bulls_name = "bull"
#     else:
#         bulls_name = "bulls"
#
#     if cows == 1:
#         cows_name = "cow"
#     else:
#         cows_name = "cows"
#
#     print(f"{bulls} {bulls_name}, {cows} {cows_name} ")
#
# def bc_time(start):
#     end_time = time.time() - start
#     minutes = int(end_time // 60)
#     seconds = int(end_time % 60)
#     return f"{minutes} minutes and {seconds} seconds"
#
#
# bullscows_main()