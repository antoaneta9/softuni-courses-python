words = ['banana', 'apple', 'pineapple', 'mango', 'orange', 'tomato', 'avocado', 'pomegranate', 'lime', 'lemon', 'peach', 'strawberry', 'cranberry', 'blackberry', 'blueberry', 'apricot', 'pear']
sorted_words = sorted(words, key=lambda x: len(x), reverse=True)
print(sorted_words)

sorted_by_last_letter = sorted(words, key=lambda x: x[-1])
print(sorted_by_last_letter)

data = [("Ivan", 90), ("Maria", 100), ("Petar", 80), ("Andrei", 90)]
print(sorted(data, key=lambda x: x[1]))
print(sorted(data, key=lambda x: -x[1]))

sorting_ = sorted(data, key=lambda x: (-x[1], x[0]))
print(sorting_)



