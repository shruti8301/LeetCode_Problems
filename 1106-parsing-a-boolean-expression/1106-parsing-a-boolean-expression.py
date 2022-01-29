class Solution():
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        stack = [[]] # dummy layer
        ops = ["!", "&", "|"]
        for i, s in enumerate(expression):
            if s in ops:
                #new layer
                stack.append([s])
                
            if s == ")":
                #eval top layer
                res = stack.pop()
                if res[0] == "!":
                    stack[-1].append(not res[1])
                if res[0] == "&":
                    stack[-1].append(all(res[1:]))
                if res[0] == "|":
                    stack[-1].append(any(res[1:]))
                    
            if s == "t":
                stack[-1].append(True)
            if s == "f":
                stack[-1].append(False)
                
        return stack[0][0]