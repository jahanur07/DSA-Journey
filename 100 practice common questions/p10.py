# number is prime or not 

n=int(input("Enter the number : "))
if n==1:
  print("Number is not prime")
if n>1:
  for i in range(2,n):
    if n % i == 0:
      print("not a prime number")
      break
  else:
    print("Number is prime")