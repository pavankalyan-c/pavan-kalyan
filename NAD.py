def sumOfAP( b, d,n) : 
    sum = 0
    i = 0
    while i < n : 
        sum = sum + b
        b = b + d 
        i = i + 1
    return sum
      
# Driver function 
n = 20
b = 3.5
d = 2.5
print (sumOfAP(b, d, n)) 
  
