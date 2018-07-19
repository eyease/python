money=input()
if money[0:3] in ['RMB','rmb']:
    usd=eval(money[3:])/6.78
    print("USD{:.2f}".format(usd))
elif money[0:3] in ['USD','usd']:
    rmb=eval(money[3:])*6.78
    print("RMB{:.2f}".format(rmb))