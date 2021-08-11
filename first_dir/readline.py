f = open("xyz.txt", "r")
lines = f.readline()
num = int(input("Enter a number:"))
print(lines[num - 1])