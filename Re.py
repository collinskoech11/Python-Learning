import re

pattern = r'spam'

match = re.search(pattern, 'eggsspamsausages')
if match:
    print(match.group())
    print(match.start())