# Python script to input new words into a dictionary
# and store then in JSON format in a fiel

import json 
from random import choice

def print_dictionary(d):
	for word, description in d.items():
		print(f"{word}\n  {description}\n")

def random_word(d):
	return choice(list(d.keys()))

f_dictionary = 'dict_eng.txt'

def clear_dictionary(d):
	conf = input("Are you sure you want to clear the dictionary? (y/n) ")
	if conf.lower().strip() == 'y':
		d.clear()

commands = {
	'_clear': clear_dictionary,
	'_print': print_dictionary,
}

try:
	with open(f_dictionary) as f:
		try:
			words = json.load(f)
		except json.JSONDecodeError:
			print(f"Error decoding {f_dictionary} content")
			words = {} 
except FileNotFoundError:
	print(f"File {f_dictionary} is not found.")

while True:
	word = input('Word: ')
	if word.strip() == 'q':
		break
	elif word.strip() == '_clear':
		commands[word](words)
		continue
	elif word.strip() == '_print':
		commands[word](words)
		continue

	description = input('Desc.: ')

	if description.strip() == 'q':
		break

	words[word] = description

with open(f_dictionary, 'w') as f:
	json.dump(words, f)
