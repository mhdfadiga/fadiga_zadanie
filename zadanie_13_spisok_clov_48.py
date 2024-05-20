import random
words = ["OVERUSED","CLAM","GUAM","TAFFETA","PYTHON","PYTHON","GUAM"]
random.shuffle(words)
unique_words = list(set(words))
for item in unique_words:
    print(item)

