###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('Title is capital letters:' , movie.upper())

# print title in small letters
print('Title in small letters:', movie.lower())

# print how many times the vowel "e" appears in the title
print('Vowel e appears:', movie.count('e'))
# print where in the text is the word "Lord"
print('Index of the world "Lord":', movie.find('Lord'))

# print where in the text is the word "dragon"
print('Index of the world "dragon": ', movie.find('dragon'))