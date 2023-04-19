operators=['+','-','*','/']
precidency={'+':1,'-':1,'*':2,'/':2}
def infix_to_prefix(expression):
    stack=[]
    output=""
    expression=expression[::-1]
    for i in expression:
        if i not in operators:
            output+=i
        elif i==')':
            stack.append(i)
        elif i=='(':
            while stack!=[] and stack[-1]!=')' and precidency[i] < precidency[stack[-1]]:
                output+=stack.pop()
            stack.append(i)
    while stack!=[]:
        output+=stack.pop()
    output=list(output[::-1])
    for i in output:
        if i == '(' or  i==')':
            output.remove(i)
    output="".join(output)
    return output
p = 'p+u+S+H-p*a/r+a/j'
print(infix_to_prefix(p))