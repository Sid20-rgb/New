import pickle

f = open("abc.txt", "rb")
lines = pickle.load(f) #to convert the dumped word to the original one and to read
print(lines)

f.close()