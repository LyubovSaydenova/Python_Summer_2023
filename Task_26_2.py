def dis(self):
    for i in self.__dict__:
        print(i, self.__dict__[i])
P = type('Pet', (), {'dis':dis})
aaa = P()
aaa.name = 'bbb'
aaa.dis()
print(aaa)