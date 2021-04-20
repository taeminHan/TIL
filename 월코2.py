from collections import deque


def solution(s):
    count = 0
    s = deque(s)

    for i in range(len(s)):
        s.append(s.popleft())
        stack = []
        for j in s:
            stack.append(j)
            if len(stack) > 1:
                if stack[-2] + stack[-1] == '{}':
                    stack.pop()
                    stack.pop()
                elif stack[-2] + stack[-1] == '[]':
                    stack.pop()
                    stack.pop()
                elif stack[-2] + stack[-1] == '()':
                    stack.pop()
                    stack.pop()
        if len(stack) == 0:
            count += 1

        s = deque(s)
    print(count)


solution("}]()[{")
