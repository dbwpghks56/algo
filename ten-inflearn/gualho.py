s = "{(([]))[]}"
stack = []

for p in s:
    if p == "(":
        stack.append(")")
        
    elif p == "{":
        stack.append("}")
        
    elif p == "[":
        stack.append("]")
        
    elif not stack or stack.pop() != p:
        print(False)
        break
        
print(not stack)