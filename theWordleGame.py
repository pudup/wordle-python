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
    clue = ["1", "1", "1", "1", "1"]
    win_hold = winner
    for i in range(5):
        if attempt[i] == winner[i]:
            clue[i] = "3"
            first_char = winner.find(attempt[i])
            winner = winner[:first_char] + ' ' + winner[first_char + 1:]
    for i in range(5):
        if attempt[i] in winner and clue[i] == "1":
            clue[i] = "2"
            first_char = winner.find(attempt[i])
            winner = winner[:first_char] + ' ' + winner[first_char + 1:]
    clueFin = ""
    winner = win_hold
    for curclue in clue:
        clueFin += curclue
    print(clueFin)
