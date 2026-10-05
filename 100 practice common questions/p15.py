#Display the Multiplication Table

# num=int(input("Enter the table number : "))

# for i in range(1,11):
#   print(f"{num} x {i} = {num*i}")
  
def table(num):
  for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
    

num=int(input("Enter the table number : "))

table(num)