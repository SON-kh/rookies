#import mod1
#import mod1 as mo
#from mod1 import PI, add, sub
#from mod1 import *
from mod.mod2 import *

print('__name__:', __name__)



#print(PI)
#print(add(10,2))
#print(add(100,3))

#print(mo.PI)
#print(mo.add(10,2))
#print(mo.sub(4,1))

#print(mod1.PI)
#print(mod1.add(1,3))
#print(mod1.sub(3,1))


def start():
    print('start')

if __name__=='__main__' :
    start()
    