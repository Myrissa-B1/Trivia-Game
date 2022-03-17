def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("_________________________")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter(A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

        display_score(correct_guesses, guesses)

# --------------------------------


def check_answer(answer, guess):

    if answer == guess:
        print("YOU'RE CORRECT!")
        return 1
    else:
        print("TRY AGAIN!")
        return 0

# ---------------------------------


def display_score(correct_guesses, guesses):
    print("_______________________")
    print("RESULTS")
    print("_______________________")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# --------------------------------------


def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -----------------------------------


questions = {
    "What serial killer had a yellow volkswagon?: ": "A",
    "Who wast he infamous serial killer that tried to turn his victims into zombies?: ": "B",
    "When was the term 'serial killer' first coined?: ": "C",
    "Which of the following serial killers kept the heads of his victims in a freezer?: ": "D",
    "Which serial killer was known for beheading and dismembering his victims?: ": "A"
}

options = [["A. Ted Bundy", "B. Gary Ridway", "C. Richard Ramirez", "D. Ed Gein"],
           ["A. Ted Bundy", "B. Jeffery Dahmer",
               "C. Edmund Kemper", "D. Albert Fish"],
           ["A. 1925", "B. 1940", "C. 1981", "D. 1990"],
           ["A. Jack the Ripper", "B. Harold Shipman",
               "C. Jane Toppan", "D. Jeffrey Dahmer"],
           ["A. Cleveland Torso", "B. BTK", "C. Son of Sam", "D. Billy the kid"]]

new_game()


while play_again():
    new_game()

print("Hope to see you again!")

# -------------------------
