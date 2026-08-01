n=int(input("Enter the Number :"))

for cr in range(n):
  for cc in range(n):
    if cc < n-(cr+1):
      print(" ",end=" ")
    else:
      print("*",end=" ")
  print("")