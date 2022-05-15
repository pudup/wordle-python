word_list = []
with open("all_answers.txt", "r") as wordFile:
    for wordAnswer in wordFile.readlines():
        word_list.append(wordAnswer[:5])

is_in_word = []
is_in_position = {}
wrong_position = {}
not_in_word = []
letter_count = {}
curr_words = []

while len(is_in_position) < 5:
    user_choice = input("Type your word: ")
    user_choice_positions = input(f"Enter pos1-5 as 1-Grey 2-Yellow 3-Green, (eg-11231): ")
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
                    if user_choice[posi] not in letter_count:
                        letter_count[user_choice[posi]] = 2
                    else:
                        letter_count[user_choice[posi]] += 1
                elif user_choice[posi] not in not_in_word:
                    not_in_word.append(user_choice[posi])

    for word in word_list:
        if user_choice_positions == "11111":
            curr_words.append(word)
        elif user_choice == word and user_choice_positions != "33333":
            if word in curr_words:
                curr_words.remove(word)
        else:
            all_len = len(is_in_word)
            all_in = 0
            for letter in is_in_word:
                if letter in word:
                    all_in += 1
                if all_in == all_len:
                    if word not in curr_words:
                        curr_words.append(word)
        for pos_in in is_in_position:
            if word[pos_in] != is_in_position[pos_in]:
                if word in curr_words:
                    curr_words.remove(word)
        for pos_out in wrong_position:
            if word[int(pos_out)] == wrong_position[pos_out]:
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
        for charcount in letter_count:
            if letter_count[charcount] <= word.count(charcount):
                if word in curr_words:
                    curr_words.remove(word)

    word_list = curr_words
    curr_words = []
    if len(word_list) <= 1: z
    print(word_list)
    break
print(word_list)
