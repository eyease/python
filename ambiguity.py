import os
return1=os.system('ping -n 4 -w 1 127.0.0.1')  #连通则返回0，否则返回非0值。
if return1==0:
    print ('host up')
else:
    print (': host down')
    #raise Exception('connect failed.')
print (return1)

