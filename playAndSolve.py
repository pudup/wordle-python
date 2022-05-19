import random

word_list = []
with open("all_answers.txt", "r") as wordFile:
    for wordAnswer in wordFile.readlines():
        word_list.append(wordAnswer[:5])

is_in_word = []
is_in_position = {}
wrong_position = {}
not_in_word = []
curr_words = []

winner = random.choice(word_list)
# print(f"Winner is {winner}")
has_won = False

number_of_tries = 0

while len(is_in_position) < 5:
    while not has_won:
        number_of_tries += 1
        if word_list:
            # user_choice = random.choice(word_list)
            user_choice = input("Enter word: ")
            # print(f"Computer chose: {user_choice}")
        else:
            has_won = True
            break
        attempt = user_choice
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
        user_choice_positions = clueFin
        print(user_choice_positions)
        for posi, num in enumerate(user_choice_positions):
            match num:
                case "3":
                    if user_choice[posi] not in is_in_word:
                        is_in_word.append(user_choice[posi])
                    is_in_position[posi] = user_choice[posi]
                    if user_choice[posi] in not_in_word:
                        not_in_word.remove(user_choice[posi])
        for posi, num in enumerate(user_choice_positions):
            match num:
                case "2":
                    if user_choice[posi] not in is_in_word:
                        is_in_word.append(user_choice[posi])
                    if user_choice[posi] in not_in_word:
                        not_in_word.remove(user_choice[posi])
                    wrong_position[posi] = user_choice[posi]
        for posi, num in enumerate(user_choice_positions):
            match num:
                case "1":
                    if user_choice[posi] in is_in_word:
                        wrong_position[posi] = user_choice[posi]
                    elif user_choice[posi] not in not_in_word:
                        not_in_word.append(user_choice[posi])

        for word in word_list:
            if user_choice_positions == "11111":
                curr_words.append(word)
            elif user_choice == word and user_choice_positions != "33333":
                if word in curr_words:
                    curr_words.remove(word)
            else:
                for letter in is_in_word:
                    if letter in word:
                        if word not in curr_words:
                            curr_words.append(word)
            for pos_in in is_in_position:
                if word[pos_in] != is_in_position[pos_in]:
                    if word in curr_words:
                        curr_words.remove(word)
            for pos_out in wrong_position:
                if word[int(pos_out)] == wrong_position[int(pos_out)]:
                    if word in curr_words:
                        curr_words.remove(word)
            for not_in_letter in not_in_word:
                if not_in_letter in word:
                    if word in curr_words:
                        curr_words.remove(word)
            for allets in is_in_word:
                if allets not in word:
                    if word in curr_words:
                        curr_words.remove(word)

        word_list = curr_words
        curr_words = []
print(number_of_tries)
