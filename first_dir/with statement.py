#to close the file automatically with statement is used nad everything is done inside with statement

with open("xyz.txt", "r") as f:
    line = f.read()
    print(line)
    print("is file closed:", f.closed)

print("is file closed:", f.closed)
