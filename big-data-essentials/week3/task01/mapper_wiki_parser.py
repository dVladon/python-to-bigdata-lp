
import re
import sys

from collections import Counter


def log(message, **kwargs):
    """
    Prints a given message to sys.stderr stream.
    """
    print(message, file=sys.stderr, **kwargs)
    

# Main block
for line in sys.stdin:
    try:
        article_id, text = line.strip().split('\t', 1)
    except ValueError:
        continue
    
    words = re.split(r"\W*\s+\W*", text, flags=re.UNICODE)
    counter = Counter(words)
    for word, count in counter.items():
        log("reporter:counter:Wiki stats,Total words,%d" % count)
        print("%s\t%d" % (word.lower(), count))
