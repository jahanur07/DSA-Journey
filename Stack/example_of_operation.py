stack=[]
def push():
  element=int(input("Enter the number :"))
  stack.append(element)
  print(stack)
  
  
def pop():
  if not stack:
    print("Stack is empty")
  else:
    e=stack.pop()
    print(stack)
    
    
while True:
  print("Select the operation 1.push 2.pop 3.exit")
  choice=int(input())
  if choice==1:
    push()
  elif choice ==2:
    pop()
  elif choice==3:
    break
  else:
    print("Enter the correct operation")
  