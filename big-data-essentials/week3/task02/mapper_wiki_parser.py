
import sys
import re


def log(message, **kwargs):
    """
    Prints a given message to sys.stderr stream.
    """
    print(message, file=sys.stderr, **kwargs)
    
    
def counter(name, value):
    """
    Prints a MapReduce job counter.
    """
    log("reporter:counter:Wiki Stats,%s,%d" % (name, value))
    

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

    words = re.split(r"\W*\s+\W*", text, flags=re.UNICODE)
    for word in words:
        if word in stop_words:
            counter("Stop words", 1)
        
        counter("Total words", 1)
        
        print("%s\t%d" % (word.lower(), 1))
