#Python Program to Check If the Number is Armstrong or Not?

n=int(input("Enter the number n : "))
sum=0
temp=n

while temp > 0:
  digit = temp%10
  sum+=digit ** 3
  temp = temp // 10
  
if sum==n:
  print("This is an armstrong number")