"""Создайте программу, которая будет выводить список слов в случайном порядке. На экране должны печататься
без повторений все слова из представленного списка. """
import random
words = ["OVERUSED","CLAM","GUAM","TAFFETA","PYTHON","PYTHON","GUAM"]
random.shuffle(words)
unique_words = list(set(words))
for item in unique_words:
    print(item)

