fileName=input("Enter the file name:")
file=open(fileName,'r')
contents=file.read()
words = contents.split()
numWords = len(words)

print(f"The file \"{fileName}\" contains {numWords} words. ")