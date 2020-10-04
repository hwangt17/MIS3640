fin = open('data/words.txt')

line = repr(fin.readline())
print(line)

for line in fin:
    word = line.strip()
    print(word)