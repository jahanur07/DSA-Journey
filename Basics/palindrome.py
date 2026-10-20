n=121

num=n
result=0

while num>0:
  id=num%10
  result=(result*10)+id
  num//=10

if n==result:
  print("This is palindrome")
else:
  print("This is not palindrome")