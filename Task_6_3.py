x = input()
word =[]
number = []
for i in x:
    if i.isalpha():
        if not word or not last_isalpha:
            word.append(i)
        else:
            word[-1] += i
    else:
        if not number or last_isalpha:
            number.append(i)
        else:
            number[-1] += i
    last_isalpha = i.isalpha()
print(word, number,sep="\n")