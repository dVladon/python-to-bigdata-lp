
import sys


current_word = None
word_count = 0

# Main block
for line in sys.stdin:
    try:
        word, count = line.strip().split('\t', 1)
    except ValueError:
        continue
        
    if current_word != word:
        if current_word:
            print("%s\t%d" % (current_word, word_count))
        
        word_count = 0
        current_word = word
    
    word_count += int(count)
    
if current_word:
    print("%s\t%d" % (current_word, word_count))
