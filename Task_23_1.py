def findPal(string):
    def findOdd(string):
        max=1
        for Middle in range(len(string)):
            leftBorder = Middle - 1
            rightBorder = Middle + 1
            while(leftBorder >= 0 and rightBorder<len(string) and string[leftBorder] == string[rightBorder]):
                new_str = string[leftBorder:rightBorder+1]
                if len(new_str) >max: max=len(new_str)
                leftBorder-=1
                rightBorder+=1
        return max
    def findEven(string):
        max=1
        for Middle in range(len(string)):
            leftBorder = Middle
            rightBorder = Middle + 1
            while(leftBorder >= 0 and rightBorder < len(string) and string[leftBorder] == string[rightBorder]):
                new_str = string[leftBorder:rightBorder+1]
                if len(new_str) >max: max=len(new_str)
                leftBorder-=1
                rightBorder+=1
        return max
    return max([findOdd(string), findEven(string)])
string=input()
print(findPal(string))