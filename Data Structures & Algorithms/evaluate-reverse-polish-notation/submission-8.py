class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        a=0
        b=0

        for token in tokens:
            if token in {"+","-","*","/"}:
                b=int(stack.pop())
                a=int(stack.pop())
                if token=="+":
                    stack.append(a+b)
                elif token=="-":
                    stack.append(a-b)
                elif token=="*":
                    stack.append(a*b)
                elif token=="/":
                    stack.append(int(a/b))     
            else :
                stack.append(int(token))
                
        return stack[0]
        