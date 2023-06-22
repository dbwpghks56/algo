dt = {"(" : ")", "{" : "}", "[" :"]"}

def brackets(arr):
    stack = []
    
    # 문자열에서 하나씩 빼서 반복
    for a in arr:
        # 여는 괄호면 해당하는 닫는 괄호를 stack 에 저장
        if a in dt:
            stack.append(dt[a])
        
        else:
            # 닫는 괄호면 가장 최근 값과 비교해서 같으면 pop
            if stack and stack[-1] == a:
                stack.pop()
            
            # 다르면 추가
            else:
                stack.append(a)
    # stack이 완전히 비워졌으면 완전한 괄호, 안 비워졌으면 불완전한 괄호
    return stack == []

print(brackets("()"))