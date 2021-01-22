import re
import sys


REGEX = re.compile('^<row.*?(?=\\bId="(\\d+)).*(?=\\bCreationDate="(\\d{4}))(?=\\bCreationDate="(\\d{4}-\\d{2})).*$')

for line in sys.stdin:
    match = REGEX.match(line)
    if match:
        print(*match.groups(), sep=",")

print(f"===\nPattern: {REGEX.pattern}")