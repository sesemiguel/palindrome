def palindrome(word):
  s = word[0:len(word)]
  y = len(word)
  for x in range(0, y-1):
    if(s[x] != s[y-1]):
      return False
    else:
      x = x+1
      y = y-1
  return True

print(palindrome("racecar"))
