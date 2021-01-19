"""
This is a reducer function: 
"""

import sys


current_word = None
articles_count = 0
    
# Main block
for line in sys.stdin:
    try:
        word, article_id, tf = line.strip().split('\t', 2)
    except ValueError as e:
        continue

    if current_word != word:
        if current_word:
            print("%s\t%d\t%d" % (current_word, 0, articles_count))

        articles_count = 0
        current_word = word

    print("%s\t%s\t%f" % (word, article_id, float(tf)))
    articles_count += 1

if current_word:
    print("%s\t%d\t%d" % (current_word, 0, articles_count))
