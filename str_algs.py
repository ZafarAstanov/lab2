def reverse (STR):
    STR2 = ""
    for i in range(len(STR)):
        STR2 += STR[-i - 1]
    return STR2
STR = input()
strnew = reverse(STR)
print(strnew)
    