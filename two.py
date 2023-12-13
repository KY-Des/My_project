x = input()
l = "а"
for word in x.split():
    if word.count(l) >= 2:
        print(word)
        