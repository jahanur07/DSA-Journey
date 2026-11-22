def check_palindrome(s,left,right):
  if left >= right:
    return True
  if s[left] != s[right]:
    return False
  
  return (check_palindrome(s,left+1,right-1))


s="mamjijmam"
l=len(s)
r=check_palindrome(s,0,l-1)
print(r)