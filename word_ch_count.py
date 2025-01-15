word = input("helo gandu\n")
letters = list(set(word))
dict ={}
for i in letters:
    n=word.count(i)
    dict.update([[i,n]])
print(sorted(dict.items()))