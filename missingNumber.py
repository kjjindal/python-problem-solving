def check(a):
    for i in range(len(a)+1):
        if(i not in a):
            return i

if __name__ == '__main__':
    a=[3,0,1]
    print(check(a))
    