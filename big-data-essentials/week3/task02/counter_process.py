
#! /usr/bin/env python

import sys
import re


STOP_WORDS_COUNTER_RE = re.compile("Stop words=\d+")
TOTAL_WORDS_COUNTER_RE = re.compile("Total words=\d+")


def parse_logs():
    """
    Parses raw logs of MapReduce job and 
    returns values of two counters as tuple.
    """
    stop_words = 0
    total_words = 0
    
    for line in sys.stdin:
        
        if STOP_WORDS_COUNTER_RE.search(line):
            stop_words = int(line.strip().split("=", 1)[1])
            
        if TOTAL_WORDS_COUNTER_RE.search(line):
            total_words = int(line.strip().split("=", 1)[1])
    
    return stop_words, total_words


if __name__ == '__main__':
    stop_words, total_words = parse_logs()
    print(stop_words / float(total_words) * 100)
