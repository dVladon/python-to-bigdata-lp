"""
This is a reducer function: 
  reduce: (<permutation> [(<word> <count2>)]) -> [(<total_count> <unique_words_count> [<word>,]),]
"""

import sys


current_permutation = None
words = set()
words_count = 0
    
# Main block
for line in sys.stdin:
    try:
        permutation, word, count = line.strip().split('\t', 2)
    except ValueError as e:
        continue

    if current_permutation != permutation:
        if current_permutation and len(words) > 1:
            print(words_count, current_permutation, len(words), ",".join(words), sep="\t")

        words_count = 0
        words = set()
        current_permutation = permutation

    words_count += int(count)
    words.add(word)

if current_permutation and len(words) > 1:
    print(words_count, len(words), ",".join(sorted(words)), sep="\t")
