def count_words(text):
	words = text.split()
	return len(words)

def count_letters(text):
	count = {}
	text = text.lower()
	words = text.split()
	for word in words:
		for char in word:
			if char in count:
				count[char] += 1
			else:
				count[char] = 1

	return count

def print_report(book, count, chars):
	print(f"--- Begin report of {book} ---")
	print(f"{count} words found in the document\n")

	list_of_chars = sorted(chars, key=chars.get, reverse=True)
	for c in list_of_chars:
		if c.isalpha():
			print(f"The '{c}' character was found {chars[c]} times")

	print("--- End report ---")

book = "books/frankenstein.txt"

with open(book) as f:
	file_contents = f.read()

	print_report(book, count_words(file_contents), count_letters(file_contents))
	