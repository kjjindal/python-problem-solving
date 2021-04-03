def check(string,width):
    count=0
    c=""

    while count<len(string):
        c=c+string[count:count+width]
        c=c+'\n'
        count=count+width
    return c     


if __name__ == '__main__':
    string="abcdefghijklmnopqrstuvwxyz"
    print(check(string,4))
