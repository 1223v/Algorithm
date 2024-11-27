from ArrayStack import ArrayStack
def c_B(s): #{ A[ (i+1) ] = 0; }
    stack = ArrayStack(100)
    for ch in s:
        if ch =='{' or ch == '[' or ch=='(':
            stack.push(ch)#stack = [{, [, (]
        elif ch=='}' or ch==']' or ch == ')':
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (ch == '}' and left !='{') or (ch ==']' and left != '[') or (ch==')' and left !='('):
                    return False
    return stack.isEmpty()

s1 = "{ A[ (i+1) ] = 0; }"
s2 = "if( (i==0) && (j==0)"
s3 = "A[ (i+1 ]) = 0; "
print(s1, "--->", c_B(s1))
print(s2, "--->", c_B(s2))
print(s3, "--->", c_B(s3))