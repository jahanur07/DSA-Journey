#Found the largest number in 3 number 

a=int(input("Enter the numbe a : "))
b=int(input("Enter the numbe b : "))
c=int(input("Enter the numbe c : "))

if a > b and a > c:
  print(f"{a} is largest number")
elif b > a and b > c:
  print(f"{b} is largest number")
else:
  print(f"{c} is largest number")