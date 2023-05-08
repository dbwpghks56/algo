t = [73,74,75,71,69,72,76,73]
stack = []
answer = [0] * len(t)

for cur_day, cur_temp in enumerate(t):
    while stack and stack[-1][1] < cur_temp:
        prev_day, _ = stack.pop()
        answer[prev_day] = cur_day - prev_day
    stack.append((cur_day, cur_temp))
    
print(answer)