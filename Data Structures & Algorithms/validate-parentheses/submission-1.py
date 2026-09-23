class Solution:
    def isValid(self, s: str) -> bool:
        left_brackets=['(','[','{']
        right_brackets=[')',']','}']
        st=[]
        for i in range(0,len(s)):
            if s[i] in left_brackets:
                st.append(s[i])
            elif s[i] in right_brackets:
                if not st:
                    return False
                top=st[-1]
                if (s[i]==')' and top!='(') or(s[i]==']' and top!='[')or(s[i]=='}' and top!='{'):
                    return False     
                st.pop()
        return not st 

        