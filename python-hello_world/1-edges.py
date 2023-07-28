word = "Holberton"
word_first_3 = slice(0,3)
word_last_2 = slice(-2, None)
middle_word = slice(1,-1)
print("First 3 letters: {}".format(word[word_first_3]))
print("Last 2 letters: {}".format(word[word_last_2]))
print("Middle word: {}".format(word[middle_word]))
word = "School"
print("First 3 letters: {}".format(word[word_first_3]))
print("Last 2 letters: {}".format(word[word_last_2]))
print("Middle word: {}".format(word[middle_word]))