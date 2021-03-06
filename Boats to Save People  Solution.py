def check(people,limit):
        people.sort()
        
        
        i = 0
        j = len(people)-1
        boat = 0
        
        while i <=j:
            
            if (i==j):
                boat +=1
                break
            
            if (people[i]+ people[j] <=limit) :
                i +=1
                j-=1
                boat +=1
            else:
                j-=1
                boat +=1
        
        return boat


        
               
    


if __name__ == '__main__':
    a=[5,4,2,1]
    l=6
    print(check(a,l))
    