def read_text():
    quotes = open("/Users/ljimenez/Desktop/detect-profanity/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

read_text()
