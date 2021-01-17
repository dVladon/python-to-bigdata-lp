"""
This is a map function: 
  map: (<article_id> <text>) -> [(<word> <1 if as name, 0 otherwise>),]

Skips all words start with a digital.
"""

import sys
import re


def is_name(word):
    """
    Checks is the word used as name. 
    Condition - the first character is uppercase, 
    all the other characters that are letters are lowercase.
    
    :return: 1 if the word used as name, otherwise 0.
    """
    if word[0].isupper() and (len(word) < 2 or word[1:].islower()):
        return True
    
    return False
    

# Main block
for line in sys.stdin:
    try:
        article_id, text = line.strip().split('\t', 1)
    except ValueError as e:
        continue

    words = re.split(r"\W*\s+\W*", text, flags=re.UNICODE)
    for word in words:
        if len(word) > 0 and word[0].isalpha():
            if is_name(word):
                print("%s\t%d" % (word.lower(), 1))
            else:
                print("%s\t%d" % (word.lower(), 0))
