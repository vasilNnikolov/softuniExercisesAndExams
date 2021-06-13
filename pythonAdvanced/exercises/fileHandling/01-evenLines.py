filename = "text.txt"

file = open(filename, "r")
lines = file.readlines()
file.close()

# get only even lines
lines = [line for index, line in enumerate(lines) if index%2 == 0]

chars_to_substitute = ["-", ",", ".", "!", "?"]
for line in lines:
    reverse_words = line.split(" ")[::-1]
    for i in range(len(reverse_words)):
        for c in chars_to_substitute:
            reverse_words[i] = reverse_words[i].replace(c, "@")
        reverse_words[i] = reverse_words[i].replace("\n", "")
    # print(reverse_words)
    print(" ".join(reverse_words))






