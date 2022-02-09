def brackets(line):
    # Напишите тело функции
    from collections import deque
    dec_line=deque()
    for i in line:
        if i is '(':
            dec_line.append(i)
        if i is ")" and len(dec_line) == 0:
            return False
        if i is ")" and len(dec_line) != 0:
            dec_line.popleft()
        
            
    if False or len(dec_line) != 0:
        return False
        
    if len(dec_line) == 0:
        return True
        

print(brackets("(()())"))