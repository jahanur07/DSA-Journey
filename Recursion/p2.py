def fun_sum(sum,i,n):
  if i>n:
    print(sum)
    return
  fun_sum(sum+i,i+1,n)
  
  
fun_sum(0,1,10)