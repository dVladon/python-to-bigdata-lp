"""
This is a reducer function: 
  combiner: (<word> <1 if as name, 0 otherwise>) -> [(<word> <num as name>]
  
  A word is a name if there are less than 0.5% occurrences of this word, 
  when this word regardless to its case appears.
"""

import sys


def is_name(total, as_name):
    """
    Returns True if there are less than 0.5% 
    occurrences of this word when the word is not a name.
    """
    if as_name / float(total) >= 0.95:
        return True
    
    return False


current_word = None
word_total_count = 0
word_count_as_name = 0
    

# Main block
for line in sys.stdin:
    try:
        word, occurrence = line.strip().split('\t', 1)
    except ValueError as e:
        continue

    if current_word != word:
        if current_word and is_name(word_total_count, word_count_as_name):
            print("%s\t%d" % (current_word, word_count_as_name))

        word_total_count = 0
        word_count_as_name = 0
        current_word = word

    word_count_as_name += int(occurrence)
    word_total_count += 1

if current_word and is_name(word_total_count, word_count_as_name):
    print("%s\t%d" % (current_word, word_count_as_name))
