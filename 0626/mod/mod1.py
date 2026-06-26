print('mod1 실행 시작')
print('mod1 새행', __name__)

def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

print('mod1 실행 종료')


if __name__=='__main__':
    print(PI)
    print(add(10,30))
    print(sub(20,10))