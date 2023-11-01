def valid(string):
    perfect = True
    
    stack = []
    for c in string:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                perfect = False
                break
            else:
                stack.pop()
    return perfect


def run(string):
    if not string: return string

    balance = 0
    for i, c in enumerate(string):
        if c == '(': balance -= 1
        else: balance += 1
        if balance == 0: break
    u = string[:i+1]
    v = string[i+1:] if i < len(string) else ''
    
    if valid(u): return u + run(v)
    else:
        new_string = f"({run(v)})"
        naked_reversed_u = ['(' if c == ')' else ')' for i, c in enumerate(u) if 0 < i < len(u)-1]
        return new_string + ''.join(naked_reversed_u)
    

def solution(p):
    if valid(p): return p
    return run(p)