import pickle

text = "hello"
f = open("abc.txt", "wb")
pickle.dump(text, f)    #dumping and writing dumped obect in abc.txt
print("Dumped")
f.close()