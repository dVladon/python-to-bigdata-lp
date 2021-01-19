"""
This is a reducer function: 
"""

import sys

from math import log


def tfidf(tf, dt):
    """
    Calculates tf*idf for word and article
    """
    idf = 1.0 / (log(1 + dt))
    tfidf = tf * idf

    return tfidf


articles_count = 0
    
# Main block
for line in sys.stdin:
    try:
        word, article_id, tf = line.strip().split('\t', 2)
        article_id, tf = int(article_id), float(tf)
    except ValueError as e:
        continue

    if article_id == 0:
        articles_count = tf
    else:
        print("%s\t%s\t%f" % (word, article_id, tfidf(tf, articles_count)))
