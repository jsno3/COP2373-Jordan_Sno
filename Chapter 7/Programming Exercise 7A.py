import re

count = 0

pattern = r'(?:^|(?<=[?.!]\s))[A-Z\d].*?(?:\.{3}|[.!?])(?=(?: [A-Z\d])|$)'

entry = input("Type in any number of sentences, including sentences which begin with numbers.")

number_of_sentences = re.findall(pattern, entry, flags=re.DOTALL)

length = len(number_of_sentences)

for sentence in number_of_sentences:
    print(sentence)
    count += 1

print(f'There are {length} sentences.')