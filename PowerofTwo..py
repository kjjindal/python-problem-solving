count=n
if(count>=0):
   if(count==0):
       return False
   else:
        while(count>2):
            if(count%2!=0):
                return False
            else:
                count=count/2
        return True
else:
  return False
