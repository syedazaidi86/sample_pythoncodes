def solution(number):
 z=0
 for x in range(0,number):
  if (x%3==0 or x%5==0):
     z=x+z
 return (z)
    
print(solution(10))
