text = input('Enter a word: ')

longest = max(text.split(), key=len)
print("The longest word is: " ,longest)
print("The length of the longest word is: " , len(longest))