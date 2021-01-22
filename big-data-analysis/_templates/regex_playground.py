import re
import sys


REGEX = re.compile('<PUT REGEX HERE>')

for line in sys.stdin:
    match = REGEX.match(line)
    if match:
        print(*match.groups(), sep=",")

print(f"===\nPattern: {REGEX.pattern}")