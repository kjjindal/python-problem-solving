

def check(a):
    hashmap = {}
        ans = 0
        i,j = -1,-1
        while True:
            f1 = False
            f2 = False

            #acquire
            while (i < len(s) - 1):
                f1 = True
                i += 1
                ch = s[i]
                if ch in hashmap:
                    hashmap[ch] += 1
                else:
                    hashmap[ch] = 1

                if hashmap[ch] == 2:
                    break
                else:
                    length = i - j
                    if(length > ans):
                        ans = length

            #release
            while (j < i):
                f2 = True
                j += 1
                ch = s[j]
                hashmap[ch] -= 1

                if hashmap[ch] == 1:
                    break

            if (f1 == False and f2 == False):
                break

        return ans   





if __name__ == '__main__':
    a="kalpitkalpitkalpit"
    print(check(a))
    