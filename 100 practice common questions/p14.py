#Find the Factorial of a Number - Python Program
 
# without recursion
# num=int(input("Enter the number : "))

# fact=1

# if num < 0:
#   print("Factorial not exist")
# if num == 0:
#   print("Factorial is",1)
# if num > 0:
#   for i in range(1,num+1):
#     fact *= i
#   print(fact)
  
#using recursion

def fact(a):
  if a == 0:
    return 1
  else:
    return (a * fact(a-1))

num=int(input("Enter the number : "))
result=fact(num)
print(f"the factiorial of {num} is {result}")