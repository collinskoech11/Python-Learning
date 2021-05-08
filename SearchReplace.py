import re

strn = "My name is Diana.i am a girl"
pattern = r"Diana" 
match = re.sub(pattern, "Ndinda", strn)

print(match)