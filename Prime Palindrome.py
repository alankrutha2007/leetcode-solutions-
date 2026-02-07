class Solution:
    def primePalindrome(self, n: int) -> int:
        def prime(p):
            if(p<=1):
                return False
            for i in range(2,int(p**0.5)+1):
                if(p%i==0):
                    return False
            return True
        def palindrome(p):
            if(str(p)==str(p)[::-1]):
                return True
            else:
                return False
        if(n<=11):
            for p in range(n,12):
                if prime(p) and palindrome(p):
                    return p
        p=n
        while(True):
            if(len(str(p))%2==0):
                p = 10 ** len(str(p)) + 1
            if(prime(p) and palindrome(p)):
                return p
            p+=1    
