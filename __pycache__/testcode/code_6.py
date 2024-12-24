import sys

args = sys.argv[1:]
words = args.split()
number_of_keywords = words.count(keyword.lower())
print(number_of_keywords)
