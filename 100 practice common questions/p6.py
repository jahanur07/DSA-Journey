#program to positive negative or zero

a=int(input("Enter the number : "))

if a < 0:
  print(f"number is negative {a}")
elif a > 0:
  print(f"number is positive {a}")
else:
  print(f"number is zero {a}")