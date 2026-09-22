class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        # "ab"
        # one = 0
        # two = 1
        one = 0
        two = len(s) - 1
        while one < two:
            while one < two and s[one].isalnum() == False:
                one+=1

            while two > one and s[two].isalnum() == False:
                two-=1
            
            if s[one].lower() != s[two].lower():
                return False

            one += 1
            two -= 1
        return True
