import os

report_filename = "report.txt"
# for linux
report_filename = os.path.join("/home/vasil/Desktop", report_filename)

# for windows
# report_filename = os.path.join("C:\Users\<name>\Desktop", report_filename)

files = [f for f in os.listdir(".") if os.path.isfile(f)]

extensions = set([tokens[1] for tokens in map(lambda x: x.split("."), files)])

file_by_extension = {}

for e in extensions:
    file_by_extension[e] = list(sorted([f for f in files if f.split(".")[1] == e]))


file_by_extension = dict(sorted(file_by_extension.items(), key=lambda item: item[0]))

with open(report_filename, "w") as output_file:
    for e in file_by_extension:
        output_file.write(f".{e}\n")
        for file in file_by_extension[e]:
            output_file.write(f"- - - {file}.{e}\n")
