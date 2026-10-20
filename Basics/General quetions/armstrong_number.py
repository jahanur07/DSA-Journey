n=int(input("Enter the number : ")) # TC = O(log10(n)). SC = O(1 )

num=n

nod=len(str(n))
total=0

while num > 0:
  ld = num%10
  total += (ld ** nod)
  num //= 10
  
if n==total:
  print(f"{n} is an armstrong number ")
else:
  print(f"{n} this is not and amrstrong number")
