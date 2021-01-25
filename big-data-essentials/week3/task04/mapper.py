"""
This is a map function: 
  map: (<article> <text>) -> [(<permutation> <word> <count1>),]

Calculates all occurrences of a word in an article.
"""

import sys
import re

from collections import Counter


def get_stop_words():
    """
    Reads a file with stop words and parses it to set.
    """
    words = set()
    
    with open('stop_words_en.txt', 'r', encoding='utf-8') as f:
        words = {w.strip().lower() for w in f}
    
    return words


stop_words = get_stop_words()

# Main block
for line in sys.stdin:
    try:
        article_id, text = line.strip().split('\t', 1)
    except ValueError as e:
        continue

    words = [w.lower() for w in re.split(r"\W*\s+\W*", text, flags=re.UNICODE) if w.lower not in stop_words]
    counter = Counter(words)
    for word, count in counter.items():
        print("".join(sorted(word)), word, count, sep="\t")
