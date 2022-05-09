import random

word_list = []
with open("all_answers.txt", "r") as wordles:
    for wordle in wordles:
        word_list.append(wordle[:5])


winner = random.choice(word_list)
has_won = False

while not has_won:
    attempt = input("Enter a word: ")
    if attempt == winner:
        has_won = True
    clue = ""
    clue_curr = ""
    for i in range(5):
        if attempt[i] == winner[i]:
            clue_curr = "3"
        elif attempt[i] in winner:
            clue_curr = "2"
        else:
            clue_curr = "1"
        clue += clue_curr
    print(clue)
