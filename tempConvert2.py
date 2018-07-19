tempStr = input()
if tempStr[0] in ['C', 'c']:
    f = eval(tempStr[1:])*1.8+32
    print("F{:.2f}".format(f))
elif tempStr[0] in ['F', 'f']:
    c = (eval(tempStr[1:])-32)/1.8
    print("C{:.2f}".format(c))
