def check(a):
    b=[i for i in range(1,len(a)+1)]

    for j,k in zip(a,b):
        if(k not in a):
            next=k
            break
        
    for j in a:
        if(a.count(j)>1):
            rpt=j  
            break

    return [rpt,next]        






if __name__ == '__main__':
    a=[3,3,1]
    print(check(a))
    