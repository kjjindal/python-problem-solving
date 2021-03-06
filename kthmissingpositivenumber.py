def check(a,k):
    num=1
    count=1
    while num>0 :
        if(num not in a and count==k):
            print('if')
            return num
        elif(num not in a):
            print('elif',num)
            count=count+1
        num+=1     
           


if __name__ == '__main__':
    a=[1,2,3,4]
    k=2
    print(check(a,k))

    