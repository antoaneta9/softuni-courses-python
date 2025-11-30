sentence = input().lower()
# words count
def words_count(text):
    list_of_words = text.split()
    count = len(list_of_words)
    return f"Words count is: {count}."

def avg_word_length(text):
    split_text = text.split()
    avg_len = sum(len(word) for word in split_text) / len(split_text)
    return f"Average word length: {avg_len:.2f}."

def most_common_word(text):
    list_of_words = text.split()
    words_dict = {}

    for word in list_of_words:
        if word not in words_dict:
            words_dict[word] = 0
        words_dict[word] += 1

    most_common = max(words_dict, key=words_dict.get)
    return f"Most common word is: {most_common}"

def search_words(text, searched_word):
    list_of_words = text.split()
    count = 0
    for word in list_of_words:
        if word == searched_word.lower():
            count += 1
    if count > 0:
        return f"The word '{searched_word}' appears ({count}) times."
    else:
        return f"The word '{searched_word}' was not found."

while True:
    cmd = input()
    if cmd == "end":
        print("Goodbye!")
        break

    if cmd == 'count':
        print(words_count(sentence))
    elif cmd == 'average':
        print(avg_word_length(sentence))
    elif cmd == 'common':
        print(most_common_word(sentence))
    elif cmd.startswith('search'):
        parts = cmd.split()

        if len(parts) == 2:
            searched_word = parts[1]
            print(search_words(sentence, searched_word))
        else:
            print('Word not found.')



