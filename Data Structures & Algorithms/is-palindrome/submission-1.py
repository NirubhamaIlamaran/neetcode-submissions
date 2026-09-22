class Solution:
    def isPalindrome(self, s: str) -> bool:
        u=s.lower()
        b=""
        for i in u:
            if i.isalnum():
                b+=i
        print(b)
        return b==b[::-1]

        