class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        list1=[]
        count=0
        if len(palindrome)==1 and palindrome!='a':
            return ""
        elif(palindrome=="a"):
            return ""
        
        else:
            for i in palindrome:
                list1.append(i)
                # print(list1)
            for i in range(len(palindrome)):
                if (list1[i]!='a'):
                    list1[i]="a"
                    count=1
                    break
            if list1!=list1[: : -1]:

                if (count==0):
                    list1[i]='b'
                return "".join(list1)
            else:
                return palindrome[:-1]+'b'
            
        # if len(palindrome)==1: return ""
        # n, m = len(palindrome)-1, len(palindrome)
        # while n>=0 and palindrome[n] == "a": n-=1
        # if n >= 0 and (m%2==0 or n!=m//2):
        #     palindrome = palindrome[:m-n-1]+"a"+palindrome[m-n:]
        # else:
        #     palindrome = palindrome[:m-1]+"b"
        # return palindrome
            