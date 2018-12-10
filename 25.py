def findMean(a, m): 
  
    sum = 0
    for i in range( 0, m): 
        sum += a[i] 
      
    return float(sum/m) 
  
# Function for calculating median 
def findMedian(a, m): 
  
    # First we sort the array 
    sorted(a) 
  
    # check for even case 
    if m % 2 != 0: 
        return float(a[m/2]) 
      
    return float((a[int((m-1)/2)] +
                  a[int(m/2)])/2.0) 
  
# Driver program 
a = [ 1, 3, 4, 2, 7, 5, 8, 6 ] 
n = len(a) 
print("Mean =", findMean(a, m)) 
print("Median =", findMedian(a, m)) 
  
