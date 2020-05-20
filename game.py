import random
# def main():

def bullscows():
    bc_intro()
    our_number = bc_generate_number()
    print(our_number)
    while True:
        user_guess = bc_take_guess()
        if bc_incorrect_guess(user_guess) == False:
            continue
        bc_evaluate(our_number, user_guess)

def bc_intro():
    """Introduction for user"""
    print("Welcome to Bulls&Cows game.",
          "For rules use this link: https://en.wikipedia.org/wiki/Bulls_and_Cows",
          "I've generated 4 secret numbers for you.",
          sep="\n")

def bc_generate_number():
    return random.randint(1000,4000)

def bc_take_guess():
    return input("Please guess a number: ")

def bc_incorrect_guess(value):
    if not value.isdigit():
        print(f"ERROR: Your guess is not a number. You must enter a 4-digit integer.")
        return False
    elif not len(value) == 4:
        print(f"ERROR: Your guess has {len(value)} digits. You must enter a 4-digit integer.")
        return False

def bc_evaluate(number, guess):
    bulls = 0
    cows = 0
    number_image = list(str(number))
    guess_image = list(str(guess))
    number = list(str(number))
    # unsolved = list(range(0,len(guess)))
    # unsolved = number

    for index,digit in enumerate(guess):
        if digit == number[index]:
            bulls += 1
            # unsolved.remove(index)
            number_image.remove(digit)
            guess_image.remove(digit)

    print(bulls, cows, number_image, guess_image)
    # for nmb in image:
    #     if nmb in guess:
    #         cows += 1
    #         image.remove(nmb)

    for digit in reversed(number_image):
        if digit in guess_image:
            cows += 1
            number_image.remove(digit)
            guess_image.remove(digit)

    print(bulls, cows, number_image, guess_image)

bullscows()