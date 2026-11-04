# using for loop
def fact_fun(n):
  if n == 0 or n ==1:
    return 1

  return n * fact_fun(n-1)
  
  
print(fact_fun(5))

  
