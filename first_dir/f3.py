f = open("xyz.txt", "r+")
lines = f.read()
print(lines)
f.write("\tHi again")
f.close()