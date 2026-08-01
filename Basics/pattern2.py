n=int(input("Enter the number :"))

for i in range(n):
  for j in range(n):
    if j<=i:
      print(j+1,end=" ")
    else:
      print(" ",end=" ")
  print()