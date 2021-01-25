"""
This is a combiner function: 
  combine: (<permutation> <word> <count1>) -> [(<permutation> <word> <count2>),]
  
  Calculates all occurrences of a word in several articles.
"""

import sys


current_word = None
current_permutation = None
word_count = 0

# Main block
for line in sys.stdin:
    try:
        permutation, word, count = line.strip().split('\t', 2)
    except ValueError as e:
        continue

    if current_word != word:
        if current_word:
            print(current_permutation, current_word, word_count, sep="\t")

        word_count = 0
        current_word = word
        current_permutation = permutation

    word_count += int(count)

if current_word:
    print(current_permutation, current_word, word_count, sep="\t")
