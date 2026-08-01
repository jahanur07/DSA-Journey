stack=[]
# print(len(stack)==0)
print(not stack)
stack.append(2)
print(len(stack)==0)
stack.append(4)
stack.append(6)
print(stack)
stack.pop()
print(stack)

print(stack[-1])