word_list = []
with open("all_answers.txt", "r") as wordFile:
    for wordAnswer in wordFile.readlines():
        word_list.append(wordAnswer[:5])
all_words = []
with open("all_words.txt", "r") as allWordFile:
    for allWordAnswer in allWordFile.readlines():
        all_words.append(allWordAnswer[:5])


def evaluateAnswer(answer, attempt):
    if attempt == answer:
        return "33333"
    cluey = ["1", "1", "1", "1", "1"]
    for i in range(5):
        if attempt[i] == answer[i]:
            cluey[i] = "3"
    for i in range(5):
        if attempt[i] in answer and cluey[i] == "3":
            first_char = answer.find(attempt[i])
            answer = answer[:first_char] + ' ' + answer[first_char + 1:]
        if attempt[i] in answer and cluey[i] == "1":
            cluey[i] = "2"
            first_char = answer.find(attempt[i])
            answer = answer[:first_char] + ' ' + answer[first_char + 1:]
    clueyd = ""
    for curclue in cluey:
        clueyd += curclue
    return clueyd

first_attempt = True
first_word = ["raise"] # The program always chooses this first anyway so this saves time on initial spin up

for i in range(5):
    min_count = 1e7
    if first_attempt:
        words_to_try = first_word
        first_attempt = False
    else:
        words_to_try = all_words

    # Idea to find best worst case scenario gotten from -> https://github.com/techtribeyt/Wordle
    for word_to_try in words_to_try:
        temporary_dict = {}

        for pot_answer in word_list:
            curr_clue = evaluateAnswer(pot_answer, word_to_try)

            if curr_clue not in temporary_dict:
                temporary_dict[curr_clue] = [pot_answer]
            else:
                temporary_dict[curr_clue].append(pot_answer)

        best_worst_case_length = max([len(value) for value in temporary_dict.values()])
        if best_worst_case_length < min_count:
            min_count = best_worst_case_length
            word_to_use = word_to_try
            potential_words = temporary_dict

    print(f"Try: {word_to_use}")
    word_list = potential_words[input("Enter result as 1-Grey, 2-Yellow, 3-Green (eg. 12321): ")]
    if len(word_list) == 1:
        break

print(f"Answer is: {word_list[0] if word_list else 'unknown'}")





