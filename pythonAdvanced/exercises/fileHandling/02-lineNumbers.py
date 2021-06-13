input_filename = "text.txt"

output_filename = "output.txt"

punctuation_chars = ["-", ",", ".", "!", "?", "'"]

file = open(input_filename, "r")
lines = file.readlines()
file.close()

output = open(output_filename, "w")

for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    n_letters = len([c for c in lines[i] if c.isalpha()])
    n_punctuation = len([c for c in lines[i] if c in punctuation_chars])
    lines[i] = f"Line {i + 1}: " + lines[i] + f"({n_letters})({n_punctuation})\n"
    output.write(lines[i])

output.close()