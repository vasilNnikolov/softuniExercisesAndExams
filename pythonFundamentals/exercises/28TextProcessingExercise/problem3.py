filePath = input()
file = filePath.split('\\')[-1]
filename, extension = file.split('.')
print(f'File name: {filename}')
print(f'File extension: {extension}')