f = open("xyz.txt", "r")
lst = [1]

for position, content in enumerate(f):
    if position in lst:
        print(content)