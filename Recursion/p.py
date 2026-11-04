# def func(i,n):
#   if i>n:
#     return
  
#   print(i)
  
#   func(i+1,n)
  
# func(1,5)

# backtraking

def func(n):
  if n==0:
    return
  func(n-1)
  
  print(n)
  
  
func(5)