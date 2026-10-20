# brout force solution

# n=int(input("Enter the number : ")) # TC = O(n)  SC = O(k)
# factor = [ ] 
# for i in range(1,n+1):
#   if n%i == 0:
#     factor.append(i)
  
    
# print(factor)
     
     
# better solution

# n=int(input("Enter the number : ")) # TC = O(n/2) == also it's almost O(n)  SC = O(k)
# factor = [ ] 
# for i in range(1,n//2):
#   if n%i == 0:
#     factor.append(i)
  
# factor.append(n)
# print(factor)

# optimum solustion
from math import sqrt
n=int(input("Enter the number : ")) # TC = O(n)  SC = O(k)
factor = [ ] 

for i in range(1,int(sqrt(n))+1):
  if n%i==0:
    factor.append(i)
    if n//i != i:
      factor.append(n//i)
      
print(factor)
     
     