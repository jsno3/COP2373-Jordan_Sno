import re

count = 0

pattern = r'(?<=(^|(. )))[A-Z\d].*?(.{3}|[.!?])(?=( [A-Z\d])|$)'

entry = input("Type in any number of sentences, including sentences which begin with numbers.")

number_of_sentences = re.findall(pattern, entry)

for sentence in number_of_sentences:
    print(sentence)
    count += 1

print(len(number_of_sentences))